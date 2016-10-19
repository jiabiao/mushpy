# coding=gbk

import d
import revise
import hell
from revise import rootRoom
from d import Room,Exit


_find_path_version = 0 #������Dijkstra��Closed���Ϲ��ܣ����Ǳ������ķ��䲻�ظ����㣬��ʹ�µ�·������Լʱ��

########## help method ##########   
def get_room(id):	
    '''
    ����id��ѯ����
    '''
    path = id.split("/")
    if path[0] in('room','tulong'):
        return None     
    area = getattr(d,path[0])
    return getattr(area,path[1])   

def get_exits_root_to(room):
    '''
    root -> room
    '''
    exits = []
    while not room is rootRoom:
        exits.append(room.come_exit)
        room = room.come_room
    return reversed(exits)

def get_exit(origin, terminus):
    '''
    ��ѯ��origin��terminus ��Exit
    '''
    for exit in origin.exits:
        if exit.room == terminus:
            return exit
    return None    

def get_back_exit(room):
    '''
    room -> root_room�ĵ�һ��Exit
    �ҿ��Է��еķ��䣺�������ŷ����ķ�����ͣBack
    '''
    if not hasattr(room,'back_exit'):
        room.back_exit = get_exit(room,room.come_room)
    return room.back_exit    


def get_exits_to_outdoor(room):
    '''
    room ->  outdoor
    �ҿ��Է��еķ���
    '''
    exits = []
    while not room.outdoor:
        back_exit = get_back_exit(room)
        if back_exit == None:
            return None
        exits.append(back_exit)
        room = room.come_room
    return exits

def get_exits_around(room,steps):
    '''
    ����room���������з��䣬��󷵻�room
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1  

    exits = []
    def around(current,back_exit,steps):        
        if steps > 0:       
            for exit in current.exits :
                next_room = exit.room
                if next_room == None or next_room.nofight or next_room.find_path_version == _find_path_version:      
                    continue
                back = get_exit(next_room, current)
                if back == None:  #���ȥ�˲��ܻ������Ͳ�Ҫȥ��
                    continue
                next_room.find_path_version = _find_path_version
                exits.append(exit)                
                around(exit.room,back,steps - 1)        
        exits.append(back_exit)
    around(room,None,steps)
    exits.pop() #Ϊ�˵ݹ���һ���жϣ����һ��������None
    return exits

def get_exits_move(origin, min_step, max_step = 15):
    '''
    �ƶ�4��
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1  

    open = {origin:[]} 

    for step in range(max_step):
        for o in open.keys():            
            path = open.pop(o) 
            if step >= min_step and o.outdoor:
                return path
            for exit in o.exits: 
                next_room = exit.room 
                if next_room == None or next_room.find_path_version == _find_path_version: 
                    continue   
                next_room.find_path_version = _find_path_version             
                open[next_room] = path + [exit]     




def get_exits_to_near_terminus(origin, terminuses , max_steps = 40): 
    '''
    origin -> terminuses������һ������
    ����Ԫ�� ����һ�� terminus, origin->terminus)
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1  #����Closed����

    open = {origin:[]} 
    print "get_exits_to_near_terminus orgin:" + origin.id
    for t in terminuses:
        print "terminus:" + t.id
    for _ in range(max_steps):
        for o in open.keys():    
   
            path = open.pop(o)            
            if o in terminuses: return o,path            
            for exit in o.exits: 
                next_room = exit.room 
                if next_room == None or next_room.find_path_version == _find_path_version: 
                    continue   
                next_room.find_path_version = _find_path_version             
                open[next_room] = path + [exit]   
    print "not found"         
    return None,[]

def get_exits_to_terminus(origin, terminus , max_steps = 40): 
    '''
    ���� origin -> terminus��Exits
    
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1  #����Closed����

    open = {origin:[]} 

    for _ in range(max_steps):
        for o in open.keys():            
            path = open.pop(o)     
            if o is terminus: return path    
            for exit in o.exits: 
                next_room = exit.room 
                if next_room == None or next_room.find_path_version == _find_path_version: 
                    continue 
                next_room.find_path_version = _find_path_version             
                open[next_room] = path + [exit]            

