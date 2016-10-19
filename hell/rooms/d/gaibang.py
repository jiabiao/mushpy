# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'gaibang/undertre', False),
	Exit('north', 'gaibang/bjandao2', False),
]
bjandao1=Room('gaibang/bjandao1', u'暗道', None, 0, exits)

exits = [
	Exit('south', 'gaibang/bjandao1', False),
	Exit('north', 'gaibang/underbj', False),
]
bjandao2=Room('gaibang/bjandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/cdandao2', False),
	Exit('northeast', 'gaibang/undertre', False),
]
cdandao1=Room('gaibang/cdandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/undercd', False),
	Exit('northeast', 'gaibang/cdandao1', False),
]
cdandao2=Room('gaibang/cdandao2', u'暗道', None, 0, exits)

exits = [
	Exit('west', 'gaibang/mishi', False),
	Exit('up', 'gaibang/undertre', False),
]
chuchang=Room('gaibang/chuchang', u'储藏室', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/dlandao2', False),
	Exit('northeast', 'gaibang/undertre', False),
]
dlandao1=Room('gaibang/dlandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/underdl', False),
	Exit('northeast', 'gaibang/dlandao1', False),
]
dlandao2=Room('gaibang/dlandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/fsandao2', False),
	Exit('northeast', 'gaibang/undertre', False),
]
fsandao1=Room('gaibang/fsandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/underfs', False),
	Exit('northeast', 'gaibang/fsandao1', False),
]
fsandao2=Room('gaibang/fsandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/fzandao2', False),
	Exit('northwest', 'gaibang/undertre', False),
]
fzandao1=Room('gaibang/fzandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/underfz', False),
	Exit('northwest', 'gaibang/fzandao1', False),
]
fzandao2=Room('gaibang/fzandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/undertre', False),
	Exit('northeast', 'gaibang/gwandao2', False),
]
gwandao1=Room('gaibang/gwandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/gwandao1', False),
	Exit('northeast', 'gaibang/undergw', False),
]
gwandao2=Room('gaibang/gwandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/undertre', False),
	Exit('northwest', 'gaibang/hsandao2', False),
]
hsandao1=Room('gaibang/hsandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/hsandao1', False),
	Exit('northwest', 'gaibang/underhs', False),
]
hsandao2=Room('gaibang/hsandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/hzandao2', False),
	Exit('northwest', 'gaibang/undertre', False),
]
hzandao1=Room('gaibang/hzandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/underhz', False),
	Exit('northwest', 'gaibang/hzandao1', False),
]
hzandao2=Room('gaibang/hzandao2', u'暗道', None, 0, exits)

exits = [
	Exit('out', 'ity/guangchang', False),
]
inhole=Room('gaibang/inhole', u'树洞内部', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/undertre', False),
	Exit('northwest', 'gaibang/lzandao2', False),
]
lzandao1=Room('gaibang/lzandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/lzandao1', False),
	Exit('northwest', 'gaibang/underlz', False),
]
lzandao2=Room('gaibang/lzandao2', u'暗道', None, 0, exits)

exits = [
	Exit('east', 'gaibang/chuchang', False),
]
mishi=Room('gaibang/mishi', u'密室', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/qzandao2', False),
	Exit('northwest', 'gaibang/undertre', False),
]
qzandao1=Room('gaibang/qzandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/underqz', False),
	Exit('northwest', 'gaibang/qzandao1', False),
]
qzandao2=Room('gaibang/qzandao2', u'暗道', None, 0, exits)

exits = [
	Exit('west', 'city/pomiao', False),
]
sheyuan=Room('gaibang/sheyuan', u'蛇园', 'city', 0, exits)

exits = [
	Exit('east', 'city/pomiao', False),
]
shoushe=Room('gaibang/shoushe', u'兽舍', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/undertre', False),
	Exit('northeast', 'gaibang/slandao2', False),
]
slandao1=Room('gaibang/slandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/slandao1', False),
	Exit('northeast', 'gaibang/undersl', False),
]
slandao2=Room('gaibang/slandao2', u'暗道', None, 0, exits)

exits = [
	Exit('out', 'beijing/caroad_e1', False),
	Exit('south', 'gaibang/bjandao2', False),
]
underbj=Room('gaibang/underbj', u'街边狗洞', None, 0, exits)

exits = [
	Exit('out', 'city3/wuhouci', False),
	Exit('northeast', 'gaibang/cdandao2', False),
]
undercd=Room('gaibang/undercd', u'武侯祠下', None, 0, exits)

exits = [
	Exit('out', 'dali/dahejieeast', False),
	Exit('northeast', 'gaibang/dlandao2', False),
]
underdl=Room('gaibang/underdl', u'大和街边', None, 0, exits)

exits = [
	Exit('out', 'foshan/beidimiao', False),
	Exit('northeast', 'gaibang/fsandao2', False),
]
underfs=Room('gaibang/underfs', u'北帝庙下', None, 0, exits)

