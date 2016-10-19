# coding=gbk

from sys import world  
from mushpy import trigger,TriggerFlags,MatchTask,ValueTask,async


@trigger('^“啪”的一声一',name='common_1', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace|TriggerFlags.eOmitFromLog|TriggerFlags.eOmitFromOutput, group='core')
def dan(*args):
	world.send("get dan\nbaocun dan")






@trigger('^00(.+)$',name='common_2', flags=TriggerFlags.eEnabled|TriggerFlags.KeepEval_Re_Replace|TriggerFlags.eOmitFromLog|TriggerFlags.eOmitFromOutput, group='core')
def dan(*args):
	world.AppendToNotepad("chat", args[2][0] + "\r\n")



@async()
def exists_npc(id):
	world.send("follow " + id)
	matches = yield MatchTask(u"^你决定开始跟随|^这里没有")
	result = matches and matches[1].startswith(u"你决定开始跟随")
	yield ValueTask(result)