########## help method ##########   

########## init room ##########   
def _init_room(room):
    if room.level > 35 or room.exits == None or len(room.exits) == 0:
        return

    for exit in room.exits:
        if exit.room == None and not exit.block:
            exit.room = get_room(exit.room_id)
        e_room = exit.room;
        if e_room == None:
            continue
  
        new_time = room.time + exit.time
        new_level = room.level + 1    
        if e_room.time < new_time or (e_room.time == new_time and e_room.level <= new_level):
            continue
        e_room.time = new_time
        e_room.level = new_level
        e_room.come_room = room
        e_room.come_exit = exit
        _init_room(e_room)
 
def init(user_id):
    revise.revise_for_user(user_id)
    _init_room(rootRoom)

hell.core.login.init_room = init 
########## init room ########## 


########## start room ########## 
_place_start_rooms_id = {
    u"��ɽ����" : [ "huashan/pingxinshi", "village/square", "village/wexit"],
    u"���ݳ�"   : [ "city/beimen", "city/nanmen", "city/ximen", "city/dongmen" ],
    u"������"   : [ "changan/dong_chengmen", "changan/nan_chengmen",   "changan/xi_chengmen", "changan/bei_chengmen", "changan/qinglong2", "changan/baihu2"],
    u"�书��"   : [ "quanzhen/xijie", "quanzhen/nanjie"],
    u"��ɽһ��" : [ "foshan/street1", "foshan/southgate"],
    u"�Ϻ�һ��" : [ "xiakedao/xkroad4" ],
    u"����һ��" : [ "shaolin/ruzhou" ],
    u"��ɽһ��" : [ "songshan/tianzhongge", "shaolin/shijie1","shaolin/shijie8"],
    u"����ɽ"   : [ "quanzhen/shanlu1", "quanzhen/shijie1","quanzhen/shijie9", "quanzhen/cuipinggu",   "quanzhen/baishulin3", "gumu/taiyi1","gumu/shenheyuan", "quanzhen/banshanting"],
    u"�ɶ���"   : [ "city3/southroad1", "city3/qingyanggong","city3/northroad2"],
    u"���޺�"   : [ "xingxiu/tianroad2"],
    u"��ɽ"     : [ "lingjiu/yan"],
    u"���ݳ�"   : [ "suzhou/xidajie2", "suzhou/dongdajie2","suzhou/road5", "suzhou/road1","suzhou/gumujiaohe", "suzhou/zhenquting"],
    u"���ݳ�"   : [ "hangzhou/suti2", "hangzhou/jujingyuan",   "hangzhou/liuzhuang", "hangzhou/road19", "hangzhou/huangniling", "hangzhou/qinglindong"],
    u"������"   : [ "xiangyang/westjie2", "xiangyang/southjie2", "xiangyang/xiaorong1", "xiangyang/zhonglie","xiangyang/guangchang", "xiangyang/dingzi"],
    u"Ȫ�ݳ�"   : [ "quanzhou/zhongxin"],
    u"���ݳ�"   : [ "fuzhou/ximendajie", "fuzhou/dongxiaojie","fuzhou/nanmen"],
    u"����"     : [ "lingzhou/xidajie", "lingzhou/nanmen","lingzhou/dongdajie"],
    u"����"     : [ "guanwai/baihe", "guanwai/road8","guanwai/xuedi1", "guanwai/beicheng","guanwai/shanshenmiao" ],
    u"����"     : [ "xingxiu/shamo5", "baituo/gebi",  "xueshan/shenghu", "xueshan/hubian4","xuedao/sroad3", "xuedao/nroad6","mingjiao/gebitan5","xingxiu/nanjiang2" ],
    u"����һ��" : [ "dali/northgate", "dali/southgate", "dali/shanlu2", "dali/buxiongbu", "dali/jinzhihe", "dali/xiaodao1","dali/tianweijing", "dali/wuding", "dali/luwang", "dali/gudao","dali/biluoxueshan", "dali/zhenxiong",    "dali/yixibu", "dali/cangshanzhong","dali/wumeng", "dali/hongsheng" ]
}


