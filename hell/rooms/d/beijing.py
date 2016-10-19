# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'beijing/aofu_dayuan', False),
	Exit('north', 'beijing/aofu_zoulang2', False),
]
aofu_dating=Room('beijing/aofu_dating', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/aofu_zoulang1', False),
	Exit('north', 'beijing/aofu_dating', False),
]
aofu_dayuan=Room('beijing/aofu_dayuan', u'������Ժ', None, 0, exits)

exits = [
	Exit('west', 'beijing/aofu_zoulang3', False),
	Exit('south', 'beijing/aofu_zoulang2', False),
	Exit('north', 'beijing/aofu_naofang', False),
]
aofu_houyuan=Room('beijing/aofu_houyuan', u'������Ժ', None, 0, exits)

exits = [
	Exit('south', 'beijing/di_4', False),
	Exit('north', 'beijing/aofu_zoulang1', False),
]
aofu_men=Room('beijing/aofu_men', u'��������', None, 0, exits)

exits = [
	Exit('up', 'beijing/aofu_shufang', False),
]
aofu_mishi=Room('beijing/aofu_mishi', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/aofu_houyuan', False),
]
aofu_naofang=Room('beijing/aofu_naofang', u'�����η�', None, 0, exits)

exits = [
	Exit('east', 'beijing/aofu_zoulang3', False),
]
aofu_shufang=Room('beijing/aofu_shufang', u'�����鷿', None, 0, exits)

exits = [
	Exit('south', 'beijing/aofu_men', False),
	Exit('north', 'beijing/aofu_dayuan', False),
]
aofu_zoulang1=Room('beijing/aofu_zoulang1', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/aofu_dating', False),
	Exit('north', 'beijing/aofu_houyuan', False),
]
aofu_zoulang2=Room('beijing/aofu_zoulang2', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/aofu_shufang', False),
	Exit('east', 'beijing/aofu_houyuan', False),
]
aofu_zoulang3=Room('beijing/aofu_zoulang3', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/ximenkou', False),
	Exit('south', 'beijing/xi_1', False),
	Exit('north', 'beijing/bei_3', False),
	Exit('east', 'beijing/bei_2', False),
]
bei_1=Room('beijing/bei_1', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/bei_1', False),
	Exit('south', 'beijing/xi_2', False),
	Exit('north', 'beijing/bei_4', False),
	Exit('east', 'beijing/kangfu_men', False),
]
bei_2=Room('beijing/bei_2', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/caishi', False),
	Exit('south', 'beijing/bei_1', False),
	Exit('north', 'beijing/shi_1', False),
	Exit('east', 'beijing/bei_4', False),
]
bei_3=Room('beijing/bei_3', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/bei_3', False),
	Exit('south', 'beijing/bei_2', False),
	Exit('north', 'beijing/di_1', False),
]
bei_4=Room('beijing/bei_4', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/tiananmen', False),
	Exit('east', 'beijing/caroad_e1', False),
]
cagc_e=Room('beijing/cagc_e', u'�������㳡', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/tianqiao', False),
	Exit('north', 'beijing/tiananmen', False),
]
cagc_s=Room('beijing/cagc_s', u'�����ֹ㳡', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/caroad_w2', False),
	Exit('east', 'beijing/tiananmen', False),
]
cagc_w=Room('beijing/cagc_w', u'�������㳡', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/bei_3', False),
]
caishi=Room('beijing/caishi', u'���ֲ���', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/cagc_e', False),
	Exit('north', 'beijing/wang_1', False),
	Exit('east', 'beijing/caroad_e2', False),
]
caroad_e1=Room('beijing/caroad_e1', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/caroad_e1', False),
	Exit('south', 'beijing/yancao', False),
	Exit('east', 'beijing/zahuo', False),
	Exit('north', 'beijing/wang_2', False),
]
caroad_e2=Room('beijing/caroad_e2', u'��������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/kedian', False),
	Exit('south', 'beijing/yangliu1', False),
	Exit('north', 'beijing/xi_1', False),
	Exit('east', 'beijing/caroad_w2', False),
]
caroad_w1=Room('beijing/caroad_w1', u'��������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/caroad_w1', False),
	Exit('south', 'beijing/gaosheng', False),
	Exit('north', 'beijing/xi_2', False),
	Exit('east', 'beijing/cagc_w', False),
]
caroad_w2=Room('beijing/caroad_w2', u'��������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_4', False),
	Exit('east', 'beijing/chaoyang_dao2', False),
]
chaoyang_dao1=Room('beijing/chaoyang_dao1', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/chaoyang_dao1', False),
	Exit('east', 'beijing/chaoyangmen', False),
]
chaoyang_dao2=Room('beijing/chaoyang_dao2', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/chaoyang_dao2', False),
	Exit('east', 'beijing/road1', False),
]
chaoyangmen=Room('beijing/chaoyangmen', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_6', False),
]
dangpu=Room('beijing/dangpu', u'����', None, 0, exits)

