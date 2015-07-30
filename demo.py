import sys, os

sys.world = world
sys.g = ax._scriptEngine_.globalNameSpaceModule

if not os.path.dirname(world.getInfo(35)) in sys.path:
    sys.path.append(os.path.dirname(world.getInfo(35)))
from mushpy import *



@async
def Jobs(name):

    count = 0

    while True:        
    	yield work()
        yield sleep()
        count+=1
        world.Note('work done. (%s times)' % count)

@async
def work():
    world.Note("working 1")
    yield TimerTask(0,0,5)
    world.Note("working 2")

    world.DoAfter(3,'hi')
    yield MatchTask(u'^你双手抱拳，作了个揖道：各位英雄请了！$')



@async
def sleep():
    world.send('sleep')
    yield TimerTask(0,0,5) #or yield MatchTask(u'^你一觉醒来......$'）
    world.note('awake')


#then call in command line:jobs("name").begin()
