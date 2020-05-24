# MKS66_Final_Project
## Brian Moses, Mohidul Abedin— Computer Graphics, pd 4
## Features
  * Add new primitive shapes
    - Cylinder
      - cylinder x y z radius height 
      - x y z- is the position of the bottom center
    - Cone 
      - cone x y z radius height 
      - x y z- is the position of the center of the base
    - Pyramid
      - pyramid x y z side height
      - x y z- is the position of the apex
  * Change behavior of vary
    - Oscilating/sinusoidal
      - The value of the knob is determined by a sin function
    - Exponential
      - The value of the knob grows/decayse exponentially 
    - Quadratic 
      - Follows a parabola 
    - Syntax
      - vary knob behavior start_frame end_frame start_value end_value extra_param
      - behavior- linear, exponential, sinusoidal, quadratic
      - extra_param- 
        - If behavior is quadratic the extra_param is a in ax^2 
        - If behavior is exponential the extra_param is the base
        - If behavior is sinusoidal or linear the extra_param is ignored
  * Anti-aliasing
    - Improve lines that are drawn using the engine
## If there is time (one of)
  * Mesh
  * Texture Mapping
