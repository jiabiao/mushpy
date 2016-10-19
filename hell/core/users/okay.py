# coding=gbk

from User import User

okay = User('okay',u'叮叮当',u'okay║lxl230035@║okqNAeZnfragclx2e8ZVVmogeI║jiabiao@outlook.com')
okay.pfm = "perform cuff.jingang\nperform unarmed.zui\nperform yi"
okay.preper_kill = "exert shield\nexert powerup"

cook ={
	"name":"cook",
	"room":"hangzhou/cook",
	"max_qn": 20000,
	# "qn_mission" : "zhuxi",
	# "qn_mission_config":{}

	# "qn_mission" : "yanjiu",
	# "qn_mission_config":{"room":"wanjiegu/wlhoushan"}

	"qn_mission" : "master",
	"qn_mission_config":{"room":"shaolin/damodong"}
}


yanjiu ={
	"name":"yanjiu",
	"room":"emei/jinding",
	#"skills":["force","sword","dodge","jiuyang-shengong"]
	#"skills":[["parry",None],"force","sword","dodge","jiuyang-shengong"]	
	"skills":["force","jiuyang-shengong","sword","dodge","parry","blade","whip","throwing","never-defeated"]
}

master = {
	"name" : "master",
	"master":"dugu",
	"room" : "huashan/shandong",
	#"skills":["buddhism"]	
	#"skills":["sanscrit"]
	"skills":["throwing","never-defeated"]
	#"skills":["jingang-buhuaiti"]	
}






lian ={
	"name":"lian",
	"room":"emei/jinding",
	 "skills":{
		'yingzhua-gong': ["parry",None], 
		'nianhua-zhi':  ["parry",None], 
		'yipai-liangsan': ["strike",None],  
		'shenxing-baibian':  ["dodge",None], 
		'zui-quan':  ["parry",None], 
		'shenzhang-bada':  ["parry",None], 		
		'sanhua-zhang':  ["parry",None], 
		'fengyun-shou':  ["parry",None], 
		'banruo-zhang':  ["parry",None], 
		'jingang-quan':  ["parry",None], 
		#'qiankun-danuoyi':  ["parry",None], 
		'jinshe-zhang':  ["parry",None], 
		'jingang-zhi':  ["parry",None], 
		'qianye-shou':  ["parry",None], 
		#'jingang-buhuaiti': ["parry",None], 		
		'ningxue-shenzhao':  ["parry",None], 
		'longzhua-gong':  ["parry",None], 
		'shaolin-shenfa':  ["dodge",None], 
		'yizhi-chan': ["parry",None],
		'wuxiang-zhi': ["parry",None],
		'six-finger':  ["parry",None], 
		'luohan-quan':  ["parry",None], 
		'jinshe-jian':  ["parry","sword"], 
		'shenghuo-ling':  ["parry","sword"], 
		'fumo-jian': ["parry","sword"], 
		'lonely-sword':  ["parry","sword"], 
		'damo-jian': ["parry","sword"],
		'xiuluo-dao': ["parry","blade"], 
		'cibei-dao':  ["parry","blade"], 
		'wuhu-duanmendao':  ["parry","blade"], 
		'qiufeng-chenfa':  ["parry","whip"], 
		'riyue-bian':  ["parry","whip"], 

	}
}

jiqu = {
	"name" : "jiqu",
	"room":"shaolin/fzlou2"
}
kill ={
	"name":"kill",
	"quest_room" : "shaolin/fzlou2",
	"quest_master" : "xuanci",
	"repairs" : ["willow"],
	"max_qn": 18000,
	"jifa_cmd":"jifa force jiuyang-shengong\njifa sword lonely-sword\njifa parry jingang-buhuaiti\njifa dodge shenxing-baibian\nsummon willow\nwield willow",
	"lian_cmd":"jifa sword damo-jian\nlian sword 100\njifa sword lonely-sword",
	"qn_mission" : yanjiu,
	"jq_mission" : jiqu
}


okay.mission = None
