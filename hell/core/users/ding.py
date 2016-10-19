# coding=gbk


from User import User

ding = User('ding',u'叮叮叮',u'ding║lxl230035║diqM05G8A2UlQlx2e8ZVVmogeI║jiabiao@outlook.com')

# born ={
# 	"name":"born",
# 	"sex_name":u"女性║║叮叮叮",
# 	"character":"s",
# 	"point":"13 30 13 24",
# 	"born":u"巴蜀人氏",
# 	"qn_mission" : "zhuxi",
# 	"special":[u"鬼话连篇", u"鸿运当头" , u"小周天运转", u"驻颜"],
# 	"require_count":2,
# 	"require_special":u"鸿运当头"
# }

cook ={
	"name":"cook",
	"room":"city3/chufang",
	"max_qn": 8000,
	# "qn_mission" : "master",
	# "qn_mission_config":{"room":"gumu/zhengting"}
	
	"qn_mission" : "zhuxi",
	"qn_mission_config":{}
}

shu = {
	"name":"shu",
	"room":"wanjiegu/wlhoushan"
}

tie ={
	"name":"tie"
}

ding.mission = cook
