class Room():

    group_by_name = {}

    def __init__(self, id, name, outdoor, nofight,exits = None):        
    	if exits == None:
    		exits = []
        self.id = id
        self.name = name
        self.outdoor = outdoor
        self.nofight = nofight
        self.exits = exits
        self.level = 99999
        self.time = 99999
        self.find_path_version = None 

        if name in Room.group_by_name:
            Room.group_by_name[name].append(self)
        else:
            Room.group_by_name[name] = [self]


    def find_exit(self,dir):
        for exit in self.exits:
            if exit.direction == dir:
                return exit
        return None


class Exit():

    time = 0.04
    block = False
    cmdTask = None
    cmd = None

    def __init__(self, direction,room_id,hasDoor = False):
        self.room_id = room_id
        self.room = None
        self.direction = direction
        self.hasDoor = hasDoor
        