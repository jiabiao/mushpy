# coding=gbk


from User import User

ding = User('ding',u'������',u'ding�Ulxl230035�UdiqM05G8A2UlQlx2e8ZVVmogeI�Ujiabiao@outlook.com')

# born ={
# 	"name":"born",
# 	"sex_name":u"Ů�ԨU�U������",
# 	"character":"s",
# 	"point":"13 30 13 24",
# 	"born":u"��������",
# 	"qn_mission" : "zhuxi",
# 	"special":[u"����ƪ", u"���˵�ͷ" , u"С������ת", u"פ��"],
# 	"require_count":2,
# 	"require_special":u"���˵�ͷ"
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
