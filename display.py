from subprocess import Popen, PIPE
from os import remove, fork, execlp

#constants
XRES = 2000
YRES = 2000
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2

DEFAULT_COLOR = [0, 0, 0]

def smooth_colors(screen, x, y):
    # print(x, y)
    # store_x = x
    # store_y = y
    #
    # x = 0
    # while (x < XRES):
    #     y = 0
    #     while (y < YRES):
    #         if (screen[x][y][RED] != 0 or screen[x][y][GREEN] != 0 or screen[x][y][BLUE] != 0):
    #             # print(screen[x][y], x, y)
    #             red = int((screen[x][y][RED] + screen[x+1][y][RED] + screen[x][y+1][RED] + screen[x+1][y+1][RED]) / 4)
    #             # print (x, y, red, red != 0)
    #         y += 1
    #     x += 1
    #
    # x = store_x
    # y = store_y

    red = int((screen[x][y][RED] + screen[x+1][y][RED] + screen[x][y+1][RED] + screen[x+1][y+1][RED]) / 4)
    green = int((screen[x][y][GREEN] + screen[x+1][y][GREEN] + screen[x][y+1][GREEN] + screen[x+1][y+1][GREEN]) / 4)
    blue = int((screen[x][y][BLUE] + screen[x+1][y][BLUE] + screen[x][y+1][BLUE] + screen[x+1][y+1][BLUE]) / 4)
    # print(red)
    # if (red != 0 or green != 0 or blue != 0):
        # print (red, green, blue)


    return [red, green, blue]


def anti_alias(screen):

    smaller_screen = []
    for x in range( int(YRES / 2) - 1 ):
        row = []
        smaller_screen.append( row )
        for y in range( int(XRES / 2) - 1 ):
            smaller_screen[x].append( smooth_colors(screen, x*2, y*2) )

    smaller_screen[0][0] = [255, 0, 0]
    return smaller_screen


def new_screen( width = XRES, height = YRES ):
    screen = []
    for y in range( height ):
        row = []
        screen.append( row )
        for x in range( width ):
            screen[y].append( DEFAULT_COLOR[:] )
    return screen

def new_zbuffer( width = XRES, height = YRES ):
    zb = []
    for y in range( height ):
        row = [ float('-inf') for x in range(width) ]
        zb.append( row )
    return zb

def plot( screen, zbuffer, color, x, y, z ):
    newy = YRES - 1 - y
    z = int((z * 1000)) / 1000.0

    if ( x >= 0 and x < XRES and newy >= 0 and newy < YRES and zbuffer[newy][x] <= z):
        screen[newy][x] = color[:]
        zbuffer[newy][x] = z

def clear_screen( screen ):
    for y in range( len(screen) ):
        for x in range( len(screen[y]) ):
            screen[y][x] = DEFAULT_COLOR[:]

def clear_zbuffer( zb ):
    for y in range( len(zb) ):
        for x in range( len(zb[y]) ):
            zb[y][x] = float('-inf')

def save_ppm( screen, fname ):
    f = open( fname, 'w' )
    ppm = 'P3\n' + str(len(screen[0])) +' '+ str(len(screen)) +' '+ str(MAX_COLOR) +'\n'
    for y in range( len(screen) ):
        row = ''
        for x in range( len(screen[y]) ):
            pixel = screen[y][x]
            row+= str( pixel[ RED ] ) + ' '
            row+= str( pixel[ GREEN ] ) + ' '
            row+= str( pixel[ BLUE ] ) + ' '
        ppm+= row + '\n'
    f.write( ppm )
    f.close()

def save_extension( screen, fname ):
    screen = anti_alias(screen)

    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( screen ):
    print ('called display')
    ppm_name = 'pic.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def make_animation( name ):
    name_arg = 'anim/' + name + '*'
    name = name + '.gif'
    print('Saving animation as ' + name)
    f = fork()
    if f == 0:
        execlp('convert', 'convert', '-delay', '1.7', name_arg, name)