exits = [
	Exit('out', 'fuzhou/nanmendou', False),
	Exit('northwest', 'gaibang/fzandao2', False),
]
underfz=Room('gaibang/underfz', u'大榕树下', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/zlandao2', False),
	Exit('up', 'city/pomiao', False),
]
undergb=Room('gaibang/undergb', u'破庙密室', None, 0, exits)

exits = [
	Exit('out', 'guanwai/tuwu', False),
	Exit('southwest', 'gaibang/gwandao2', False),
]
undergw=Room('gaibang/undergw', u'小土屋下', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/hsandao2', False),
	Exit('out', 'huashan/sheshen', False),
]
underhs=Room('gaibang/underhs', u'舍身崖下', None, 0, exits)

exits = [
	Exit('out', 'hangzhou/xilingqiao', False),
	Exit('northwest', 'gaibang/hzandao2', False),
]
underhz=Room('gaibang/underhz', u'西泠桥下', None, 0, exits)

exits = [
	Exit('southeast', 'gaibang/lzandao2', False),
	Exit('out', 'lingzhou/dawu', False),
]
underlz=Room('gaibang/underlz', u'大屋下', None, 0, exits)

exits = [
	Exit('out', 'quanzhou/tieqiang', False),
	Exit('northwest', 'gaibang/qzandao2', False),
]
underqz=Room('gaibang/underqz', u'铁枪庙下', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/slandao2', False),
	Exit('up', 'shaolin/chufang2', False),
]
undersl=Room('gaibang/undersl', u'屋角边', None, 0, exits)

exits = [
	Exit('west', 'city/gbxiaowu', False),
	Exit('up', 'gaibang/inhole', False),
	Exit('down', 'gaibang/chuchang', False),
]
undertre=Room('gaibang/undertre', u'树洞下', None, 0, exits)

exits = [
	Exit('out', 'wudang/tufeiwo1', False),
	Exit('northeast', 'gaibang/wdandao2', False),
]
underwd=Room('gaibang/underwd', u'土匪窝边', None, 0, exits)

exits = [
	Exit('out', 'quanzhen/xiaomiao', False),
	Exit('northeast', 'gaibang/wgandao2', False),
]
underwg=Room('gaibang/underwg', u'土地庙下', None, 0, exits)

exits = [
	Exit('south', 'gaibang/xcandao2', False),
	Exit('up', 'village/square', False),
]
underxc=Room('gaibang/underxc', u'谷场槐树边', None, 0, exits)

exits = [
	Exit('out', 'uedao/hollow', False),
	Exit('northeast', 'gaibang/xsandao2', False),
]
underxs=Room('gaibang/underxs', u'雪坑小洞', None, 0, exits)

exits = [
	Exit('west', 'ingxiu/silk4', False),
	Exit('east', 'gaibang/xxandao2', False),
]
underxx=Room('gaibang/underxx', u'沙丘小洞', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/wdandao2', False),
	Exit('northeast', 'gaibang/undertre', False),
]
wdandao1=Room('gaibang/wdandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/underwd', False),
	Exit('northeast', 'gaibang/wdandao1', False),
]
wdandao2=Room('gaibang/wdandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/wgandao2', False),
	Exit('northeast', 'gaibang/undertre', False),
]
wgandao1=Room('gaibang/wgandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/underwg', False),
	Exit('northeast', 'gaibang/wgandao1', False),
]
wgandao2=Room('gaibang/wgandao2', u'暗道', None, 0, exits)

exits = [
	Exit('south', 'gaibang/undertre', False),
	Exit('north', 'gaibang/xcandao2', False),
]
xcandao1=Room('gaibang/xcandao1', u'暗道', None, 0, exits)

exits = [
	Exit('south', 'gaibang/xcandao1', False),
	Exit('north', 'gaibang/underxc', False),
]
xcandao2=Room('gaibang/xcandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/xsandao2', False),
	Exit('northeast', 'gaibang/undertre', False),
]
xsandao1=Room('gaibang/xsandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/underxs', False),
	Exit('northeast', 'gaibang/xsandao1', False),
]
xsandao2=Room('gaibang/xsandao2', u'暗道', None, 0, exits)

exits = [
	Exit('west', 'gaibang/xxandao2', False),
	Exit('east', 'gaibang/undertre', False),
]
xxandao1=Room('gaibang/xxandao1', u'暗道', None, 0, exits)

exits = [
	Exit('west', 'gaibang/underxx', False),
	Exit('east', 'gaibang/xxandao1', False),
]
xxandao2=Room('gaibang/xxandao2', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/undertre', False),
	Exit('northeast', 'gaibang/zlandao2', False),
]
zlandao1=Room('gaibang/zlandao1', u'暗道', None, 0, exits)

exits = [
	Exit('southwest', 'gaibang/zlandao1', False),
	Exit('northeast', 'gaibang/undergb', False),
]
zlandao2=Room('gaibang/zlandao2', u'暗道', None, 0, exits)

