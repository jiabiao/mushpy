# coding=gbk
from __future__ import division
from sys import world  
from mushpy import trigger,TriggerFlags,async,TimerTask,MatchTask
import time
import re


_hp_data = {}
_th1 = 0
_th2 = 0
_regex_12 = re.compile(u"^12.+气血\.\d+\:(?P<qi1>\d+)/(?P<qi2>\d+)/(?P<qi3>\d+).+内力\.\d+\:(?P<nei1>\d+)/(?P<nei2>\d+)/(?P<nei3>\d+).+精神\.\d+\:(?P<shen1>\d+)/(?P<shen2>\d+)/(?P<shen3>\d+).+精力\.\d+\:(?P<jing1>\d+)/(?P<jing2>\d+)/(?P<jing3>\d+).+经验\.(?P<exp>\d+).+潜能\.(?P<qn>\d+)")
@trigger('^12',name='status_12', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace|TriggerFlags.eOmitFromLog|TriggerFlags.eOmitFromOutput, group='core')
def parse_hp12(*args):
	global _hp_data
	line = args[1]
	result = _regex_12.match(line)	
	if result:
		_hp_data = result.groupdict()



@trigger('〖气血〗：(\d+)\/(\d+)\(\d+%\)\$br#〖内力〗：(\d+)\/(\d+).+【实战体会】：(\d+)\/(\d+)',name='status_hp', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='core')
def parse_hp(*args):	
	global _th1,_th2
	matches = args[2]
	_hp_data["qi1"] = args[2][0]
	_hp_data["qi2"] = args[2][1]
	_hp_data["nei1"] = args[2][2]
	_hp_data["nei2"] = args[2][3]
	_th1 = args[2][4]
	_th2 = args[2][5]

	

def qn():
	return (int)(_hp_data.get("qn",0))

def qi1():
	return (int)(_hp_data.get("qi1",0))

def qi2():
	return (int)(_hp_data.get("qi2",0))

def qi3():
	return (int)(_hp_data.get("qi3",0))

def shen1():
	return (int)(_hp_data.get("shen1",0))

def shen2():
	return (int)(_hp_data.get("shen2",0))

def shen3():
	return (int)(_hp_data.get("shen3",0))

def nei1():
	return (int)(_hp_data.get("nei1",0))

def nei2():
	return (int)(_hp_data.get("nei2",0))

def jing1():
	return (int)(_hp_data.get("jing1",0))

def jing2():
	return (int)(_hp_data.get("jing2",0))


def exp():	
	return (int)(_hp_data.get("exp",0))

def th1():
	return (int)(_th1)

def th2():
	return (int)(_th2)


@async()
def yun_dispel():
	dispel = True
	while dispel:
		if nei1() < 300:
			world.send("myshop buy 1 /clone/vip/zyao2.c")
			yield TimerTask(0,0,1)
			world.send("use zaohua dan")
			yield TimerTask(0,0,2)
			for _ in range(8):
				world.send("yun recover\nyun regenerate\nhp")
				yield TimerTask(0,0,5)
		yield yun_recover()
		world.send("yun dispel")
		matches = yield MatchTask(u"^你调息完毕，将内力收回丹田。|^结果你没发现自己有任何异常。")
		dispel = matches and matches[1].startswith(u"你调息完毕")
		world.send("hp")
		if dispel:
			yield TimerTask(0,0,5.5)
		else:
			yield TimerTask(0,0,2.5)


@async()
def yun_recover():
	if qi2() < qi3():
		world.send("yun heal")
		yield MatchTask(u"^你运功完毕，吐出一口瘀血")	

	if shen2() < shen3():
		world.send("yun inspire")
		yield MatchTask(u"^你缓缓睁开双目，精光四射，神清意爽。")		

	while shen1() / shen2() < 0.6:
		world.send("yun regenerate\nhp")			
		yield TimerTask(0,0,1)

	while nei1() / nei2() < 1.2:
		world.send("yun recover\ndazuo " + str(qi2() - 500))
		yield TimerTask(0,0,11)

	world.send("yun recover")
	world.send("yun regenerate")


@trigger('你感觉内功又精进了：',name='status_dz', flags=TriggerFlags.eEnabled|TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group='core')
def dazuoOK(*args):
	world.send("hp")


_dan_time = 0
_dan_count = 0


def dan_count():
	return _dan_count


def dan_ok():
	return dan_time() < 0

def dan_time():
	return _dan_time + 60 - time.time()



@async()
def recover():

	if qi2() < qi3() or nei1() < nei2():
		if dan_count > 0 and dan_ok():
			world.send("fuyong huxin dan")
			yield TimerTask(0,0,6)
		else:
			world.send("dazuo " + str(qi1() - 1000))
			yield TimerTask(0,0,10)
	world.send("yun recover")
	yield TimerTask(0,0,1)



@trigger('^天王护心丹已经被吃的一丝不剩了',name='status_8', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='core')
def dan1(*args):
	global _dan_count
	global _dan_time
	_dan_count = 0
	_dan_time = time.time()



@trigger('^天王护心丹还能继续使用(.+)次',name='status_9', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='core')
def dan2(*args):
	global _dan_count
	global _dan_time
	_dan_count = 5
	_dan_time = time.time()


@trigger('^东方使者给了你一些天王护心丹。|^东方使者说道：小兄弟你身上',name='status_10', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='core')
def dan2(*args):
	global _dan_count
	_dan_count = 5

#^你上次的药劲儿还没过呢，等会再吃吧。$