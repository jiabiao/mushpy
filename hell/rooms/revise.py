# coding=gbk
from d import *
from mushpy import async,MatchTask,TimerTask
from sys import world

fly = {
	"yz"  		: "city/guangchang",
	"bj"  		: "beijing/tiananmen",
	"cd"  		: "city3/guangchang",
	"changan"  	: "changan/bridge2",
	"sz"   		: "suzhou/canlangting",
	"hz" 		: "hangzhou/road10",
	"fz"   		: "fuzhou/dongjiekou",
	"foshan"   	: "foshan/street3",
	"guiyun"  	: "guiyun/taihu",
	"hmy"  		: "heimuya/up1",
	"wugong"   	: "quanzhen/zhongxin",
	"ts"  		: "taishan/taishanjiao",
	"dl"     	: "dali/center",
	"nanyang"  	: "shaolin/nanyang",
	"qz" 		: "quanzhou/zhongxin",
	"jx"  		: "quanzhou/jiaxing",
	"xy"		: "xiangyang/guangchang",
	"yongdeng" 	: "huanghe/yongdeng",
	"lingzhou" 	: "lingzhou/center",
	"henyang"  	: "henshan/hengyang",
	"guanwai"  	: "guanwai/jishi",
	"xx"  		: "xingxiu/xxh1",
	"bt"   		: "baituo/guangchang",       
	"qzj" 		: "quanzhen/damen",
	"zhongnan" 	: "quanzhen/shanjiao",
	"gm"     	: "gumu/mumen",
	"mr"   		: "yanziwu/hupan",
	"lj"  		: "lingjiu/jian",
	"sl"  		: "shaolin/shanmen",
	"wd"   		: "wudang/jiejianyan",
	"xyg"  		: "xiaoyao/xiaodao4",	
	"hs"  		: "huashan/shaluo",
	"xs"  		: "xuedao/nroad4",
	"xd"   		: "xuedao/wangyougu",
	#"kl"   	: "kunlun/klshanlu",
	"em"     	: "emei/huayanding",
	"mj" 		: "mingjiao/shanjiao",
	"nanhai"   	: "xiakedao/haibin",
	"hujia"    	: "guanwai/xiaoyuan",
	"yzw"  		: "yanziwu/bozhou",
	"thd"   	: "taohua/tingzi",
	"hsjz"		: "huashan/pingdi",
	"moye"		: "item/xiaowu",
	"ruzhou"	: "shaolin/ruzhou"
}
#root room 
rootRoom = Room('root','root',1,1)
rootRoom.level = 0
rootRoom.time = 0


@async()
def flyto(*args):
	world.send("fly " + args[0])
	yield MatchTask("^你一路驾御白雕飞行，终于赶到了","fly_task",name = "auto_fly")


for direction,roomid in fly.iteritems():
	e = Exit(direction, roomid)
	e.time = 7
	e.cmdTask = flyto
	e.cmdTaskArgs = [direction]
	rootRoom.exits.append(e)

@async()
def flush():
	world.send("grant")
	yield MatchTask(u'^只有管理员才能使用授权命令。')

@async()
def toto(error,direction):
	while True:
		yield flush()
		world.send(direction)
		matches = yield MatchTask(error + u"|^你来到了")
		ok = matches and matches[1].startswith(u"你来到了")
		if ok:
			break
		else:
			yield TimerTask(0,0,0.3)


#fix room

def revise_for_user(name):
	if name != "khua":
		gumu.shandong.find_exit("westdown").block = True
	else:
		exit = Exit('tang','gumu/mishi2',False)
		exit.cmd = "tang coffin\nniu lock\ndrop jiuyin zhenjing3"
		gumu.houting.exits.append(exit)

		exit = Exit("south","gumu/qianting",False)
		exit.cmd = "move shi\nsouth"
		gumu.mumen.exits.append(exit)


	if name == "okay":		
		exit = Exit('north','shaolin/smdian',False)
		exit.cmd = "knock gate\nnorth"
		shaolin.guangchang1.exits.append(exit)

		exit = Exit('south','shaolin/guangchang1',False)
		exit.cmd = "open gate\nsouth"
		shaolin.smdian.exits.append(exit)


		exit = Exit("cross","shaolin/hanshui2",False)
		shaolin.hanshui1.exits.append(exit)

		exit = Exit("cross","shaolin/hanshui1",False)
		shaolin.hanshui2.exits.append(exit)


		xingxiu.xxh1.find_exit("north").block = True
		xingxiu.xxh1.find_exit("westup").block = True

gaibang.inhole.find_exit('out').room_id = 'city/guangchang'

lingzhou.gongsquare =Room('lingzhou/gongsquare', u'皇宫广场', None, 1, [
	Exit('east', 'lingzhou/dongmen', False),
	Exit('south', 'lingzhou/gonggate', False)
])
lingzhou.biangate.find_exit("west").room_id = 'lingzhou/gongsquare'

