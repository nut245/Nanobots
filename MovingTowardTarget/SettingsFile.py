# specifies the dimensions of the program, in in pixels
GAMEWIDTH = 1000
GAMEHEIGHT = 700

# specifies the size of cubes generated on border of game window
BORDERSIZE = 20

# specifies how many pxiels nanobots traverse per specified FPS_MS
NANOBOTSPEED = 3

# specifies the tick speed/refresh cycles, in milliseconds
FPS_MS = 1

# specifies the number of nanobots initially generated
NANOBOT_NUMBER = 500

# specifies the number of times target must be found before being
# surrounded by all nanobots
TARGET_FOUND_CONDITION = 20

# specifies visual aesthetic of nanobots once target is being surrounded
# - SPEEDUP_WHEN_TARGET_FOUND: multiplies the speed of nanobots
# - TOGGLE_DELETE_NANOBOTS: deletes nanobot when in contact with target
SPEEDUP_WHEN_TARGET_FOUND = False
TOGGLE_DELETE_NANOBOTS = False