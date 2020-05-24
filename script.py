import mdl, sys
from display import *
from matrix import *
from draw import *

"""======== first_pass( commands ) ==========

  Checks the commands array for any animation commands
  (frames, basename, vary)

  Should set num_frames and basename if the frames
  or basename commands are present

  If vary is found, but frames is not, the entire
  program should exit.

  If frames is found, but basename is not, set name
  to some default value, and print out a message
  with the name being used.
  ==================== """
def first_pass( commands ):
    name = ''
    num_frames = 1
    vary_present = False

    for command in commands:
        if (command['op'] == 'frames'):
            num_frames = int(command['args'][0])
        if (command['op'] == 'basename'):
            name = command['args'][0]
        if (command['op'] == 'vary'):
            vary_present = True

    if name == '':
        name = 'anim_00'
        print('No base name provided, set to default "anim_00"')
    if num_frames == 1 and vary_present:
        print("\nERROR: 'vary' command present but frames set to 1 or frames not set. Exiting.")
        sys.exit()

    return (name, num_frames)

"""======== second_pass( commands ) ==========

  In order to set the knobs for animation, we need to keep
  a seaprate value for each knob for each frame. We can do
  this by using an array of dictionaries. Each array index
  will correspond to a frame (eg. knobs[0] would be the first
  frame, knobs[2] would be the 3rd frame and so on).

  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.

  Go through the command array, and when you find vary, go
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropirate value.
  ===================="""

"""
--- frame_data ---
[
  {'spinny': 0.00, 'bigenator': 0.00},
  {'spinny': 0.02, 'bigenator': 0.04},
]
"""

def scale_linear(current_frame, starting_frame, ending_frame, starting_value, ending_value):

    if current_frame >= starting_frame and current_frame <= ending_frame:
        range_of_frames = ending_frame - starting_frame
        range_of_values = ending_value - starting_value

        increment_per_value = range_of_values / range_of_frames
        progress = current_frame - starting_frame

        value = starting_value + increment_per_value * progress

    elif current_frame <= starting_frame:
        value = starting_value
    else:
        value = ending_value

    return value

def scale_quadratic(current_frame, starting_frame, ending_frame, starting_value, ending_value, increment):

    value = 1
    return value

def scale_exponential(current_frame, starting_frame, ending_frame, starting_value, ending_value):

    if current_frame > starting_frame and current_frame <= ending_frame:
        # a and b for equation y = ab^x

        if (starting_value == 0):
            starting_value = .01
        b = pow(ending_value/starting_value, 1/(ending_frame-starting_frame))
        a = starting_value / pow(b, starting_frame)
        value = a * pow(b, current_frame)

    elif current_frame <= starting_frame:
        value = starting_value
    else:
        value = ending_value

    return value

def scale_sinusoidal(current_frame, starting_frame, ending_frame, starting_value, ending_value):
    value = 1
    return value





def second_pass( commands, num_frames ):
    knobs = []
    frames = []
    for command in commands:
        if command['op'] == 'vary':
            knobs.append(command)

    current_frame = 0
    while (current_frame < num_frames):
        frame = {}
        for knob in knobs:
            if knob['type'] == 'linear':
                value = scale_linear(current_frame, knob['args'][0], knob['args'][1], knob['args'][2], knob['args'][3])
            elif knob['type'] == 'quadratic':
                value = scale_quadratic(current_frame, knob['args'][0], knob['args'][1], knob['args'][2], knob['args'][3], knob['args'][4])
            elif knob['type'] == 'exponential':
                value = scale_exponential(current_frame, knob['args'][0], knob['args'][1], knob['args'][2], knob['args'][3])
            elif knob['type'] == 'sinusoidal':
                value = scale_sinusoidal(current_frame, knob['args'][0], knob['args'][1], knob['args'][2], knob['args'][3])

            frame[  knob['knob']  ] = value
        frames.append(frame)
        current_frame += 1
    return frames


