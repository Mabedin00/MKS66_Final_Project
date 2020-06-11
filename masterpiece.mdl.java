// NOTE: file has .java extension for color highlighting in atom

frames 100
basename masterpiece_00

// constants colors [red_ambient, red_diffuse, red_specular] [green] [blue]
constants gnome_hat .2 .1 .7 0 0 0 0 0 0
constants gnome_face .2  .7  .4 .18 .63 .36 .14 .49 .28
constants gnome_coat .14 .4 .237 .17 .6 .33 .18 .63 .3
constants eyes .0 0 1 0 0 1 0 0 1

// vary constants
vary sinusoidal hang 0 60 0 1 2
vary sinusoidal hang_end 60 100 0 1 1
vary sinusoidal hang_end_cylinder 60 100 0 1 .8
vary quadratic gravity 60 100 0 1 .001
vary linear momentum 60 100 0 1

push
move 500 1000 0
rotate x 20
rotate z 75 hang
rotate z 25 hang_end
move 0 -1200 0 gravity
push
rotate z 60 hang_end_cylinder
move 900 0 0 momentum
cylinder 0 0 0 2 230
pop
move 1575 0 0 momentum
move 0 -230 0
cone gnome_hat 0 0 0 50 80
move 0 -100 0
push
scale 0.8 1 1
sphere gnome_face 0 0 0 50
pop
sphere eyes -15 14 38 10
sphere eyes 15 14 38 10
push
move 0 -45 0
cylinder gnome_coat 0 0 0 60 90
move 0 -90 0
cylinder -20 0 0 25 70
cylinder 20 0 0 25 70
display
