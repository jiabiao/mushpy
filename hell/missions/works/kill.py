# coding=gbk
from __future__ import division
from sys import world  
from mushpy import trigger,async,enum,TriggerFlags,TimerTask,ManualEndTask,ValueTask,timer,TimerFlags
import time
import hell.core.i as i
import hell


step = None
_master_room = None  
_master_id = None
_config = None
_quest_count = 0   #������
_questing = False  #�Ƿ�������
_fee = False       #npc�Ƿ�������ã�ΪTrueʱ_area��Ч
_area = None       #��������
_outdoor = None    #����Ŀ¼
_room = None       #������
_followed = False  #�Ƿ����NPC
_killer_id = None  #npc id
_killer_name = None #npc name
_killer_die = False #npc �Ƿ�����
_letter = False
_dispel =False      #�Ƿ���Ҫ����            
_back = False       #�Ƿ���Ҫ��ͷ��ȥ��ʦ��
_repair = False
_aroundMET = ManualEndTask("kill_around")
NAME = "kill"



@async("kill_job")
def entry(config):	
	global _config,step,_master_id,_master_room

	if _master_room == None:
		_config = config
		room_id = config["quest_room"]
		_master_id = config["quest_master"]
		_master_room = hell.rooms.manager.get_room(room_id)
	world.send("cha")	
	yield TimerTask(0,0,1)
	world.send("cha 2")	
	yield TimerTask(0,0,1)
	world.send(_config["jifa_cmd"])
	yield TimerTask(0,0,1)
	world.send("quest\ni\nc")
	step = "master"

mission = hell.core.missionfactory.register_mission(NAME, entry)

@trigger('��Ҫ��˭��飿',name='kill_0', flags=TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME)
def do(*args):
	world.note("kill steps:" + str(step))
	globals()[step]().begin()

@async()
def cancel():	
	global step
	yield hell.rooms.walker.runto(_master_room)		
	if not i.has("/clone/misc/head"):
		yield jiqu_wait(8)
		world.send("quest cancel")
		yield TimerTask(0,0,8)
	world.send("i\nc")	
	step = "master"

@async()
def master():
	global step
	yield TimerTask(0,0,0.1)	

	if i.has("/clone/misc/head"):
		yield hell.rooms.walker.runto(_master_room)	
		world.send("give head to " + _master_id)

	if len(hell.core.missionDispatcher.temp_configs) > 0:
		mission.end()
		return

	yield hell.rooms.walker.runto(_master_room)	
	world.send("quest " + _master_id)
	yield TimerTask(0,0,2)

	world.send("quest\ni\nc")
	step = "check_quest"


@async()
def check_quest():
	global step,_room,_repair

	if not _questing:
		print "accept failed,waiting..."
		yield TimerTask(0,1,0)
		world.send("quest\ni\nc")
		step = "master"
		return

	if not i.has("/clone/vip/zbagua"):
		if  not i.has("/clone/money/gold") and not i.has("/clone/money/cash"):
			yield hell.rooms.walker.runto(hell.rooms.city.qianzhuang)
			world.send("qu 5 cash")
			yield TimerTask(0,0,3)	
		world.send("myshop buy 1 /clone/vip/zbagua.c")
		yield TimerTask(0,0,0.5)

	if _repair:
		_repair = False
		if i.count("/clone/money/cash") < 4:
			yield hell.rooms.walker.runto(hell.rooms.city.qianzhuang)
			world.send("qu 5 cash")
			yield TimerTask(0,0,3)	
		yield hell.rooms.walker.runto(hell.rooms.city.datiepu)	
		for item in _config["repairs"]:
			world.send("repair %s\nrepair %s\nwear all" % (item,item))
			yield TimerTask(0,0,11)

	_room = None
	world.send("use ba gua\nhp\nc")
	step = "search"

# @async()
# def recover():
# 	if not i.has("huxin dan"): 
# 		yield TimerTask(0,0,1)
# 		yield hell.rooms.walker.runto(hell.rooms.city.kedian)
# 		world.send("ask shizhe ���ĵ�\nw")
# 		yield TimerTask(0,0,1)


# 	status = hell.core.status
# 	time = status.dan_time()
# 	if 	time < 10 or status.qi2() / status.qi3() < 0.9 or status.nei1() / status.qi2() < 0.9:
# 		if time > 3:
# 			yield jiqu_wait(time)
# 		for _ in range(3):
# 			world.send(_config["lian_cmd"])
# 			yield TimerTask(0,0,1)
# 		world.send("fuyong huxin dan")
# 		yield TimerTask(0,0,6)

