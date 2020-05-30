// NOTE: file has .java extension for color highlighting in atom

frames 10
basename cannon_00

// constants colors [red_ambient, red_diffuse, red_specular] [green] [blue]
constants wood .052 .52 .52 .037 .37 .37 .026 .26 .26
constants steel .0357 .357 .357 .0376 .376 .376 .0396 .396 .396
constants cannonball_color .04 .4 .4 .043 .43 .43 .042 .42 .42

// vary constants
vary exponential cannonball_anim 0 9 .01 1
vary linear slow_down 4 9 0 1

push
move -20 0 0 cannonball_anim
move 5 0 0 slow_down
move 150 150 0
rotate x 100
rotate y 10
// wheel, farther
torus wood 0 0 0 15 75
// axle connecting wheels
box wood -10 150 10 20 150 20
move 0 150 0
// wheel, closer
torus wood 0 0 0 15 75
move -50 -50 0
// cannon firing part
box steel 0 0 0 250 50 50
push
rotate y 20
// stabilizes cannon w/ ground
box -100 -15 30 200 20 20
pop
push
move 60 55 0
// wheel axles
box wood -80 0 10 150 20 20
rotate y 90
box wood -70 8 0 145 20 20
pop
// cannonball
push
move 280 0 -30
move 300 0 0 cannonball_anim
sphere cannonball_color 0 0 0 25
