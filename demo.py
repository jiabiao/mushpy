import sys, os

sys.world = world
sys.g = ax._scriptEngine_.globalNameSpaceModule

if not os.path.dirname(world.getInfo(35)) in sys.path:
	sys.path.append(os.path.dirname(world.getInfo(35)))
from mushpy import *



@async
def work(name):
	world.DoAfter(3,'hi')
	yield MatchTask(u'^你双手抱拳，作了个揖道：各位英雄请了！$'）

	world.send('hp')
	yield TimerTask(0,0,5)
	
	yield sleep()
	world.send('say all done')

@async
def sleep():
	world.send('sleep')
	yield TimerTask(0,0,5)
	world.note('awake')


#then call in command line:work().begin()