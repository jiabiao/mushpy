

import sys, os


sys.world = world
sys.g = ax._scriptEngine_.globalNameSpaceModule

_path = os.path.dirname(world.getInfo(35))
sys.path.append(_path)
os.chdir(_path)
import mushpy
import hell
import hell.rooms as d