exits = [
	Exit('south', 'beijing/bei_4', False),
	Exit('east', 'beijing/di_2', False),
	Exit('north', 'beijing/di_3', False),
]
di_1=Room('beijing/di_1', u'�������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_1', False),
	Exit('south', 'beijing/xichang_men', False),
	Exit('north', 'beijing/di_xigc', False),
]
di_2=Room('beijing/di_2', u'�������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/di_1', False),
	Exit('east', 'beijing/di_xigc', False),
	Exit('north', 'beijing/di_4', False),
]
di_3=Room('beijing/di_3', u'�������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/shi_3', False),
	Exit('south', 'beijing/di_3', False),
	Exit('east', 'beijing/di_5', False),
	Exit('north', 'beijing/aofu_men', False),
]
di_4=Room('beijing/di_4', u'�������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_4', False),
	Exit('south', 'beijing/di_xigc', False),
	Exit('east', 'beijing/di_dajie1', False),
	Exit('north', 'beijing/qianzhuang', False),
]
di_5=Room('beijing/di_5', u'�������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/di_dajie2', False),
]
di_anmen=Room('beijing/di_anmen', u'�ذ���', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_5', False),
	Exit('south', 'beijing/dianmen', False),
	Exit('east', 'beijing/dong_2', False),
	Exit('north', 'beijing/di_dajie2', False),
]
di_dajie1=Room('beijing/di_dajie1', u'�ذ��Ŵ��', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/di_dajie1', False),
	Exit('north', 'beijing/di_anmen', False),
]
di_dajie2=Room('beijing/di_dajie2', u'�ذ��Ŵ��', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/dianmen', False),
	Exit('south', 'beijing/dong_1', False),
	Exit('east', 'beijing/wang_9', False),
	Exit('north', 'beijing/dong_2', False),
]
di_donggc=Room('beijing/di_donggc', u'�ض��㳡', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_3', False),
	Exit('south', 'beijing/di_2', False),
	Exit('east', 'beijing/dianmen', False),
	Exit('north', 'beijing/di_5', False),
]
di_xigc=Room('beijing/di_xigc', u'�ذ������ֹ㳡', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_xigc', False),
	Exit('south', 'beijing/hgmen_n', False),
	Exit('east', 'beijing/di_donggc', False),
	Exit('north', 'beijing/di_dajie1', False),
]
dianmen=Room('beijing/dianmen', u'�ذ��Ź㳡', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/dongchang_men', False),
	Exit('east', 'beijing/wang_7', False),
	Exit('north', 'beijing/di_donggc', False),
]
dong_1=Room('beijing/dong_1', u'�ض����', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_dajie1', False),
	Exit('south', 'beijing/di_donggc', False),
	Exit('east', 'beijing/dong_3', False),
	Exit('north', 'beijing/guozijian', False),
]
dong_2=Room('beijing/dong_2', u'�ض����', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/dong_2', False),
	Exit('south', 'beijing/wang_9', False),
	Exit('north', 'beijing/wenmiao', False),
]
dong_3=Room('beijing/dong_3', u'�ض����', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/dongchang_men', False),
]
dongchang=Room('beijing/dongchang', u'����', None, 0, exits)

