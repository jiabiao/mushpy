# coding=gbk
from sys import world  
from mushpy import trigger,async,TriggerFlags
import hell


NAME = "tie"

@async("cook_job")
def entry(config):	
	yield hell.rooms.walker.runto(hell.rooms.city.datiepu)
	world.send(u"ask smith 工作")

mission = hell.core.missionfactory.register_mission(NAME, entry)


@trigger('^14(.+)$',name='tie_1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def work(*args):
	world.send(args[2][0])






