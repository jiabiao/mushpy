# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'xingxiu/shanjiao', False),
	Exit('west', 'xingxiu/store', False),
	Exit('northwest', 'xingxiu/saimachang', False),
	Exit('north', 'xingxiu/majiu', False),
	Exit('east', 'xingxiu/house', False),
]
beijiang=Room('xingxiu/beijiang', u'����', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/shamo4', False),
	Exit('westup', 'xingxiu/btshan1', False),
]
btshan=Room('xingxiu/btshan', u'����ɽ', None, 0, exits)

exits = [
	Exit('out', 'xingxiu/xxroad5', False),
]
cangku=Room('xingxiu/cangku', u'�����ɴ�����', 'xingxiu', 0, exits)

exits = [
	Exit('out', 'xingxiu/tianroad5', False),
]
cave=Room('xingxiu/cave', u'ɽ��', None, 0, exits)

exits = [
	Exit('west', 'xingxiu/beijiang', False),
	Exit('east', 'xingxiu/house1', False),
]
house=Room('xingxiu/house', u'������Ժ', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/house', False),
]
house1=Room('xingxiu/house1', u'�����ҿ���', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/silk1', False),
	Exit('eastup', 'xingxiu/xxroad3', False),
]
jiayuguan=Room('xingxiu/jiayuguan', u'������', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shanjiao', False),
	Exit('up', 'xingxiu/kedian2', False),
]
kedian=Room('xingxiu/kedian', u'�͵�', None, 0, exits)

exits = [
	Exit('enter', 'xingxiu/kedian3', False),
	Exit('down', 'xingxiu/kedian', False),
]
kedian2=Room('xingxiu/kedian2', u'�͵��¥', None, 0, exits)

exits = [
	Exit('out', 'xingxiu/kedian2', False),
]
kedian3=Room('xingxiu/kedian3', u'�͵��¥', None, 0, exits)

exits = [
	Exit('southwest', 'xingxiu/nanjiang3', False),
	Exit('northeast', 'xingxiu/shanjiao', False),
]
luzhou=Room('xingxiu/luzhou', u'ɳĮ����', 'xiyu', 0, exits)

exits = [
	Exit('south', 'xingxiu/beijiang', False),
]
majiu=Room('xingxiu/majiu', u'���', 'xingxiu', 0, exits)

exits = [
	Exit('north', 'xingxiu/yueerquan', False),
]
mogaoku=Room('xingxiu/mogaoku', u'Ī�߿�', None, 0, exits)