city.zuixianlou.exits.append(Exit('north', 'city/cook', False))

city.cook = Room('city/cook',u'酒楼厨房',None,True,[
	Exit('south', 'city/zuixianlou', False)
])

city.zuixianlou.exits.append(Exit('north', 'city/cook', False))
city.cook = Room('city/cook',u'酒楼厨房',None,True,[
	Exit('south', 'city/zuixianlou', False)
])


###################

city.n = Room('city/n',u'北大街','city',False,[
	Exit('north', 'city/beimen', False),
	Exit('south', 'city/beidajie2', False),
	Exit('east', 'city/ne1', False),
	Exit('west', 'city/nw1', False)
])

city.ne1 = Room('city/ne1',u'武林北街3号','city',False,[
	Exit('east', 'city/ne2', False),
	Exit('west', 'city/n', False)
])

city.ne2 = Room('city/ne2',u'武林北街2号','city',False,[
	Exit('east', 'city/ne3', False),
	Exit('west', 'city/ne1', False)
])

city.ne3 = Room('city/ne3',u'武林北街1号','city',False,[
	Exit('west', 'city/ne2', False),
	Exit('south', 'city/en2', False)	
])

city.en2 = Room('city/en2',u'武林东街','city',False,[
	Exit('north', 'city/ne3', False),
	Exit('south', 'city/en1', False)	
])

city.en1 = Room('city/en1',u'武林东街','city',False,[
	Exit('north', 'city/en2', False),
	Exit('south', 'city/e', False)	
])

city.e = Room('city/e',u'东大街','city',False,[
	Exit('west', 'city/dongdajie2', False),
	Exit('east', 'city/dongmen', False),

	Exit('north', 'city/en1', False),
	Exit('south', 'city/es1', False)	
])

city.es1 = Room('city/es1',u'武林东街','city',False,[
	Exit('north', 'city/e', False),
	Exit('south', 'city/es2', False)	
])

city.es2 = Room('city/es2',u'武林东街','city',False,[
	Exit('north', 'city/es1', False),
	Exit('south', 'city/se3', False)	
])

city.se3 = Room('city/se3',u'武林南街','city',False,[
	Exit('north', 'city/es2', False),
	Exit('west', 'city/se2', False)	
])

city.se2 = Room('city/se2',u'武林南街','city',False,[
	Exit('east', 'city/se3', False),
	Exit('west', 'city/se1', False)	
])

city.se1 = Room('city/se1',u'武林南街','city',False,[
	Exit('east', 'city/se2', False),
	Exit('west', 'city/s', False)	
])

city.s = Room('city/s',u'南大街','city',False,[
	Exit('north', 'city/nandajie2', False),
	Exit('south', 'city/nanmen', False),

	Exit('east', 'city/se1', False),
	Exit('west', 'city/sw1', False)	
])
city.sw1 = Room('city/sw1',u'武林南街','city',False,[

	Exit('east', 'city/s', False),
	Exit('west', 'city/sw2', False)	
])

city.sw2 = Room('city/sw2',u'武林南街','city',False,[

	Exit('east', 'city/sw1', False),
	Exit('west', 'city/sw3', False)	
])
city.sw3 = Room('city/sw3',u'武林南街','city',False,[

	Exit('east', 'city/sw2', False),
	Exit('north', 'city/ws2', False)	
])

city.ws2 = Room('city/ws2',u'武林西街','city',False,[
	Exit('north', 'city/ws1', False),
	Exit('south', 'city/sw3', False)	
])
city.ws1 = Room('city/ws1',u'武林西街','city',False,[
	Exit('north', 'city/w', False),
	Exit('south', 'city/ws2', False)	
])

city.w = Room('city/w',u'西大街','city',False,[
	Exit('east', 'city/xidajie2', False),
	Exit('west', 'city/ximen', False),	

	Exit('north', 'city/wn1', False),
	Exit('south', 'city/ws1', False)	
])
city.wn1 = Room('city/wn1',u'武林西街','city',False,[
	Exit('north', 'city/wn2', False),
	Exit('south', 'city/w', False)	
])
city.wn2 = Room('city/wn2',u'武林西街','city',False,[
	Exit('north', 'city/nw3', False),
	Exit('south', 'city/wn1', False)	
])
city.nw3 = Room('city/nw3',u'武林北街','city',False,[
	Exit('east', 'city/nw2', False),
	Exit('south', 'city/wn2', False)	
])

city.nw2 = Room('city/nw2',u'武林北街','city',False,[
	Exit('east', 'city/nw1', False),
	Exit('west', 'city/nw3', False),
	Exit('south', 'city/fygc', False)	
])
city.nw1 = Room('city/nw1',u'武林北街','city',False,[
	Exit('east', 'city/n', False),
	Exit('west', 'city/nw2', False)	
])