_outdoor = {
u"����":"fuzhou",
u"���޺�":"xingxiu",
u"����":"city",
u"����":"guanwai",
u"����":"suzhou",
u"�ɶ�":"city3",
u"��Ĺ":"gumu",
u"��ɽ":"lingjiu",
u"����":"lingzhou",
u"����":"changan",
u"����":"guanwai",
u"����ɽ(�书��)":"quanzhen",
u"����":"shaolin",
u"��ɽ":"songshan",
u"����":"xiangyang",
u"��ɽ��":"village",
u"���͵�":"xiakedao",
u"��ɽ":"foshan",
u"��ɽ":"huashan",
u"����":"dali",
u"Ȫ��":"quanzhou",
u"ѩɽ":"xueshan",
u"��ѩɽ":"xuedao",
u"����":"hangzhou",
u"������":"yanziwu",
u"����":"beijing",
u"����ɽ":"mingjiao",
u"�䵱":"wudang",
u"�ƺ�":"huanghe",
u"��ľ��":"heimuya",
u"����ɽ":"baituo",
u"������":"item",
u"̩ɽ":"taishan",
u"����ׯ":"guiyun",
u"������":"tianlongsi"
}

_place_start_rooms = {}  #��place �����start room
_all_start_rooms = []  #���е�start room

def _init_start_rooms():
    for palce,rooms_id in _place_start_rooms_id.iteritems():
        _place_start_rooms[palce] = []
        for room_id in rooms_id:
            room = get_room(room_id)
            _place_start_rooms[palce].append(room)
            _all_start_rooms.append(room)

_init_start_rooms()


def find_near_start_rooms(place, outdoor , name, steps):
    '''
    ��������㷨���ݹ飬������Ĺ�������㷨��
    ��ѯstart_room ����������Ϊroom_name�ķ���
    place ���ΪNone��ѯ����palce�Ŀ�ʼ����
    steps Ϊ����������0 ��ѯ start room,����ѯ����
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1

    if not outdoor in _outdoor:
        print "*******" + outdoor + " not config"

    result_rooms = []

    if place == None:
        start_rooms = _all_start_rooms
    else:
        start_rooms = _place_start_rooms.get(place,[])

    def find_near_rooms(room, steps):
        global _find_path_version
        if room.find_path_version == _find_path_version: 
            return
        room.find_path_version = _find_path_version
        if room.name == name and room.id.startswith(_outdoor[outdoor]):#
            print "***" + room.id
            result_rooms.append(room)

        if steps > 0:
            for exit in room.exits:
                e_room = exit.room;
                if e_room == None:
                    continue
                find_near_rooms(e_room,steps - 1)

    for room in start_rooms:
        find_near_rooms(room , steps)
    return result_rooms


def find_near_start_rooms_breadth_first(place, name , steps): 
    '''
    ��������㷨����Ϊ�������ϲ��������ܲ��������������ȣ��ݹ��㷨
    ��ѯstart_room ����������Ϊroom_name�ķ���
    place ���ΪNone��ѯ����palce�Ŀ�ʼ����
    steps Ϊ����������0 ��ѯ start room,����ѯ����
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1

    result_rooms = []

    if place == None:
        open = list(_all_start_rooms)
    else:
        open = list(_place_start_rooms.get(place,[]))
    
    for _ in range(steps):
        for o in open:
            open.remove(o) 
            if o.name == name: #and outdoor
                result_rooms.append(o)       
            for exit in o.exits: 
                next_room = exit.room 
                if next_room == None or next_room.find_path_version == _find_path_version: 
                    continue   
                next_room.find_path_version = _find_path_version 
                open.append(next_room)

        if len(open) == 0:
            break
    return result_rooms 

########## start room ########## 