exits = [
	Exit('south', 'beijing/dongchang', False),
	Exit('north', 'beijing/dong_1', False),
]
dongchang_men=Room('beijing/dongchang_men', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/yong_1', False),
]
duchang=Room('beijing/duchang', u'�����ĳ�', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/mianguan', False),
	Exit('east', 'beijing/fu_2', False),
]
fu_1=Room('beijing/fu_1', u'����·', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/fu_1', False),
	Exit('south', 'beijing/hai_men', False),
	Exit('east', 'beijing/tianqiao', False),
	Exit('north', 'beijing/fukedian', False),
]
fu_2=Room('beijing/fu_2', u'����·', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/fu_2', False),
	Exit('north', 'beijing/kediandayuan', False),
]
fukedian=Room('beijing/fukedian', u'������ջ', None, 0, exits)

exits = [
	Exit('north', 'beijing/caroad_w2', False),
]
gaosheng=Room('beijing/gaosheng', u'�������', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/guandao_2', False),
	Exit('east', 'beijing/shi_2', False),
]
guandao_1=Room('beijing/guandao_1', u'��ٵ�', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/guandao_1', False),
	Exit('north', 'beijing/huangling', False),
]
guandao_2=Room('beijing/guandao_2', u'��ٵ�', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/dong_2', False),
]
guozijian=Room('beijing/guozijian', u'���Ӽ�', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/hai_houyuan', False),
	Exit('north', 'beijing/hai_dayuan', False),
]
hai_dating=Room('beijing/hai_dating', u'���ι�������', None, 0, exits)

exits = [
	Exit('west', 'beijing/hai_fang', False),
	Exit('south', 'beijing/hai_dating', False),
	Exit('east', 'beijing/hai_huating', False),
	Exit('north', 'beijing/hai_men', False),
]
hai_dayuan=Room('beijing/hai_dayuan', u'���ι�����Ժ', None, 0, exits)

exits = [
	Exit('east', 'beijing/hai_dayuan', False),
]
hai_fang=Room('beijing/hai_fang', u'�᷿', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/hai_dating', False),
]
hai_houyuan=Room('beijing/hai_houyuan', u'��Ժ', None, 0, exits)

exits = [
	Exit('west', 'beijing/hai_dayuan', False),
]
hai_huating=Room('beijing/hai_huating', u'����', None, 0, exits)

exits = [
	Exit('south', 'beijing/hai_dayuan', False),
	Exit('north', 'beijing/fu_2', False),
]
hai_men=Room('beijing/hai_men', u'���ι���', None, 0, exits)

exits = [
	Exit('west', 'beijing/road10', False),
	Exit('north', 'tulong/tulong/haian', False),
]
haigang=Room('beijing/haigang', u'����֮��', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/hg_w', False),
	Exit('south', 'beijing/hgmen_s', False),
	Exit('north', 'beijing/hgmen_n', False),
]
hg=Room('beijing/hg', u'�ʹ����', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/hg', False),
]
hg_w=Room('beijing/hg_w', u'С��', None, 0, exits)

exits = [
	Exit('south', 'beijing/hg', False),
	Exit('north', 'beijing/dianmen', False),
]
hgmen_n=Room('beijing/hgmen_n', u'�ʹ�����', None, 0, exits)

exits = [
	Exit('south', 'beijing/qiao', False),
	Exit('north', 'beijing/hg', False),
]
hgmen_s=Room('beijing/hgmen_s', u'�ʹ�����', None, 0, exits)

exits = [
	Exit('south', 'beijing/yong_2', False),
]
huadian=Room('beijing/huadian', u'�ʻ���', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/guandao_2', False),
]
huangling=Room('beijing/huangling', u'ʮ������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/xi_2', False),
	Exit('east', 'beijing/liandan_neiting', False),
]
huichuntang=Room('beijing/huichuntang', u'�ش���ҩ��', 'beijing', 0, exits)

exits = [
	Exit('up', 'beijing/huiyingup', False),
	Exit('north', 'beijing/yong_1', False),
]
huiying=Room('beijing/huiying', u'��Ӣ��¥', 'beijing', 0, exits)