city.fygc = Room('city/fygc',u'风云广场',None,False,[
	Exit('north', 'city/nw2', False),
	Exit('south', 'city/home1', False)	
])

city.home1 = Room('city/home1',u'南云街',None,False,[
	Exit('north', 'city/fygc', False),
	Exit('west', 'city/home1w', False),
	Exit('east', 'city/home1e', False)		
])

city.home1w = Room('city/home1w',u'叮叮客栈',None,False,[
	Exit('east', 'city/home1', False),	
	Exit('west', 'city/home1ww', False)	
])

city.home1ww = Room('city/home1ww',u'叮字一号房',None,False,[
	Exit('east', 'city/home1w', False)	
])

city.home1e = Room('city/home1e',u'当当武馆',None,False,[
	Exit('west', 'city/home1', False)		
])


city.beidajie2.find_exit("north").room_id = 'city/n'
city.beimen.find_exit("south").room_id = 'city/n'

city.dongdajie2.find_exit("east").room_id = 'city/e'
city.dongmen.find_exit("west").room_id = 'city/e'

city.nandajie2.find_exit("south").room_id = 'city/s'
city.nanmen.find_exit("north").room_id = 'city/s'

city.xidajie2.find_exit("west").room_id = 'city/w'
city.ximen.find_exit("east").room_id = 'city/w'


city.heishi = Room('city/heishi',u'黑市','city',False,[
	Exit('northwest', 'city/guangchang', False)		
])

city.guangchang.exits.append(Exit('southeast','city/heishi',False))
###################



hangzhou.jiulou.exits.append(Exit('north','hangzhou/cook',False))
hangzhou.cook = Room('hangzhou/cook',u'厨房',None,True,[
	Exit('south', 'hangzhou/jiulou', False)
])

hangzhou.jiulou.exits.append(Exit('north','hangzhou/cook',False))
hangzhou.cook = Room('hangzhou/cook',u'厨房',None,True,[
	Exit('south', 'hangzhou/jiulou', False)
])

fuzhou.weizhongwei.exits.append(Exit('north','fuzhou/cook',False))
fuzhou.cook = Room('fuzhou/cook',u'厨房',None,True,[
	Exit('south', 'fuzhou/weizhongwei', False)
])



huashan.laojun.find_exit("southup").block = True


city.caizhu.find_exit("north").block = True
city.bingyin.find_exit("south").block = True
city.bingyindamen.find_exit("south").block = True
city.dangpu.find_exit("down").block = True
city.kedian.find_exit("up").block = True
city.kedian.find_exit("south").block = True
city.yamen.find_exit("north").block = True

city3.kedian.find_exit("up").block = True

city3.tidugate.find_exit("north").block = True
city3.wuguan.find_exit("up").block = True
city3.wuguan.find_exit("down").block = True
city3.northroad2.find_exit("south").block = True
dali.kedian.find_exit("up").block = True



fuzhou.rongcheng.find_exit("up").block = True
fuzhou.xiangyang.find_exit("west").block = True
fuzhou.yamen.find_exit("east").block = True

hangzhou.kedian.find_exit("up").block = True
hangzhou.liuhe1.find_exit("up").block = True
xiangyang.jiangjungate.find_exit("north").block = True

xueshan.shanmen.find_exit("north").block = True


for xsroom in [xueshan.hubian1,xueshan.shenghu,xueshan.tulu3]:
	for e in xsroom.exits:
		e.cmdTask = toto
		e.time = 2
		e.cmdTaskArgs = [u"^你突然发现眼前的景象有些迷乱。$",e.direction]


changan.kezhan.find_exit("up").block = True

lingzhou.chema.find_exit("up").block = True
xingxiu.kedian.find_exit("up").block = True
xuedao.shandong2.find_exit("west").block = True
xuedao.sroad8.find_exit("enter").block = True
xuedao.sroad9.find_exit("east").block = True
guanwai.kedian.find_exit("up").block = True
guanwai.xiaoyuan.find_exit("north").block = True
guanwai.xiaoyuan.back_exit = guanwai.xiaoyuan.find_exit("south")

xingxiu.shanjiao.find_exit("southwest").block = True
xingxiu.silk4.find_exit("west").block = True
xingxiu.house.find_exit("east").block = True

baituo.gebi.find_exit("east").block = True
shaolin.kedian1.find_exit("up").block = True
shaolin.qfdian.find_exit("north").cmd = "open door\nnorth"
shaolin.damodong.back_exit = shaolin.damodong.find_exit("out")



huashan.shanhongpb.exits.append(Exit('cross', 'huashan/shandong', False))



mingjiao.gebitan1.outdoor = False
mingjiao.gebitan2.outdoor = False
mingjiao.gebitan3.outdoor = False
mingjiao.gebitan4.outdoor = False
mingjiao.gebitan5.outdoor = False
mingjiao.gebitan3.find_exit("north").block = True
mingjiao.gebitan4.find_exit("south").block = True