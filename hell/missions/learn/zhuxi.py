# coding=gbk

from mushpy import trigger,async,TriggerFlags
from sys import world
import hell

zhuxi_room = hell.rooms.city.shuyuan
noMoney = False
noPot = False


NAME = "zhuxi"

@async("zhuxi_job")
def entry(config):
	yield hell.rooms.walker.runto(zhuxi_room)
	world.send("c")

mission = hell.core.missionfactory.register_mission(NAME, entry)



@trigger('^����˵������̫�����ˣ�����ô�ҵ�|^����Ц��˵��������Ц��',name='zhuxi1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi1(*args):
	global noMoney
	noMoney = True


@trigger('^���Ǳ�ܲ���ѧϰ��ô����ˡ�',name='zhuxi2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi2(*args):
	global noPot
	noPot = True

@trigger('^��о��ڹ��־�����',name='zhuxi3', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi3(*args):
	world.send("n\nn\nxue zhu xi literate 500\nej\nhp\nc")


@trigger('^�����ڵ���̫���ˣ��޷�������Ϣ����ȫ������|^�����ھ��������޷�������Ϣ��������',name='cook_9', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi3(*args):
	world.doafter(5,"ej\neh\ndazuo 200")



@trigger('^��Ҫ��˭���',name='zhuxi4', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi4(*args):
	global noMoney
	global noPot

	if noPot:
		noPot = False
		mission.end()
		return
	if noMoney:
		noMoney = False
		world.send("s\nw\nn\nw\ncun 4000 coin")
		world.doafter(4,"qu 20 silver")
		world.doafter(8,"e\ns\ne\nn\ngive zhu xi 20 silver\nc")
		return
	if hell.core.status.dan_count() == 0:
		world.doafter(6,"s\nw\nn\ne\nask shizhe ���ĵ�")
		world.doafter(8,"w\ns\ne\nn\nc")
		return
	if hell.core.status.nei1() > 800:
		world.doafter(1,"xue zhu xi literate 500\nej\nhp\nc")
		return
	if hell.core.status.dan_ok():
		world.send("fuyong huxin dan")
		world.doafter(6,"xue zhu xi literate 500\nej\nhp\nc")
		return
	world.send("s\ns\neh\ndazuo " + str(hell.core.status.qi2()))