exits = [
	Exit('northwest', 'xingxiu/nanjiang1', False),
	Exit('northeast', 'xingxiu/shanjiao', False),
]
nanjiang=Room('xingxiu/nanjiang', u'�Ͻ�ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/nanjiang2', False),
	Exit('northeast', 'xingxiu/nanjiang', False),
]
nanjiang1=Room('xingxiu/nanjiang1', u'�Ͻ�ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/nanjiang3', False),
	Exit('northeast', 'xingxiu/nanjiang', False),
]
nanjiang2=Room('xingxiu/nanjiang2', u'�Ͻ�ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('northwest', 'xingxiu/luzhou', False)
]
nanjiang3=Room('xingxiu/nanjiang3', u'�Ͻ�ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('south', 'xingxiu/xxh2', False),
]
riyuedong=Room('xingxiu/riyuedong', u'���¶�', 'xingxiu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/beijiang', False),
]
saimachang=Room('xingxiu/saimachang', u'����', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo=Room('xingxiu/shamo', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo1=Room('xingxiu/shamo1', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo10=Room('xingxiu/shamo10', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo2=Room('xingxiu/shamo2', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo3=Room('xingxiu/shamo3', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo4=Room('xingxiu/shamo4', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo5=Room('xingxiu/shamo5', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo6=Room('xingxiu/shamo6', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo7=Room('xingxiu/shamo7', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo8=Room('xingxiu/shamo8', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo', False),
	Exit('south', 'xingxiu/shamo', False),
	Exit('north', 'xingxiu/shamo', False),
	Exit('east', 'xingxiu/shamo', False),
]
shamo9=Room('xingxiu/shamo9', u'��ɳĮ', 'xiyu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/silk4', False),
	Exit('southwest', 'xingxiu/nanjiang', False),
	Exit('north', 'xingxiu/beijiang', False),
	Exit('east', 'xingxiu/kedian', False),
	Exit('westup', 'xingxiu/tianroad1', False),
]
shanjiao=Room('xingxiu/shanjiao', u'��ɽ����', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/yueerquan', False),
	Exit('northeast', 'xingxiu/silk3', False),
]
shashan=Room('xingxiu/shashan', u'��ɳɽ', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/silk2', False),
	Exit('east', 'xingxiu/jiayuguan', False),
]
silk1=Room('xingxiu/silk1', u'˿��֮·', 'xiyu', 0, exits)

exits = [
	Exit('west', 'mingjiao/westroad1', False),
	Exit('northwest', 'xingxiu/silk3', False),
	Exit('east', 'xingxiu/silk1', False),
]
silk2=Room('xingxiu/silk2', u'˿��֮·', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/silk4', False),
	Exit('southeast', 'xingxiu/silk2', False),
]
silk3=Room('xingxiu/silk3', u'˿��֮·', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xingxiu/shamo1', False),
	Exit('northwest', 'xingxiu/shanjiao', False),
	Exit('southwest', 'xueshan/caoyuan', False),
	Exit('east', 'xingxiu/silk3', False),
]
silk4=Room('xingxiu/silk4', u'˿��֮·', 'xiyu', 0, exits)

exits = [
	Exit('east', 'xingxiu/beijiang', False),
]
store=Room('xingxiu/store', u'�ӻ���', None, 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/shanjiao', False),
	Exit('north', 'xingxiu/tianroad2', False),
]
tianroad1=Room('xingxiu/tianroad1', u'��ɽɽ·', None, 0, exits)

exits = [
	Exit('northwest', 'lingjiu/shanjiao', False),
	Exit('south', 'xingxiu/tianroad1', False),
	Exit('northeast', 'xingxiu/xxh1', False),
]
tianroad2=Room('xingxiu/tianroad2', u'��ɽɽ·', 'xingxiu', 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/xxh1', False),
	Exit('northup', 'xingxiu/xxroad4', False),
]
tianroad3=Room('xingxiu/tianroad3', u'��ɽɽ·', 'xingxiu', 0, exits)

exits = [
	Exit('westup', 'xingxiu/tianroad5', False),
]
tianroad4=Room('xingxiu/tianroad4', u'��ɽɽ·', 'xingxiu', 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/tianroad4', False),
	Exit('enter', 'xingxiu/cave', False),
	Exit('westup', 'xingxiu/tianroad6', False),
]
tianroad5=Room('xingxiu/tianroad5', u'��ɽɽ·', 'xingxiu', 0, exits)

exits = [
	Exit('eastdown', 'xingxiu/tianroad5', False),
]
tianroad6=Room('xingxiu/tianroad6', u'��ɽ����', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/wuchang3', False),
	Exit('east', 'xingxiu/xxroad6', False),
]
wuchang2=Room('xingxiu/wuchang2', u'ɽ��ƽ��', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/wuchang2', False),
]
wuchang3=Room('xingxiu/wuchang3', u'ɽ��ƽ��', 'xingxiu', 0, exits)

exits = [
	Exit('out', 'xingxiu/xxh6', False),
]
xiaoyao=Room('xingxiu/xiaoyao', u'��ң��', None, 0, exits)

exits = [
	Exit('southup', 'xingxiu/tianroad2', False),
	Exit('north', 'xingxiu/xxh2', False),
	Exit('westup', 'xingxiu/tianroad3', False),
]
xxh1=Room('xingxiu/xxh1', u'���޺�', 'xingxiu', 0, exits)

exits = [
	Exit('northwest', 'xingxiu/xxh4', False),
	Exit('south', 'xingxiu/xxh1', False),
	Exit('northeast', 'xingxiu/xxh3', False),
	Exit('north', 'xingxiu/riyuedong', False),
]
xxh2=Room('xingxiu/xxh2', u'���޺�', 'xingxiu', 0, exits)

exits = [
	Exit('northwest', 'xingxiu/xxh5', False),
	Exit('southwest', 'xingxiu/xxh2', False),
]
xxh3=Room('xingxiu/xxh3', u'���޺�', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/xxh6', False),
	Exit('southeast', 'xingxiu/xxh2', False),
	Exit('northeast', 'xingxiu/xxh5', False),
]
xxh4=Room('xingxiu/xxh4', u'���޺�', 'xingxiu', 0, exits)

exits = [
	Exit('southeast', 'xingxiu/xxh3', False),
	Exit('southwest', 'xingxiu/xxh4', False),
]
xxh5=Room('xingxiu/xxh5', u'���޺�', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/xxh4', False),
	Exit('enter', 'xingxiu/xiaoyao', False),
]
xxh6=Room('xingxiu/xxh6', u'ʯ��', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/xxroad2', False),
	Exit('east', 'changan/xi_chengmen', False),
]
xxroad1=Room('xingxiu/xxroad1', u'���', 'xingxiu', 0, exits)

exits = [
	Exit('northup', 'xingxiu/xxroad3', False),
	Exit('east', 'xingxiu/xxroad1', False),
]
xxroad2=Room('xingxiu/xxroad2', u'���', 'xingxiu', 0, exits)

exits = [
	Exit('southdown', 'xingxiu/xxroad2', False),
	Exit('westdown', 'xingxiu/jiayuguan', False),
]
xxroad3=Room('xingxiu/xxroad3', u'����ɽ', 'xingxiu', 0, exits)

exits = [
	Exit('southdown', 'xingxiu/tianroad3', False),
	Exit('north', 'xingxiu/xxroad5', False),
]
xxroad4=Room('xingxiu/xxroad4', u'С·', 'xingxiu', 0, exits)

exits = [
	Exit('south', 'xingxiu/xxroad4', False),
	Exit('north', 'xingxiu/xxroad6', False),
	Exit('enter', 'xingxiu/cangku', False),
]
xxroad5=Room('xingxiu/xxroad5', u'С·', 'xingxiu', 0, exits)

exits = [
	Exit('west', 'xingxiu/wuchang2', False),
	Exit('south', 'xingxiu/xxroad5', False),
]
xxroad6=Room('xingxiu/xxroad6', u'ɽ��ƽ��', 'xingxiu', 0, exits)

exits = [
	Exit('east', 'xingxiu/shashan', False),
]
yueerquan=Room('xingxiu/yueerquan', u'�¶�Ȫ', None, 0, exits)

