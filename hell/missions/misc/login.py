# coding=gbk

from sys import world  
from mushpy import async,TimerTask,trigger,TriggerFlags
import hell



@async("login_job")
def entry(config):	
	yield hell.rooms.walker.runto(hell.rooms.city.kedian)
	world.send("ask shizhe 结束\nask shizhe 历练\nwear all\nc")

mission = hell.core.missionfactory.register_mission("login", entry)

@trigger('^你要向谁求婚',name='login1', flags=TriggerFlags.KeepEval_Re_Replace, group="login")
def login1(*args):
	mission.end()