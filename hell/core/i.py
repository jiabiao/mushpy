# coding=gbk
import re
from sys import world
from mushpy import trigger,TriggerFlags,async,TimerTask

items = None

_regex_item = re.compile(u'zj#.(\d+)?.+?:look (.+?)(?:\#\d+)?\$')

@trigger(u'^07你共有\d+元宝。.+\\n09[^#]+#(.+)\Z',name='inentory_1', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace|TriggerFlags.eOmitFromLog|TriggerFlags.eOmitFromOutput, group='core',multi_line="y",lines_to_match="2")
def parse_inventory(*args):
	global items
	line = args[2][0]
	result = _regex_item.findall(line)
	items = dict((item, count and int(count)) for count,item in  result)

#vanilla icecream

	
def has(item):
	if item == "ba gua":
		item = "/clone/vip/zbagua"
	return items and item in items

def count(item):
	if not has(item):
		return 0
	return items[item] or 1


@async("cun_money")
def cun(self):	
	if count("coin") > 10000:
		world.send("cun %d coin" % (items["coin"]))
		yield TimerTask(0,0,2)

	if count("silver") > 100:
		world.send("cun %d silver" % (items["silver"]))
		yield TimerTask(0,0,2)

	if count("gold") > 10:
		world.send("cun %d gold" % (items["gold"]))
		yield TimerTask(0,0,2)

	if count("cash") > 0:
		world.send("cun %d cash" % (items["cash"]))
		yield TimerTask(0,0,2)
	yield TimerTask(0,0,3)

@async("clear_inventory")
def function(self):
	pass
	