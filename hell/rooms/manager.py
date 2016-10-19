# coding=gbk

import d
import revise
import hell
from revise import rootRoom
from d import Room,Exit


_find_path_version = 0 #类似于Dijkstra的Closed集合功能，凡是遍历过的房间不重复计算，即使新的路径更节约时间

########## help method ##########   
def get_room(id):	
    '''
    根据id查询房间
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
    查询从origin到terminus 的Exit
    '''
    for exit in origin.exits:
        if exit.room == terminus:
            return exit
    return None    

def get_back_exit(room):
    '''
    room -> root_room的第一个Exit
    找可以飞行的房间：可以沿着飞来的反方向不停Back
    '''
    if not hasattr(room,'back_exit'):
        room.back_exit = get_exit(room,room.come_room)
    return room.back_exit    


def get_exits_to_outdoor(room):
    '''
    room ->  outdoor
    找可以飞行的房间
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
    遍历room附近的所有房间，最后返回room
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
                if back == None:  #如果去了不能回来，就不要去了
                    continue
                next_room.find_path_version = _find_path_version
                exits.append(exit)                
                around(exit.room,back,steps - 1)        
        exits.append(back_exit)
    around(room,None,steps)
    exits.pop() #为了递归少一次判断，最后一个出口是None
    return exits

def get_exits_move(origin, min_step, max_step = 15):
    '''
    移动4步
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
    origin -> terminuses的任意一个房间
    返回元祖 （第一个 terminus, origin->terminus)
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1  #代替Closed集合

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
    返回 origin -> terminus的Exits
    
    '''
    global _find_path_version
    _find_path_version = _find_path_version + 1  #代替Closed集合

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
    u"华山附近" : [ "huashan/pingxinshi", "village/square", "village/wexit"],
    u"扬州城"   : [ "city/beimen", "city/nanmen", "city/ximen", "city/dongmen" ],
    u"长安城"   : [ "changan/dong_chengmen", "changan/nan_chengmen",   "changan/xi_chengmen", "changan/bei_chengmen", "changan/qinglong2", "changan/baihu2"],
    u"武功镇"   : [ "quanzhen/xijie", "quanzhen/nanjie"],
    u"佛山一带" : [ "foshan/street1", "foshan/southgate"],
    u"南海一带" : [ "xiakedao/xkroad4" ],
    u"汝州一带" : [ "shaolin/ruzhou" ],
    u"嵩山一带" : [ "songshan/tianzhongge", "shaolin/shijie1","shaolin/shijie8"],
    u"终南山"   : [ "quanzhen/shanlu1", "quanzhen/shijie1","quanzhen/shijie9", "quanzhen/cuipinggu",   "quanzhen/baishulin3", "gumu/taiyi1","gumu/shenheyuan", "quanzhen/banshanting"],
    u"成都城"   : [ "city3/southroad1", "city3/qingyanggong","city3/northroad2"],
    u"星宿海"   : [ "xingxiu/tianroad2"],
    u"天山"     : [ "lingjiu/yan"],
    u"苏州城"   : [ "suzhou/xidajie2", "suzhou/dongdajie2","suzhou/road5", "suzhou/road1","suzhou/gumujiaohe", "suzhou/zhenquting"],
    u"杭州城"   : [ "hangzhou/suti2", "hangzhou/jujingyuan",   "hangzhou/liuzhuang", "hangzhou/road19", "hangzhou/huangniling", "hangzhou/qinglindong"],
    u"襄阳城"   : [ "xiangyang/westjie2", "xiangyang/southjie2", "xiangyang/xiaorong1", "xiangyang/zhonglie","xiangyang/guangchang", "xiangyang/dingzi"],
    u"泉州城"   : [ "quanzhou/zhongxin"],
    u"福州城"   : [ "fuzhou/ximendajie", "fuzhou/dongxiaojie","fuzhou/nanmen"],
    u"灵州"     : [ "lingzhou/xidajie", "lingzhou/nanmen","lingzhou/dongdajie"],
    u"关外"     : [ "guanwai/baihe", "guanwai/road8","guanwai/xuedi1", "guanwai/beicheng","guanwai/shanshenmiao" ],
    u"西域"     : [ "xingxiu/shamo5", "baituo/gebi",  "xueshan/shenghu", "xueshan/hubian4","xuedao/sroad3", "xuedao/nroad6","mingjiao/gebitan5","xingxiu/nanjiang2" ],
    u"大理一带" : [ "dali/northgate", "dali/southgate", "dali/shanlu2", "dali/buxiongbu", "dali/jinzhihe", "dali/xiaodao1","dali/tianweijing", "dali/wuding", "dali/luwang", "dali/gudao","dali/biluoxueshan", "dali/zhenxiong",    "dali/yixibu", "dali/cangshanzhong","dali/wumeng", "dali/hongsheng" ]
}


_outdoor = {
u"福州":"fuzhou",
u"星宿海":"xingxiu",
u"扬州":"city",
u"关外":"guanwai",
u"苏州":"suzhou",
u"成都":"city3",
u"古墓":"gumu",
u"天山":"lingjiu",
u"灵州":"lingzhou",
u"长安":"changan",
u"关外":"guanwai",
u"终南山(武功镇)":"quanzhen",
u"少林":"shaolin",
u"嵩山":"songshan",
u"襄阳":"xiangyang",
u"华山村":"village",
u"侠客岛":"xiakedao",
u"佛山":"foshan",
u"华山":"huashan",
u"大理":"dali",
u"泉州":"quanzhou",
u"雪山":"xueshan",
u"大雪山":"xuedao",
u"杭州":"hangzhou",
u"燕子坞":"yanziwu",
u"北京":"beijing",
u"昆仑山":"mingjiao",
u"武当":"wudang",
u"黄河":"huanghe",
u"黑木崖":"heimuya",
u"白驼山":"baituo",
u"苏州南":"item",
u"泰山":"taishan",
u"归云庄":"guiyun",
u"天龙寺":"tianlongsi"
}

_place_start_rooms = {}  #按place 分组的start room
_all_start_rooms = []  #所有的start room

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
    深度优先算法，递归，比下面的广度优先算法快
    查询start_room 附近的名称为room_name的房间
    place 如果为None查询所有palce的开始房间
    steps 为附近几步，0 查询 start room,不查询附近
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
    广度优先算法，因为大量集合操作，性能不及上面的深度优先，递归算法
    查询start_room 附近的名称为room_name的房间
    place 如果为None查询所有palce的开始房间
    steps 为附近几步，0 查询 start room,不查询附近
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

