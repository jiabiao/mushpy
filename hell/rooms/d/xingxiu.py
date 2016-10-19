# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'xingxiu/shanjiao', False),
	Exit('west', 'xingxiu/store', False),
	Exit('northwest', 'xingxiu/saimachang', False),
	Exit('north', 'xingxiu/majiu', False),
	Exit('east', 'xingxiu/house', False),
]
beijiang=Room('xingxiu/beijiang', u'伊犁', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/shamo4', False),
	Exit('westup', 'xingxiu/btshan1', False),
]
btshan=Room('xingxiu/btshan', u'白驼山', None, 0, exits)

exits = [
	Exit('out', 'xingxiu/xxroad5', False),
]
cangku=Room('xingxiu/cangku', u'星宿派储藏室', 'xingxiu', 0, exits)

exits = [
	Exit('out', 'xingxiu/tianroad5', False),
]
cave=Room('xingxiu/cave', u'山洞', None, 0, exits)

exits = [
	Exit('west', 'xingxiu/beijiang', False),
	Exit('east', 'xingxiu/house1', False),
]
house=Room('xingxiu/house', u'巴依家院', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/house', False),
]
house1=Room('xingxiu/house1', u'巴依家客厅', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/silk1', False),
	Exit('eastup', 'xingxiu/xxroad3', False),
]
jiayuguan=Room('xingxiu/jiayuguan', u'嘉峪关', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shanjiao', False),
	Exit('up', 'xingxiu/kedian2', False),
]
kedian=Room('xingxiu/kedian', u'客店', None, 0, exits)

exits = [
	Exit('enter', 'xingxiu/kedian3', False),
	Exit('down', 'xingxiu/kedian', False),
]
kedian2=Room('xingxiu/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('out', 'xingxiu/kedian2', False),
]
kedian3=Room('xingxiu/kedian3', u'客店二楼', None, 0, exits)

exits = [
	Exit('southwest', 'xingxiu/nanjiang3', False),
	Exit('northeast', 'xingxiu/shanjiao', False),
]
luzhou=Room('xingxiu/luzhou', u'沙漠绿洲', 'xiyu', 0, exits)

exits = [
	Exit('south', 'xingxiu/beijiang', False),
]
majiu=Room('xingxiu/majiu', u'马厩', 'xingxiu', 0, exits)

exits = [
	Exit('north', 'xingxiu/yueerquan', False),
]
mogaoku=Room('xingxiu/mogaoku', u'莫高窟', None, 0, exits)

exits = [
	Exit('northwest', 'xingxiu/nanjiang1', False),
	Exit('northeast', 'xingxiu/shanjiao', False),
]
nanjiang=Room('xingxiu/nanjiang', u'南疆沙漠', 'xiyu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/nanjiang2', False),
	Exit('northeast', 'xingxiu/nanjiang', False),
]
nanjiang1=Room('xingxiu/nanjiang1', u'南疆沙漠', 'xiyu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/nanjiang3', False),
	Exit('northeast', 'xingxiu/nanjiang', False),
]
nanjiang2=Room('xingxiu/nanjiang2', u'南疆沙漠', 'xiyu', 0, exits)

exits = [
	Exit('northwest', 'xingxiu/luzhou', False)
]
nanjiang3=Room('xingxiu/nanjiang3', u'南疆沙漠', 'xiyu', 0, exits)