def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print("Parsing failed.")
        return

    view = [0,
            0,
            1];
    ambient = [150,
               150,
               150]
    light = [[0.5,
              -0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.7],
                          'green': [0.2, 0.5, 0.7],
                          'blue': [0.2, 0.5, 0.7]}]
    reflect = '.white'

    (name, num_frames) = first_pass(commands)
    frames = second_pass(commands, num_frames)

    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []

    print (symbols)
    for command in commands:
        print(command)

    if num_frames == 1:
        for command in commands:
            # print(command)
            c = command['op']
            args = command['args']
            knob_value = 1

            if c == 'box':
                if command['constants']:
                    reflect = command['constants']
                add_box(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'pyramid':
                if command['constants']:
                    reflect = command['constants']
                add_pyramid(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'cone':
                if command['constants']:
                    reflect = command['constants']
                add_cone(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'cylinder':
                if command['constants']:
                    reflect = command['constants']
                add_cylinder(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'sphere':
                if command['constants']:
                    reflect = command['constants']
                add_sphere(tmp,
                           args[0], args[1], args[2], args[3], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'torus':
                if command['constants']:
                    reflect = command['constants']
                add_torus(tmp,
                          args[0], args[1], args[2], args[3], args[4], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'line':
                add_edge(tmp,
                         args[0], args[1], args[2], args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_lines(tmp, screen, zbuffer, color)
                tmp = []
            elif c == 'move':
                tmp = make_translate(args[0], args[1], args[2])
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'scale':
                tmp = make_scale(args[0], args[1], args[2])
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'rotate':
                theta = args[1] * (math.pi/180)
                if args[0] == 'x':
                    tmp = make_rotX(theta)
                elif args[0] == 'y':
                    tmp = make_rotY(theta)
                else:
                    tmp = make_rotZ(theta)
                matrix_mult( stack[-1], tmp )
                stack[-1] = [ x[:] for x in tmp]
                tmp = []
            elif c == 'push':
                stack.append([x[:] for x in stack[-1]] )
            elif c == 'pop':
                stack.pop()
            elif c == 'display':
                display(screen)
            elif c == 'save':
                save_extension(screen, args[0])
                # end operation loop
    else:
        frame = 0
        while ( frame < num_frames ):
            tmp = new_matrix()
            ident( tmp )

            stack = [ [x[:] for x in tmp] ]
            screen = new_screen()
            zbuffer = new_zbuffer()
            tmp = []
            step_3d = 100
            consts = ''
            coords = []
            coords1 = []
            for command in commands:
                c = command['op']
                args = command['args']
                knob_value = 1

                if c == 'box':
                    if command['constants']:
                        reflect = command['constants']
                    add_box(tmp,
                            args[0], args[1], args[2],
                            args[3], args[4], args[5])
                    matrix_mult( stack[-1], tmp )
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                    tmp = []
                    reflect = '.white'
                elif c == 'pyramid':
                    if command['constants']:
                        reflect = command['constants']
                    add_pyramid(tmp,
                            args[0], args[1], args[2],
                            args[3], args[4])
                    matrix_mult( stack[-1], tmp )
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                    tmp = []
                    reflect = '.white'
                elif c == 'cone':
                    if command['constants']:
                        reflect = command['constants']
                    add_cone(tmp,
                            args[0], args[1], args[2],
                            args[3], args[4], step_3d)
                    matrix_mult( stack[-1], tmp )
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                    tmp = []
                    reflect = '.white'
                elif c == 'cylinder':
                    if command['constants']:
                        reflect = command['constants']
                    add_cylinder(tmp,
                            args[0], args[1], args[2],
                            args[3], args[4], step_3d)
                    matrix_mult( stack[-1], tmp )
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                    tmp = []
                    reflect = '.white'
                elif c == 'sphere':
                    if command['constants']:
                        reflect = command['constants']
                    add_sphere(tmp,
                               args[0], args[1], args[2], args[3], step_3d)
                    matrix_mult( stack[-1], tmp )
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                    tmp = []
                    reflect = '.white'
                elif c == 'torus':
                    if command['constants']:
                        reflect = command['constants']
                    add_torus(tmp,
                              args[0], args[1], args[2], args[3], args[4], step_3d)
                    matrix_mult( stack[-1], tmp )
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                    tmp = []
                    reflect = '.white'
                elif c == 'line':
                    add_edge(tmp,
                             args[0], args[1], args[2], args[3], args[4], args[5])
                    matrix_mult( stack[-1], tmp )
                    draw_lines(tmp, screen, zbuffer, color)
                    tmp = []
                elif c == 'move':
                    if command['knob'] != None:
                        m_move = frames[frame][  command['knob']  ]
                        tmp = make_translate(args[0] * m_move, args[1] * m_move, args[2] * m_move)
                    else:
                        tmp = make_translate(args[0], args[1], args[2])
                    matrix_mult(stack[-1], tmp)
                    stack[-1] = [x[:] for x in tmp]
                    tmp = []
                elif c == 'scale':
                    if command['knob'] != None:
                        m_scale = frames[frame][  command['knob']  ]
                        # m_scale = 1
                        tmp = make_scale(args[0] * m_scale, args[1] * m_scale, args[2] * m_scale)
                    else:
                        tmp = make_scale(args[0], args[1], args[2])
                    # print_matrix (tmp)
                    matrix_mult(stack[-1], tmp)
                    stack[-1] = [x[:] for x in tmp]
                    tmp = []
                    # print (args[0], mul/tiplier, args[0] * multiplier)
                elif c == 'rotate':
                    if command['knob'] != None:
                        m_rot = frames[frame][  command['knob']  ]
                        theta = args[1] * m_rot * (math.pi/180)
                    else:
                        theta = args[1] * (math.pi/180)
                    if args[0] == 'x':
                        tmp = make_rotX(theta)
                    elif args[0] == 'y':
                        tmp = make_rotY(theta)
                    else:
                        tmp = make_rotZ(theta)
                    # print_matrix (tmp)
                    matrix_mult( stack[-1], tmp )
                    stack[-1] = [ x[:] for x in tmp]
                    tmp = []
                elif c == 'push':
                    stack.append([x[:] for x in stack[-1]] )
                elif c == 'pop':
                    stack.pop()
                # end operation loop
            print ("Generating frame " + str(frame) + "...")
            if (frame < 10):
                frame = "0" + str(frame)
            else:
                frame = str(frame)
            save_extension(screen, "anim/" + name + frame + ".png")
            clear_screen(screen)
            clear_zbuffer(zbuffer)
            frame = int(frame) + 1
        print ("Frame generation complete")