@async()
def search():
	global step

	if not _room:
		world.send("i\nc")
		step = "cancel"
		return	

	yield hell.core.status.yun_recover()

	rooms = hell.rooms.manager.find_near_start_rooms(_area,_outdoor ,_room,8) 
	if (not rooms) or len(rooms) == 0:
		rooms = hell.rooms.manager.find_near_start_rooms(None ,_outdoor,_room,8) 
	if len(rooms) == 0:
		print "** not found room. area:%s,room:%s" % (_area,_room)
	found = False

	while len(rooms) > 0: 
		room = yield hell.rooms.walker.run_near(rooms)
		if not room:
			room = rooms[0]
			yield hell.rooms.walker.runto(room)

		rooms.remove(room)
		found = yield around(room)
		if found:
			world.send("c")
			step = "kill"
			return

	print "not found,cancel"
	world.send("i\nc")
	step = "cancel"

@async()
def around(room):
	global _followed,step
	_followed = False
	step = "arounding"

	world.send("follow %s\nc" %(_killer_id))		
	yield _aroundMET
	if _followed:
		yield ValueTask(True)
		return

	exits = hell.rooms.manager.get_exits_around(room,2)  #4�ܱ�֤ȫ���ǣ�����Ч�ʵ�
	for exit in exits:
		if exit.cmdTask:		
			yield exit.cmdTask(*exit.cmdTaskArgs)
		else:
			world.send(exit.cmd or exit.direction)		
		world.send("follow %s\nc" %(_killer_id))		
		yield _aroundMET
		if _followed:
			yield ValueTask(True)
			return
	yield ValueTask(False)


@async()
def arounding():
	yield TimerTask(0,0,0.2)
	_aroundMET.end()


@async()
def kill():
	global _fee,_killer_die
	yield TimerTask(0,0,0.1)
	_fee = False
	_killer_die = False
	me = hell.core.login.me
	if hell.core.login.me.preper_kill:
		world.send(hell.core.login.me.preper_kill)
	world.send("kill %s\nimbue combat" %(_killer_id))
	if me.pfm:
		world.send(me.pfm + " " + _killer_id)



@async()
def kill_end():
	global step,_dispel

	if not _back and _killer_die:
		world.doafter(10,"accept quest")
		t1 = time.time()		
		if _dispel or hell.core.status.shen2() < hell.core.status.shen3() :
			_dispel = False
			yield hell.core.status.yun_dispel()
		yield hell.core.status.yun_recover() 
		t2 = time.time()
		t = t1 + 10 - t2
		if t > 1:
			yield jiqu_wait(t)
	elif _dispel or hell.core.status.shen2() < hell.core.status.shen3() :
		_dispel = False
		yield hell.core.status.yun_dispel()


	if i.has("/clone/box/lack_card"):
		world.send("xuyuan lack card")
		yield TimerTask(0,0,0.5)

	if i.has("/clone/vip/putao"):
		world.send("eat putao")
	if i.has("/clone/box/vip_box"):		
		world.send("baocun vipbox")
	if i.has("/clone/box/chuji_box"):
		world.send("drop box no1")
	if i.has("/clone/box/zhongji_box"):
		world.send("drop boxno2")
	if i.has("/clone/box/gaoji_box"):
		world.send("baocun boxno3")
	if i.has("/clone/box/chaoji_box"):
		world.send("baocun boxno4")
	yield TimerTask(0,0,0.2)
	yield hell.core.skills.fangqi()	

	if _back:
		step = "master"
	else:
		step = "check_quest"
	world.send("quest\ni\nc")