exits = [
	Exit('down', 'beijing/huiying', False),
]
huiyingup=Room('beijing/huiyingup', u'��Ӣ��¥��¥', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/kangfu_zoulang1', False),
	Exit('north', 'beijing/kangfu_zoulang2', False),
]
kangfu_dating=Room('beijing/kangfu_dating', u'��������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/kangfu_men', False),
	Exit('north', 'beijing/kangfu_zoulang1', False),
]
kangfu_dayuan=Room('beijing/kangfu_dayuan', u'������Ժ', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/kangfu_zoulang2', False),
]
kangfu_dongfang=Room('beijing/kangfu_dongfang', u'���᷿', None, 0, exits)

exits = [
	Exit('west', 'beijing/bei_2', False),
	Exit('east', 'beijing/kangfu_dayuan', False),
]
kangfu_men=Room('beijing/kangfu_men', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/kangfu_zoulang2', False),
]
kangfu_shufang=Room('beijing/kangfu_shufang', u'�������鷿', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/kangfu_zoulang2', False),
]
kangfu_xifang=Room('beijing/kangfu_xifang', u'���᷿', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/kangfu_dayuan', False),
	Exit('north', 'beijing/kangfu_dating', False),
]
kangfu_zoulang1=Room('beijing/kangfu_zoulang1', u'��������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/kangfu_xifang', False),
	Exit('south', 'beijing/kangfu_dating', False),
	Exit('east', 'beijing/kangfu_dongfang', False),
	Exit('north', 'beijing/kangfu_shufang', False),
]
kangfu_zoulang2=Room('beijing/kangfu_zoulang2', u'��������', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/caroad_w1', False),
]
kedian=Room('beijing/kedian', u'�͵�', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/fukedian', False),
	Exit('east', 'beijing/kefang', False),
]
kediandayuan=Room('beijing/kediandayuan', u'�͵��Ժ', None, 0, exits)

exits = [
	Exit('west', 'beijing/kediandayuan', False),
]
kefang=Room('beijing/kefang', u'���ͷ�', None, 0, exits)

exits = [
	Exit('south', 'beijing/liandan_yaoshi', False),
]
liandan_fang=Room('beijing/liandan_fang', u'������', None, 0, exits)

exits = [
]
liandan_lin=Room('beijing/liandan_lin', u'', None, 0, exits)

exits = [
	Exit('west', 'beijing/liandan_lin4', False),
	Exit('south', 'beijing/ximenwai', False),
	Exit('east', 'beijing/liandan_lin5', False),
	Exit('north', 'beijing/liandan_lin3', False),
]
liandan_lin1=Room('beijing/liandan_lin1', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/liandan_lin6', False),
	Exit('east', 'beijing/liandan_lin7', False),
	Exit('north', 'beijing/ximenwai', False),
]
liandan_lin2=Room('beijing/liandan_lin2', u'��������', None, 0, exits)

exits = [
	Exit('south', 'beijing/liandan_lin1', False),
]
liandan_lin3=Room('beijing/liandan_lin3', u'��������', None, 0, exits)

exits = [
	Exit('east', 'beijing/liandan_lin1', False),
]
liandan_lin4=Room('beijing/liandan_lin4', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/liandan_lin1', False),
]
liandan_lin5=Room('beijing/liandan_lin5', u'��������', None, 0, exits)

exits = [
	Exit('north', 'beijing/liandan_lin2', False),
]
liandan_lin6=Room('beijing/liandan_lin6', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/liandan_lin2', False),
]
liandan_lin7=Room('beijing/liandan_lin7', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/huichuntang', False),
	Exit('north', 'beijing/liandan_yaoshi', False),
]
liandan_neiting=Room('beijing/liandan_neiting', u'�ش�������', None, 0, exits)

exits = [
	Exit('south', 'beijing/liandan_neiting', False),
	Exit('north', 'beijing/liandan_fang', False),
]
liandan_yaoshi=Room('beijing/liandan_yaoshi', u'Ҧ������', None, 0, exits)

