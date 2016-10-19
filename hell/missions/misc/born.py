# coding=gbk


from mushpy import trigger,async,TriggerFlags,TimerTask
from sys import world
import hell



NAME = "born"
_config = None

@async("born_job")
def entry(config):		
	global _config
	_config = config
	world.send(_config["sex_name"])
	yield TimerTask(0,0,0.1)	


mission = hell.core.missionfactory.register_mission(NAME, entry)


@trigger('^你可以进入不同的方向选择品质和先天属性',name='born2', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='born')
def name(*args):
	world.send(_config["character"])
	world.send("out")
	world.send("washto " + _config["point"])
	world.send("born " + _config["born"])


@trigger(u'^你与生俱来的技能有：(.+)。',name='born3', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='born')
def spcial(*args):
	msg = args[2][0]
	if not match(msg):
		world.send("suicide -f")

def match(msg):
	spcials = msg.split(u"、")
	print msg	

	count = 0
	for s in _config["special"]:
		if s in spcials:
			count = count + 1
	if count == _config["require_count"]:
		return True
	if count == 0:
	    return False
	if count == 1:
		return len(spcials) == 3