exits = [
	Exit('south', 'xingxiu/xxh2', False),
]
riyuedong=Room('xingxiu/riyuedong', u'日月洞', 'xingxiu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/beijiang', False),
]
saimachang=Room('xingxiu/saimachang', u'赛马场', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo=Room('xingxiu/shamo', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo1=Room('xingxiu/shamo1', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo10=Room('xingxiu/shamo10', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo2=Room('xingxiu/shamo2', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo3=Room('xingxiu/shamo3', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo4=Room('xingxiu/shamo4', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo5=Room('xingxiu/shamo5', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo6=Room('xingxiu/shamo6', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo7=Room('xingxiu/shamo7', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo8=Room('xingxiu/shamo8', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo9=Room('xingxiu/shamo9', u'大沙漠', 'xiyu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/silk4', False),
	Exit('southwest', 'xingxiu/nanjiang', False),
	Exit('north', 'xingxiu/beijiang', False),
	Exit('east', 'xingxiu/kedian', False),
	Exit('westup', 'xingxiu/tianroad1', False),
]
shanjiao=Room('xingxiu/shanjiao', u'天山脚下', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/yueerquan', False),
	Exit('northeast', 'xingxiu/silk3', False),
]
shashan=Room('xingxiu/shashan', u'鸣沙山', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/silk2', False),
	Exit('east', 'xingxiu/jiayuguan', False),
]
silk1=Room('xingxiu/silk1', u'丝绸之路', 'xiyu', 0, exits)

exits = [
	Exit('west', 'mingjiao/westroad1', False),
	Exit('northwest', 'xingxiu/silk3', False),
	Exit('east', 'xingxiu/silk1', False),
]
silk2=Room('xingxiu/silk2', u'丝绸之路', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/silk4', False),
	Exit('southeast', 'xingxiu/silk2', False),
]
silk3=Room('xingxiu/silk3', u'丝绸之路', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo1', False),
	Exit('northwest', 'xingxiu/shanjiao', False),
	Exit('southwest', 'xueshan/caoyuan', False),
	Exit('east', 'xingxiu/silk3', False),
]
silk4=Room('xingxiu/silk4', u'丝绸之路', 'xiyu', 0, exits)

exits = [
	Exit('east', 'xingxiu/beijiang', False),
]
store=Room('xingxiu/store', u'杂货铺', None, 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/shanjiao', False),
	Exit('north', 'xingxiu/tianroad2', False),
]
tianroad1=Room('xingxiu/tianroad1', u'天山山路', None, 0, exits)

exits = [
	Exit('northwest', 'lingjiu/shanjiao', False),
	Exit('south', 'xingxiu/tianroad1', False),
	Exit('northeast', 'xingxiu/xxh1', False),
]
tianroad2=Room('xingxiu/tianroad2', u'天山山路', 'xingxiu', 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/xxh1', False),
	Exit('northup', 'xingxiu/xxroad4', False),
]
tianroad3=Room('xingxiu/tianroad3', u'天山山路', 'xingxiu', 0, exits)

exits = [
	Exit('westup', 'xingxiu/tianroad5', False),
]
tianroad4=Room('xingxiu/tianroad4', u'天山山路', 'xingxiu', 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/tianroad4', False),
	Exit('enter', 'xingxiu/cave', False),
	Exit('westup', 'xingxiu/tianroad6', False),
]
tianroad5=Room('xingxiu/tianroad5', u'天山山路', 'xingxiu', 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/tianroad5', False),
]
tianroad6=Room('xingxiu/tianroad6', u'天山顶峰', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/wuchang3', False),
	Exit('east', 'xingxiu/xxroad6', False),
]
wuchang2=Room('xingxiu/wuchang2', u'山间平地', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/wuchang2', False),
]
wuchang3=Room('xingxiu/wuchang3', u'山间平地', 'xingxiu', 0, exits)

exits = [
	Exit('out', 'xingxiu/xxh6', False),
]
xiaoyao=Room('xingxiu/xiaoyao', u'逍遥洞', None, 0, exits)

exits = [
	Exit('southup', 'xingxiu/tianroad2', False),
	Exit('north', 'xingxiu/xxh2', False),
	Exit('westup', 'xingxiu/tianroad3', False),
]
xxh1=Room('xingxiu/xxh1', u'星宿海', 'xingxiu', 0, exits)

exits = [
	Exit('northwest', 'xingxiu/xxh4', False),
	Exit('south', 'xingxiu/xxh1', False),
	Exit('northeast', 'xingxiu/xxh3', False),
	Exit('north', 'xingxiu/riyuedong', False),
]
xxh2=Room('xingxiu/xxh2', u'星宿海', 'xingxiu', 0, exits)

exits = [
	Exit('northwest', 'xingxiu/xxh5', False),
	Exit('southwest', 'xingxiu/xxh2', False),
]
xxh3=Room('xingxiu/xxh3', u'星宿海', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/xxh6', False),
	Exit('southeast', 'xingxiu/xxh2', False),
	Exit('northeast', 'xingxiu/xxh5', False),
]
xxh4=Room('xingxiu/xxh4', u'星宿海', 'xingxiu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/xxh3', False),
	Exit('southwest', 'xingxiu/xxh4', False),
]
xxh5=Room('xingxiu/xxh5', u'星宿海', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/xxh4', False),
	Exit('enter', 'xingxiu/xiaoyao', False),
]
xxh6=Room('xingxiu/xxh6', u'石道', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/xxroad2', False),
	Exit('east', 'changan/xi_chengmen', False),
]
xxroad1=Room('xingxiu/xxroad1', u'大道', 'xingxiu', 0, exits)

exits = [
	Exit('northup', 'xingxiu/xxroad3', False),
	Exit('east', 'xingxiu/xxroad1', False),
]
xxroad2=Room('xingxiu/xxroad2', u'大道', 'xingxiu', 0, exits)

exits = [
	Exit('southdown', 'xingxiu/xxroad2', False),
	Exit('westdown', 'xingxiu/jiayuguan', False),
]
xxroad3=Room('xingxiu/xxroad3', u'六盘山', 'xingxiu', 0, exits)

exits = [
	Exit('southdown', 'xingxiu/tianroad3', False),
	Exit('north', 'xingxiu/xxroad5', False),
]
xxroad4=Room('xingxiu/xxroad4', u'小路', 'xingxiu', 0, exits)

exits = [
	Exit('south', 'xingxiu/xxroad4', False),
	Exit('north', 'xingxiu/xxroad6', False),
	Exit('enter', 'xingxiu/cangku', False),
]
xxroad5=Room('xingxiu/xxroad5', u'小路', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/wuchang2', False),
	Exit('south', 'xingxiu/xxroad5', False),
]
xxroad6=Room('xingxiu/xxroad6', u'山间平地', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/shashan', False),
]
yueerquan=Room('xingxiu/yueerquan', u'月儿泉', None, 0, exits)

