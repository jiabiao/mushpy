# coding=gbk
import re
from sys import world
from mushpy import trigger,TriggerFlags,async,TimerTask
import hell

_skills = {}

_regex_skills= re.compile(u'(\d+)\/.+?(\S+)\$zj\#')




@trigger(u'^07你目前所学到的所有技能：\\n09(.+)\Z',name='skills_1', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace|TriggerFlags.eOmitFromLog|TriggerFlags.eOmitFromOutput, group='core',multi_line="y",lines_to_match="2")
def parse_skills(*args):
	global items
	line = args[2][0]
	result = _regex_skills.findall(line)
	for lvl,skill in result:
		_skills[skill] = (int)(lvl)

@trigger('^恭喜: 你的「.+」进步了！',name='skills_2', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace, group='core')
def dan1(*args):
	world.send("cha 2")
	world.doafter(0.5,"cha")
	

def level(skill):
	return _skills.get(skill,0)

def min_skill(skills):
	return min(filter(lambda x: x in skills, _skills),key=_skills.get)

def max_skill_lvl():
	knowledges = ["literate","zuoyou-hubo","buddhism"]
	skill = max(filter(lambda x: not x in knowledges, _skills),key=_skills.get)
	return _skills[skill]


@async()
def fangqi():
	max_lvl = max_skill_lvl() + 2
	min_exp = max_lvl * max_lvl * max_lvl / 10
	_exp = hell.core.status.exp() - min_exp
	print "fangqi exp:" + str(_exp)
	if _exp > 100000000000:
		world.send("fangqi exp " + str(_exp))
		yield TimerTask(0,0,1.5)