exits = [
	Exit('east', 'beijing/niaoshi', False),
]
majiu=Room('beijing/majiu', u'���', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/fu_1', False),
]
mianguan=Room('beijing/mianguan', u'���', None, 0, exits)

exits = [
	Exit('east', 'beijing/yangliu1', False),
]
minju_y=Room('beijing/minju_y', u'�ĺ�Ժ', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/majiu', False),
	Exit('east', 'beijing/xi_1', False),
]
niaoshi=Room('beijing/niaoshi', u'����', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/di_5', False),
]
qianzhuang=Room('beijing/qianzhuang', u'����Ǯׯ', None, 0, exits)

exits = [
	Exit('south', 'beijing/tiananmen', False),
	Exit('north', 'beijing/hgmen_s', False),
]
qiao=Room('beijing/qiao', u'��ˮ��', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/qingmu_fang1', False),
]
qingmu_dating=Room('beijing/qingmu_dating', u'����', None, 0, exits)

exits = [
	Exit('west', 'beijing/qingmu_fang3', False),
	Exit('south', 'beijing/qingmu_fang2', False),
	Exit('east', 'beijing/qingmu_fang1', False),
	Exit('north', 'beijing/qingmu_men', False),
]
qingmu_dayuan=Room('beijing/qingmu_dayuan', u'��Ժ', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/qingmu_dayuan', False),
	Exit('south', 'beijing/qingmu_dating', False),
]
qingmu_fang1=Room('beijing/qingmu_fang1', u'��ľ��', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/qingmu_dayuan', False),
]
qingmu_fang2=Room('beijing/qingmu_fang2', u'��ľ��', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/qingmu_dayuan', False),
]
qingmu_fang3=Room('beijing/qingmu_fang3', u'��ľ��', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/qingmu_dayuan', False),
	Exit('north', 'beijing/yangliu3', False),
]
qingmu_men=Room('beijing/qingmu_men', u'��ľ�ô���', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/yangliu3', False),
]
qingmumen=Room('beijing/qingmumen', u'��ľ��', None, 0, exits)

exits = [
	Exit('south', 'beijing/wang_10', False),
	Exit('up', 'beijing/quanjudeup', False),
]
quanjude=Room('beijing/quanjude', u'ȫ�۵¾�¥', None, 0, exits)

exits = [
	Exit('down', 'beijing/quanjude', False),
]
quanjudeup=Room('beijing/quanjudeup', u'ȫ�۵¾�¥��¥', None, 0, exits)

exits = [
	Exit('southeast', 'beijing/road2', False),
	Exit('west', 'beijing/chaoyangmen', False),
	Exit('northeast', 'beijing/zhuang1', False),
]
road1=Room('beijing/road1', u'�����', 'beijing', 0, exits)

exits = [
	Exit('south', 'shaolin/ruzhou', False),
	Exit('north', 'beijing/road9', False),
	Exit('east', 'beijing/haigang', False),
]
road10=Room('beijing/road10', u'С��', 'beijing', 0, exits)

exits = [
	Exit('southeast', 'beijing/road3', False),
	Exit('northwest', 'beijing/road1', False),
]
road2=Room('beijing/road2', u'�����', 'beijing', 0, exits)

exits = [
	Exit('northwest', 'beijing/road2', False),
	Exit('south', 'beijing/road4', False),
	Exit('northeast', 'guanwai/laolongtou', False),
]
road3=Room('beijing/road3', u'�����', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/road7', False),
	Exit('south', 'beijing/road8', False),
	Exit('north', 'beijing/road3', False),
]
road4=Room('beijing/road4', u'�����', 'beijing', 0, exits)

exits = [
	Exit('southeast', 'beijing/road6', False),
	Exit('west', 'xueshan/bieyuan', False),
	Exit('north', 'beijing/yongdingmen', False),
]
road5=Room('beijing/road5', u'�����', 'beijing', 0, exits)

exits = [
	Exit('southeast', 'beijing/road7', False),
	Exit('northwest', 'beijing/road5', False),
	Exit('southwest', 'hengshan/jinlongxia', False),
]
road6=Room('beijing/road6', u'�����', 'beijing', 0, exits)