@trigger('^ʦ����������������Ѿ����������\s*(\d+)\s*����$',name='kill_1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def kill1(*args):
	global _quest_count	
	_quest_count = (int)(args[2][0])

@trigger('^������û�����κ�����$',name='kill_2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def kill2(*args):
	global _questing
	_questing = False

@trigger('^(.+)Ŀǰ����(.+?)��(.+)���$',name='kill_3', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def kill3(*args):
	global _killer_name,_killer_id,_room,_outdoor
	_killer_name = args[2][0]
	_killer_id = hell.name.get_cn_id(_killer_name)
	_outdoor = args[2][1]
	_room = args[2][2]

@trigger('^��˵����ǰ����������(.+)��û��$',name='kill_4', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def kill4(*args):
	global _area,_questing
	_questing = True
	_area = args[2][0]


@trigger(u'^�������ʼ����(.+)һ���ж���$',name='kill_9', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def kill9(*args):
	global _followed
	if(args[2][0] == _killer_name):
		_followed = True

@trigger(u'^.{0,8}�������䣬ͻȻһ�˼���ææ�ĸ��˹���|�����뿪��ͻȻһ��ͬ��װ���ĵ��Ӽ���ææ�ĸ��˹���|^.{0,8}���һ�������¼�����Ѫ|^.{0,8}ҡҡ��׹���ۿ���Ҫ��������|^����һ���֮�£�|^.{0,8}����һ��������ɫ��΢����һ|^�������������ۿ���Ҫ���֣���|^.{0,8}����һ����ȴ����С��|^.{0,8}�������£���Ȼ����������ס|^.{0,8}�����ˣ���Ȼ���У����߼�',name='kill_11', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def kill11(*args):
	global step,_fee
	_fee = True

@trigger('��æ����������������������ɣ�',name='kill_13', flags=TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME)
def kill13(*args):
	world.doafter(0.5,"hp\nimbue combat")


@trigger('���������ڴ�ܣ�ûʱ������Щ���顣',name='kill_14', flags=TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME)
def kill14(*args):
	me = hell.core.login.me
	status = hell.core.status
	if _killer_die: # Ŀ�����ˣ�����ս����˵���а���
		hell.rooms.walker.move(1).begin()
	elif (status.qi2() / status.qi3() < me.heal_factor) or (status.shen2() / status.shen3() < me.inspire_factor) :
		hell.rooms.walker.move(5).begin()
	elif status.qi1() / status.qi2() < me.recover_factor:
		world.send("exert recover")
	elif status.shen1() / status.shen2() < me.regenerate_factor:
		world.send("exert regenerate")
	elif me.pfm:
		world.send(me.pfm + " " + _killer_id)
	world.doafter(0.5,"hp\nimbue combat")

@trigger('^�����һ�������������ǽ���������|^��ֻ�����˿�һ������|^���������������ӿ��|^���ֻ����һ���Һ����ѱ��������|^�㾪��ʧ�룬��æ���ˣ�Ȼ��û�ܱܿ���������һצץ����Ѫ����|^���ֻ���˵�һ��',name='kill_17', flags=TriggerFlags.eTriggerRegularExpression|TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME)
def kill17(*args):
	global _dispel
	_dispel = True

@trigger('(05����:look (.+))?\\n(.+)���˼�����Ѫ���ڵ��ϳ鶯�˼��¾����ˣ�\Z',name='kill_16', flags=TriggerFlags.eTriggerRegularExpression|TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME,multi_line="y",lines_to_match="2")
def kill16(*args):
	global _killer_die,_back
	if args[2][2] == _killer_name:
		_killer_die = True

		if args[2][1]:
			world.send("get putao")

		if hell.core.status.qn() > _config["max_qn"]:
			hell.core.missionDispatcher.add_temp_mission(_config["qn_mission"])

		if hell.core.status.th1() > 9000:			
			hell.core.missionDispatcher.add_temp_mission(_config["jq_mission"])	

		_back = len(hell.core.missionDispatcher.temp_configs) > 0
		world.send("open qiandai zi\nget lack card from %s corpse\nget silver from %s corpse" % (_killer_id,_killer_id))
		if _back:
			world.send("cut head from %s corpse\nget head" % (_killer_id))


@trigger('��Ҫ�����������ʲô��Ʒ��',name='kill_15', flags=TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME)
def kill15(*args):
	global step	
	step = "kill_end"
	world.send("i\nhp\nc")



gifts = {
	u"�����ɵ�":"xiandan",
	u"������":"shenli wan ",
	u"����ɵ�":"huohong xiandan",
	u"ϴ�赤":"xisui dan",
	u"����ʯ":"magic stone",
	u"�ڽ�˿":"black silk",
	u"��������":"ice steel",
	u"����˿":"white silk",
	u"���":"jin kuai",
	u"������":"puti zi",
	u"������¶":"magic water",
	u"��ת��":"jiuzhuan jindan",
	u"��觲�Ƭ":"chipped agate",
	u"ˮ����Ƭ":"chipped crystal",
	u"��ʯ����":"chipped diamond"
}

@trigger(u'^������һ(.+)��',name='kill_18', flags=TriggerFlags.eTriggerRegularExpression|TriggerFlags.eKeepEvaluating|TriggerFlags.eReplace|TriggerFlags.eTemporary, group=NAME)
def kill18(*args):
	name = args[2][0][1:]
	print name
	world.send("baocun " + gifts[name])


@async()
def jiqu_wait(sec):
	world.send("jiqu")
	yield TimerTask(0,0,sec)
	world.send("halt")



@timer(2,0,0, name ="kill_19",flags= TimerFlags.eTemporary | TimerFlags.eReplace,group=NAME)
def repaire(*args):
	global _repair
	_repair = True
