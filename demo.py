import sys, os

sys.world = world
sys.g = ax._scriptEngine_.globalNameSpaceModule

if not os.path.dirname(world.getInfo(35)) in sys.path:
    sys.path.append(os.path.dirname(world.getInfo(35)))
from mushpy import *



@async
def work(name):

    count = 0

    while True:
        world.Note("working 1")
        yield TimerTask(0,0,5)

        world.Note("working 2")

        world.DoAfter(3,'hi')
        yield MatchTask(u'^��˫�ֱ�ȭ�����˸�Ҿ������λӢ�����ˣ�$')

        yield sleep()

        count+=1
        world.Note('work done. (%s times)' % count)
        

@async
def sleep():
    world.send('sleep')
    yield TimerTask(0,0,5) #or yield MatchTask(u'^��һ������......$'��
    world.note('awake')


#then call in command line:work("name").begin()
