# coding=gbk
from sys import world
from mushpy import trigger,TriggerFlags,async,McObject
import hell
import missionfactory


temp_configs = []

def add_temp_mission(config):
	temp_configs.append(config)

@async("check_temp")
def check_temp_mission():
	while len(temp_configs):
		high_priority_config = temp_configs[0]
		for config in temp_configs:
			if config.get("priority",0) > high_priority_config.get("priority",0):
				high_priority_config = config	

		temp_configs.remove(high_priority_config)				
		yield missionfactory.start(high_priority_config)
		

@async("root")
def run():
	main_config = hell.core.login.me.mission
	if main_config == None:
		print "main config is None"
		return
	while True:
		yield check_temp_mission()
		yield missionfactory.start(main_config)

@trigger(u'^你连线进入了',name='mission_start', group='core')
def _start(*args):
	triggerlist = world.GetTriggerList
	if (triggerlist):
		for t in triggerlist:
			group = world.GetTriggerOption(t, "group")
			if not group:
				world.DeleteTrigger(t)
			elif group != "core":
				world.EnableTrigger(t,False)

	timerlist = world.GetTimerList
	if (timerlist):
		for t in timerlist:
			group =  world.GetTimerOption(t, "group")
			if not group:
				world.DeleteTimer(t)   
			elif group != "core":
				world.EnableTimer(t,False)
	temp_configs.append({"name":"login"})
	run().begin()


# @trigger(u'^000008$',name='born_start', group='core')
# def _born(*args):
# 	world.EnableTrigger("restart", False)
# 	run().begin()


@trigger('^东方使者向你千里传音：你输入的指令过多|^重新连线完毕。',name='restart', group='core')
def restart(*args):	
	world.doafter(3,"halt\nhalt\nquit")

@trigger('^你吐了几口鲜血，在地上抽动了几下就死了！',name='die', group='core')
def die(*args):	
	hell.core.login.me.mission = None
	world.EnableGroup ("kill", 0) 