exits = [
	Exit('northwest', 'beijing/road6', False),
	Exit('east', 'beijing/road4', False),
]
road7=Room('beijing/road7', u'�����', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/xiaotan', False),
	Exit('south', 'beijing/road9', False),
	Exit('north', 'beijing/road4', False),
]
road8=Room('beijing/road8', u'�����', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/road10', False),
	Exit('north', 'beijing/road8', False),
]
road9=Room('beijing/road9', u'�����', 'beijing', 0, exits)

exits = [
	Exit('eastdown', 'beijing/zhuang1', False),
	Exit('northup', 'beijing/shanlu2', False),
]
shanlu1=Room('beijing/shanlu1', u'ɽ·', 'beijing', 0, exits)

exits = [
	Exit('southdown', 'beijing/shanlu1', False),
	Exit('westup', 'beijing/shanlu3', False),
]
shanlu2=Room('beijing/shanlu2', u'ɽ·', 'beijing', 0, exits)

exits = [
	Exit('eastdown', 'beijing/shanlu2', False),
]
shanlu3=Room('beijing/shanlu3', u'ɽ·', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/bei_3', False),
	Exit('north', 'beijing/shi_2', False),
]
shi_1=Room('beijing/shi_1', u'�����ϴ��', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/guandao_1', False),
	Exit('south', 'beijing/shi_1', False),
	Exit('north', 'beijing/shi_3', False),
]
shi_2=Room('beijing/shi_2', u'���ı����', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/shi_2', False),
	Exit('east', 'beijing/di_4', False),
]
shi_3=Room('beijing/shi_3', u'���ı����', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/cagc_w', False),
	Exit('south', 'beijing/cagc_s', False),
	Exit('east', 'beijing/cagc_e', False),
	Exit('north', 'beijing/qiao', False),
]
tiananmen=Room('beijing/tiananmen', u'�찲�Ź㳡', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/fu_2', False),
	Exit('south', 'beijing/tiantan_n', False),
	Exit('east', 'beijing/yong_1', False),
	Exit('north', 'beijing/cagc_s', False),
]
tianqiao=Room('beijing/tianqiao', u'������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/yongdingdao', False),
	Exit('north', 'beijing/tiantan_n', False),
]
tiantan=Room('beijing/tiantan', u'���̳', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/tiantan', False),
	Exit('north', 'beijing/tianqiao', False),
]
tiantan_n=Room('beijing/tiantan_n', u'��̳����', 'beijing', 0, exits)

exits = [
	Exit('north', 'beijing/yong_2', False),
]
tiepu=Room('beijing/tiepu', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/weifu_men', False),
	Exit('south', 'beijing/caroad_e1', False),
	Exit('east', 'beijing/wang_2', False),
	Exit('north', 'beijing/wang_3', False),
]
wang_1=Room('beijing/wang_1', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_9', False),
	Exit('south', 'beijing/wang_8', False),
	Exit('east', 'beijing/xiyuan', False),
	Exit('north', 'beijing/quanjude', False),
]
wang_10=Room('beijing/wang_10', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_1', False),
	Exit('south', 'beijing/caroad_e2', False),
	Exit('east', 'beijing/xingchang', False),
	Exit('north', 'beijing/wang_4', False),
]
wang_2=Room('beijing/wang_2', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/xiaochang', False),
	Exit('south', 'beijing/wang_1', False),
	Exit('east', 'beijing/wang_4', False),
	Exit('north', 'beijing/wang_5', False),
]
wang_3=Room('beijing/wang_3', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_3', False),
	Exit('south', 'beijing/wang_2', False),
	Exit('east', 'beijing/chaoyang_dao1', False),
	Exit('north', 'beijing/wang_6', False),
]
wang_4=Room('beijing/wang_4', u'���������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/wang_3', False),
	Exit('east', 'beijing/wang_6', False),
	Exit('north', 'beijing/wang_7', False),
]
wang_5=Room('beijing/wang_5', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_5', False),
	Exit('south', 'beijing/wang_4', False),
	Exit('east', 'beijing/dangpu', False),
	Exit('north', 'beijing/wang_8', False),
]
wang_6=Room('beijing/wang_6', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/dong_1', False),
	Exit('south', 'beijing/wang_5', False),
	Exit('east', 'beijing/wang_8', False),
	Exit('north', 'beijing/wang_9', False),
]
wang_7=Room('beijing/wang_7', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_7', False),
	Exit('south', 'beijing/wang_6', False),
	Exit('east', 'beijing/yihongyuan', False),
	Exit('north', 'beijing/wang_10', False),
]
wang_8=Room('beijing/wang_8', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/di_donggc', False),
	Exit('south', 'beijing/wang_7', False),
	Exit('east', 'beijing/wang_10', False),
	Exit('north', 'beijing/dong_3', False),
]
wang_9=Room('beijing/wang_9', u'���������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/weifu_fangw', False),
	Exit('south', 'beijing/weifu_zoulang2', False),
	Exit('east', 'beijing/weifu_fange', False),
	Exit('north', 'beijing/weifu_shufang', False),
]
weifu_dating=Room('beijing/weifu_dating', u'Τ������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/weifu_zoulang1', False),
	Exit('north', 'beijing/weifu_zoulang2', False),
]
weifu_dayuan=Room('beijing/weifu_dayuan', u'Τ����Ժ', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/weifu_dating', False),
]
weifu_fange=Room('beijing/weifu_fange', u'���᷿', None, 0, exits)

