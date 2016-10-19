# coding=gbk




from User import User



khua = User('khua',u'当当当',u'khua║lxl230035@║khctQ.ef1ZGTUlx2e8ZVVmogeI║jiabiao@outlook.com')
khua.preper_kill = "exert shield\nexert powerup\nspecial agile\nspecial hatred\nspecial power"
khua.pfm = "perform you twice"

cook ={
	"name":"cook",
	"room":"city/cook",
	"max_qn": 10000,
	#"qn_mission" : "master",
	#"qn_mission_config":{"room":"gumu/zhengting"}
	#"qn_mission_config":{"room":"quanzhen/jiaobei"}
	
	 "qn_mission" : "zhuxi",
	 "qn_mission_config":{}
}


master = {
	"name" : "master",
	"master":"kuihua taijian",
	"room" : "beijing/shanlu3",
	#"skills":["zuoyou-hubo"]
	"skills":["kuihua-mogong"] #
}

yanjiu ={
	"name":"yanjiu",
	"room":"city/home1ww",
	"skills":["surge-force","force","unarmed","parry","sword","dodge","kuihua-mogong"] #,"sad-strike"
}


shu = {
	"name":"shu",
	"room":"wanjiegu/wlhoushan"
}

lian ={
	"name":"lian",
	"room":"city/home1e",
	 "skills":{
		#'huanyin-zhi': ["parry",None],


		'shenxing-baibian': ["dodge",None],
		#'bianfu-bu': ["dodge",None],
		'yunv-shenfa': ["dodge",None],
		'kongming-quan': ["unarmed",None],
		'meinv-quan': ["unarmed",None],
		#'sad-strike': ["unarmed",None],
		#'sougu': ["parry",None],
		
		
		'shenghuo-ling': ["sword","sword"],
		'xuantie-jian': ["sword","sword"],
		'sanfen-jianshu': ["sword","sword"],		
		#'zhuihun-jian': ["sword","sword"],
		'quanzhen-jian': ["sword","sword"],
		#'yunv-jian': ["parry","sword"],	
	}
}



jiqu = {
	"name" : "jiqu",
	"room":"city/home1ww"
}

kill ={
	"name":"kill",
	"quest_room" : "gumu/zhengting",
	"quest_master" : "long nv",
	#"repairs" : ["yushe"],
	"repairs" : ["zhi"],
	"jifa_cmd":"jifa force surge-force\njifa parry kongming-quan\njifa unarmed kuihua-mogong\nbei unarmed\njifa dodge shenxing-baibian",
	"lian_cmd":"lian claw 30",
	"max_qn": 18000,
	"force" : None,
	"qn_mission" : yanjiu,
	"jq_mission" : jiqu
}



khua.mission = kill


arm = ["hei","bai","yushe","caoxie","yaodai","huwan"]