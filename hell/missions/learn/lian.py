# coding=gbk

from mushpy import trigger,async,TriggerFlags,TimerTask,timer,TimerFlags
from sys import world
import hell

_room = None
_config = None
noPot = False
skill = None
skill_value = ["",""]
NAME = "lian"

@async("lian_job")
def entry(config):
	global _room,_config,skill
	if _room == None:
		_config = config
		room_id = config["room"]
		_room = hell.rooms.manager.get_room(room_id)		

	yield hell.rooms.walker.runto(hell.rooms.city.datiepu)	
	world.send(u"buy 1 长剑")
	yield TimerTask(0,0,3)
	world.send(u"buy 1 钢刀")
	yield hell.rooms.walker.runto(_room)	
	world.send("cha")	
	yield TimerTask(0,0,1)
	world.send("cha 2")	
	yield TimerTask(0,0,1)
	yield hell.core.status.yun_dispel()	
	skill = None
	world.send("c")

mission = hell.core.missionfactory.register_mission(NAME, entry)

@async()
def lianxi():
	global skill,skill_value

	if hell.core.status.nei1() < 2000:
		yield hell.core.status.yun_recover()

	sk = hell.core.skills.min_skill(_config["skills"].keys())
	if sk != skill:
		sk_value = _config["skills"][sk]
		world.send("jifa %s %s" % (sk_value[0],sk)) 
		world.send("unwield " + str(skill_value[1]))
		world.send("wield " + str(sk_value[1]))
		skill = sk
		skill_value = sk_value

	cmd = "lian %s 100\neh\nhp\nc" % (skill_value[0])
	world.doafter(1, cmd)


@trigger('^你要向谁求婚',name='lian1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def lian1(*args):
	lianxi().begin()


@trigger('^你的基本.+',name='lian2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def lian1(*args):
	del _config["skills"][skill]





