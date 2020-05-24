
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONE CONSTANTS DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE MESH MOVE POP PUSH ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : CONE NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONE NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,27,33,35,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[-1,0,-1,-3,-9,-10,-12,-14,-56,-65,-2,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'COMMENT':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[3,3,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'POP':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[4,4,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'PUSH':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[5,5,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SCREEN':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[6,6,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SAVE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[7,7,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'DISPLAY':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[8,8,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SPHERE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[9,9,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'CONE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[10,10,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'TORUS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[11,11,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'BOX':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[12,12,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'LINE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[13,13,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'MOVE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[14,14,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SCALE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[15,15,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'ROTATE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[16,16,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'FRAMES':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[17,17,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'BASENAME':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[18,18,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'VARY':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[19,19,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SET':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[20,20,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SET_KNOBS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[21,21,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'AMBIENT':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[22,22,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'CONSTANTS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[23,23,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'LIGHT':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[24,24,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SHADING':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[25,25,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'CAMERA':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[26,26,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[27,27,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'MESH':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[28,28,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[29,29,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'SAVE_COORDS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[30,30,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'TWEEN':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[31,31,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'FOCAL':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[32,32,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'WEB':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[33,33,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'TEXTURE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,131,132,137,138,140,141,142,144,152,157,158,159,160,161,162,164,170,172,173,174,175,176,177,179,181,183,184,185,186,189,192,198,199,],[34,34,-3,-9,-10,-12,-14,-56,-65,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-11,-13,-44,-48,-57,-40,-42,-43,-50,-59,-58,-15,-39,-41,-60,-63,-17,-16,-19,-23,-47,-18,-20,-21,-24,-25,-27,-31,-55,-22,-26,-28,-29,-32,-33,-35,-53,-30,-34,-37,-36,-38,-51,-52,-66,]),'DOUBLE':([6,9,10,11,12,13,14,15,17,21,22,26,31,32,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,61,62,63,65,70,72,75,76,77,78,79,80,81,82,83,84,85,86,88,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,111,113,114,115,119,121,122,123,124,125,126,127,128,129,130,133,134,135,136,139,143,145,146,147,148,149,150,151,153,154,155,156,163,165,166,167,168,169,171,178,180,182,187,188,190,191,192,193,194,195,196,197,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,-4,-5,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'STRING':([7,18,38,39,40,41,42,66,95,],[40,40,40,-6,-7,-4,-5,40,40,]),'XYZ':([7,9,10,11,12,13,16,18,19,20,23,24,28,29,30,34,37,38,39,40,41,42,66,87,94,95,96,106,108,109,117,118,120,130,141,142,144,159,161,162,164,175,177,179,185,],[41,41,41,41,41,41,55,41,41,41,41,41,41,41,41,41,-8,41,-6,-7,-4,-5,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'ID':([7,9,10,11,12,13,18,19,20,23,24,28,29,30,34,37,38,39,40,41,42,66,87,94,95,96,106,108,109,117,118,120,130,141,142,144,159,161,162,164,175,177,179,185,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-8,42,-6,-7,-4,-5,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'SHADING_TYPE':([25,],[64,]),'CO':([28,41,42,67,],[66,-4,-5,95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,35,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,12,13,14,15,17,21,22,26,31,32,36,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,61,62,63,65,70,72,75,76,77,78,79,80,81,82,83,84,85,86,88,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,111,113,114,115,119,121,122,123,124,125,126,127,128,129,130,133,134,135,136,139,143,145,146,147,148,149,150,151,153,154,155,156,163,165,166,167,168,169,171,178,180,182,187,188,190,191,192,193,194,195,196,197,],[36,43,45,47,49,51,53,54,56,60,61,65,70,71,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,114,115,119,120,121,122,123,124,125,126,127,128,130,133,134,135,136,139,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,159,161,162,163,164,165,166,167,168,169,170,171,175,177,178,179,180,181,182,185,187,188,190,191,192,193,194,195,196,197,198,199,]),'TEXT':([7,18,38,66,95,],[38,57,74,94,117,]),'SYMBOL':([7,9,10,11,12,13,18,19,20,23,24,28,29,30,34,38,66,87,94,95,96,106,108,109,117,118,120,130,141,142,144,159,161,162,164,175,177,179,185,],[39,44,46,48,50,52,39,58,59,62,63,67,68,69,72,39,39,110,116,39,118,129,131,132,137,138,140,150,157,158,160,172,173,174,176,183,184,186,189,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',124),
  ('input -> command input','input',2,'p_input','mdl.py',125),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',129),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',133),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',134),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',138),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',139),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',143),
  ('command -> POP','command',1,'p_command_stack','mdl.py',147),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',148),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',152),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',153),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',160),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',164),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',168),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',169),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',170),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',171),
  ('command -> CONE NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_cone','mdl.py',185),
  ('command -> CONE NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_cone','mdl.py',186),
  ('command -> CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_cone','mdl.py',187),
  ('command -> CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_cone','mdl.py',188),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',203),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',204),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',205),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',206),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',220),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',221),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',222),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',223),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',237),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',238),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',239),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',240),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',241),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',242),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',243),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',244),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',265),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',266),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',274),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',275),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',283),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',284),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',292),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',297),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',302),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',308),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',309),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',320),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',326),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',327),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',333),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',339),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',345),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',350),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',354),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',355),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',356),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',357),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',371),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',377),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',384),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',389),
  ('command -> WEB','command',1,'p_web','mdl.py',393),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',397),
]