exits = [
	Exit('east', 'beijing/weifu_dating', False),
]
weifu_fangw=Room('beijing/weifu_fangw', u'���᷿', None, 0, exits)

exits = [
	Exit('west', 'beijing/weifu_zoulang1', False),
	Exit('east', 'beijing/wang_1', False),
]
weifu_men=Room('beijing/weifu_men', u'Τ������', None, 0, exits)

exits = [
	Exit('south', 'beijing/weifu_dating', False),
]
weifu_shufang=Room('beijing/weifu_shufang', u'Τ���鷿', None, 0, exits)

exits = [
	Exit('east', 'beijing/weifu_men', False),
	Exit('north', 'beijing/weifu_dayuan', False),
]
weifu_zoulang1=Room('beijing/weifu_zoulang1', u'Τ������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/weifu_dayuan', False),
	Exit('north', 'beijing/weifu_dating', False),
]
weifu_zoulang2=Room('beijing/weifu_zoulang2', u'Τ������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/dong_3', False),
]
wenmiao=Room('beijing/wenmiao', u'�ġ���', None, 0, exits)

exits = [
	Exit('west', 'beijing/niaoshi', False),
	Exit('south', 'beijing/caroad_w1', False),
	Exit('north', 'beijing/bei_1', False),
	Exit('east', 'beijing/xi_2', False),
]
xi_1=Room('beijing/xi_1', u'����', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/xi_1', False),
	Exit('south', 'beijing/caroad_w2', False),
	Exit('north', 'beijing/bei_2', False),
	Exit('east', 'beijing/huichuntang', False),
]
xi_2=Room('beijing/xi_2', u'����', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/wang_3', False),
]
xiaochang=Room('beijing/xiaochang', u'У��', None, 0, exits)

exits = [
	Exit('east', 'beijing/road8', False),
]
xiaotan=Room('beijing/xiaotan', u'С̯', None, 0, exits)

exits = [
	Exit('north', 'beijing/xichang_men', False),
]
xichang=Room('beijing/xichang', u'����', None, 0, exits)

exits = [
	Exit('south', 'beijing/xichang', False),
	Exit('north', 'beijing/di_2', False),
]
xichang_men=Room('beijing/xichang_men', u'��������', None, 0, exits)

exits = [
	Exit('west', 'beijing/ximenwai', False),
	Exit('east', 'beijing/ximenkou', False),
]
xichengmen=Room('beijing/xichengmen', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/xichengmen', False),
	Exit('east', 'beijing/bei_1', False),
]
ximenkou=Room('beijing/ximenkou', u'���ſ�', 'beijing', 0, exits)

