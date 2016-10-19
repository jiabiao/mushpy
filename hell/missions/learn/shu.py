# coding=gbk

from mushpy import trigger,async,TriggerFlags,TimerTask
from sys import world
import hell

_room = None
_config = None
noPot = False


NAME = "shu"

@async("du_shu_job")
def entry(config):
	global _room
	if _room == None:
		_config = config
		room_id = config["room"]
		_room = hell.rooms.manager.get_room(room_id)
	yield hell.rooms.walker.runto(_room)
	world.send("c")

mission = hell.core.missionfactory.register_mission(NAME, entry)



@trigger('^你感觉内功又精进了',name='du_shu1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi3(*args):
	world.send("c")


@trigger('^你现在的气太少了，无法产生内息运行全身经脉。|^你现在精不够，无法控制内息的流动！',name='du_shu2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi3(*args):
	world.doafter(5,"ej\neh\ndazuo 100")



@trigger('^你要向谁求婚',name='du_shu3', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi4(*args):
	if hell.core.status.dan_count() == 0:
		get_dan().begin()
	if hell.core.status.nei1() > hell.core.status.nei2() * 0.5:
		world.doafter(0.5,"ds\nhp\nc")
		return
	if hell.core.status.dan_ok():
		world.send("fuyong huxin dan")
		world.doafter(6,"ds\nhp\nc")
		return
	qi = hell.core.status.qi1() - 20
	if qi > 10:
		world.send("dazuo " + str(qi))
	else:
		world.doafter(10,"c")


@async("shu_get_dan")
def get_dan():
	yield TimerTask(0,0,20)
	world.send("ej")
	yield hell.rooms.walker.runto(hell.rooms.city.kedian)
	world.send("ask shizhe 护心丹")
	yield TimerTask(0,0,1)	
	yield hell.rooms.walker.runto(_room)
	world.send("c")

