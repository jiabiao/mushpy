# coding=gbk


from mushpy import TimerTask,MatchTask,TriggerFlags,ValueTask,async
from sys import world

from d import city,Room
from manager import *

current = None

@async("get_current")
def get_current():

	world.send("grant\nl")
	args = yield MatchTask(u'^只有管理员才能使用授权命令。\\n02(.+)\\n04.+\\n03(.+)\Z',group='core',multi_line="y",lines_to_match="4")
	name = args[2][0]
	rooms = Room.group_by_name.get(name)
	if rooms == None:
		print "** find room group by current name failed:" + name	
		yield ValueTask(None)
		return
	if len(rooms) == 1:
		yield ValueTask(rooms[0])
		return
	if name == u"石阶":
		world.send("l")
		matches = yield MatchTask(u"04【石阶】 (松树与松树似乎都挤在一块生长|眼前遽然出现一大片松林|长长的石阶往上依然看不到尽头|一挂巨大的瀑布白龙出霄般横越山间|这里是瀑布上方一道窄窄的山梁)?")
		desc = matches[2][0]


		if desc == u"长长的石阶往上依然看不到尽头":
			yield ValueTask(get_room("shaolin/shijie2"))
			return

		if desc == u"一挂巨大的瀑布白龙出霄般横越山间":
			yield ValueTask(get_room("shaolin/shijie5"))
			return
		if desc == u"这里是瀑布上方一道窄窄的山梁":
			yield ValueTask(get_room("shaolin/shijie6"))
			return

		if desc == u"眼前遽然出现一大片松林":
			yield ValueTask(get_room("shaolin/shijie9"))
			return

		if desc == u"松树与松树似乎都挤在一块生长":
			yield ValueTask(get_room("shaolin/shijie10"))
			return

	c_exits = dict(exit.split(":") for exit in args[2][1].split("$zj#")) 
	
	match_room = rooms[0]
	max_match_exit_count = 0

	for r in rooms:		
		allMatch = True
		match_count = 0
		for e in r.exits:
			if e.direction not in c_exits:
				allMatch = False				
				break
			if e.room == None:
				continue
			if e.room.name != c_exits[e.direction]:
				allMatch = False				
				break
			match_count = match_count + 1

		if allMatch and r is current:
			yield ValueTask(current)
			return

		if allMatch and match_count >= max_match_exit_count:
			if max_match_exit_count > 0:
				print "** find more than 1 room by exits name:" + name + "exits:" + args[2][1]
			max_match_exit_count = match_count
			match_room = r
	yield ValueTask(match_room)

	


@async("run_room")
def runto(room):
	success = False
	try:
		origin = yield get_current()	
		exits = get_exits_to_terminus(origin,room) 
		if exits != None:
			yield run_exits(exits)	
		else:	
			exits = get_exits_to_outdoor(origin)
			yield run_exits(exits)	
			exits = get_exits_root_to(room)
			yield run_exits(exits)	
		success = room is current
	except Exception, e:
		print e
		success =  False

	if not success:
		print "runto failed: terminus：%s, origin:%s , current:%s" % (room.id, origin and origin.id, current and current.id)
	yield ValueTask(success)

@async("move_room")
def move(step):
	origin = yield get_current()
	exits = get_exits_move(origin,step) 
	yield run_exits(exits)


@async("run_near")
def run_near(terminuses, max_steps = 40 ):
	origin = yield get_current()
	room,exits = get_exits_to_near_terminus(origin,terminuses,max_steps) 
	print "near room:" + str(room and room.id)
	if room != None:
		yield run_exits(exits)
		yield ValueTask(room)
	else:
		yield ValueTask(None)



@async("run_exits")
def run_exits(exits):
	global current
	exits = list(exits)
	queue = []
	for exit in exits:
		if exit.cmdTask:
			flush_queue(queue)			
			yield exit.cmdTask(*exit.cmdTaskArgs)
		else:
			queue.append(exit.cmd or exit.direction)
			if len(queue) == 10:
				flush_queue(queue)
				yield  TimerTask(0,0,1.4)			
	flush_queue(queue)
	if len(exits) > 0:
		current = exits[-1].room




def flush_queue(queue):
	if queue and len(queue):
		cmds = "\n".join(queue)
		world.send(cmds)
		del queue[:]
		