exits = [
	Exit('west', 'heimuya/road3', False),
	Exit('south', 'beijing/liandan_lin2', False),
	Exit('north', 'beijing/liandan_lin1', False),
	Exit('east', 'beijing/xichengmen', False),
]
ximenwai=Room('beijing/ximenwai', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_2', False),
]
xingchang=Room('beijing/xingchang', u'�̳�', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_10', False),
	Exit('north', 'beijing/xiyuanup', False),
]
xiyuan=Room('beijing/xiyuan', u'����ϷԺ', None, 0, exits)

exits = [
	Exit('south', 'beijing/xiyuan', False),
]
xiyuanup=Room('beijing/xiyuanup', u'ϷԺ��̨', None, 0, exits)

exits = [
	Exit('north', 'beijing/caroad_e2', False),
]
yancao=Room('beijing/yancao', u'�̲ݵ�', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/minju_y', False),
	Exit('south', 'beijing/yangliu2', False),
	Exit('north', 'beijing/caroad_w1', False),
]
yangliu1=Room('beijing/yangliu1', u'������ͬ', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/yangliu3', False),
	Exit('north', 'beijing/yangliu1', False),
]
yangliu2=Room('beijing/yangliu2', u'������ͬ', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/qingmu_men', False),
	Exit('north', 'beijing/yangliu2', False),
]
yangliu3=Room('beijing/yangliu3', u'������ͬ', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/wang_8', False),
]
yihongyuan=Room('beijing/yihongyuan', u'����Ժ', None, 0, exits)

exits = [
	Exit('west', 'beijing/tianqiao', False),
	Exit('south', 'beijing/huiying', False),
	Exit('east', 'beijing/yong_2', False),
	Exit('north', 'beijing/duchang', False),
]
yong_1=Room('beijing/yong_1', u'���ڶ���', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/yong_1', False),
	Exit('south', 'beijing/tiepu', False),
	Exit('east', 'beijing/yong_3', False),
	Exit('north', 'beijing/huadian', False),
]
yong_2=Room('beijing/yong_2', u'���ڶ���', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/yong_2', False),
]
yong_3=Room('beijing/yong_3', u'���ڶ���', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/yongdingmen', False),
	Exit('north', 'beijing/tiantan', False),
]
yongdingdao=Room('beijing/yongdingdao', u'������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/road5', False),
	Exit('north', 'beijing/yongdingdao', False),
]
yongdingmen=Room('beijing/yongdingmen', u'������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/caroad_e2', False),
]
zahuo=Room('beijing/zahuo', u'�ӻ���', None, 0, exits)

exits = [
	Exit('southwest', 'beijing/road1', False),
	Exit('north', 'beijing/zhuang2', False),
	Exit('westup', 'beijing/shanlu1', False),
]
zhuang1=Room('beijing/zhuang1', u'С·', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/zhuang1', False),
	Exit('north', 'beijing/zhuang3', False),
]
zhuang2=Room('beijing/zhuang2', u'С·', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/zhuang2', False),
]
zhuang3=Room('beijing/zhuang3', u'ׯ������', None, 0, exits)

exits = [
	Exit('west', 'beijing/zhuang7', False),
	Exit('south', 'beijing/zhuang3', False),
	Exit('north', 'beijing/zhuang8', False),
	Exit('east', 'beijing/zhuang6', False),
]
zhuang5=Room('beijing/zhuang5', u'ׯ������', 'beijing', 0, exits)

exits = [
	Exit('west', 'beijing/zhuang5', False),
]
zhuang6=Room('beijing/zhuang6', u'ׯ������', 'beijing', 0, exits)

exits = [
	Exit('east', 'beijing/zhuang5', False),
]
zhuang7=Room('beijing/zhuang7', u'ׯ������', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/zhuang5', False),
	Exit('north', 'beijing/zhuang9', False),
]
zhuang8=Room('beijing/zhuang8', u'����', 'beijing', 0, exits)

exits = [
	Exit('south', 'beijing/zhuang8', False),
]
zhuang9=Room('beijing/zhuang9', u'С����', 'beijing', 0, exits)

