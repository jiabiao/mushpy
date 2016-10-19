from consts import *
from sys import world,g

class McObject(object):

    _index = 100    
    _callbacks ={}   

    # ----------- VIRTUAL ----------------
    def _set_option(self, key, value):
        '''Proxy to set object option.
        
        It should return the corresponding MUSH return error code.'''
        raise NotImplementedError

    def _get_option(self, key):
        '''Proxy to get object option.'''
        raise NotImplementedError

    def _del(self):
        '''Proxy to del object.'''
        raise NotImplementedError


    # ----------- END VIRTUAL ----------------

    def __init__(self, name = None):
        McObject._index += 1
        self._name = name or "mc" +  str(McObject._index)
        self._index = McObject._index

    def __cmp__(self, other):
        if self._index == other._index: return 0

    def __hash__(self):
        return self._index 

    def __getitem__(self, key):
        res = self._get_option(key)
        if res == None: # FIXME Obj. not found handled???
            raise KeyError(key)
        return res

    def __setitem__(self, key, value):
        if key == 'name':
            raise KeyError(key, "Cannot set 'name'")

        res = self._set_option(key, value)
        if res != ErrorNo.eOK:
            raise KeyError(res, 'Error setting option %s => %s' % (key, value))    

    def delete(self):
        res = self._del()
        if res == ErrorNo.eItemInUse:
            pass
        elif res != ErrorNo.eOK:
            raise SystemError(res, "Error deleting object.")

    def enable(self):
        self['enabled'] = 1
    def disable(self):
        self['enabled'] = 0

    @staticmethod    
    def disable_group(group):
        world.EnableGroup(group, False)
    
    @staticmethod        
    def enable_group(group):
        world.EnableGroup(group, True)    

    def callback(self,func):
        '''Set a callback to call when match matches.

        A callback can be any python callable, which should meet the
        corresponding mush object's callback interface, i.e.,

            * trigger/alias: cb(name, line, wc)
            * timer: cb(name)
        '''
        if not callable(func):
            raise TypeError(func, 'Not callable')
        McObject._callbacks[self._name] = func
        self["script"] = "CbFacade"
        return func

    @staticmethod
    def GC():
        if len(McObject._callbacks) < 50:
            return;        
        newcallbacks = {}

        triggerlist = world.GetTriggerList
        if (triggerlist):
            for t in triggerlist:
                if t in McObject._callbacks:
                    newcallbacks[t] =McObject._callbacks[t]

        aliaslist = world.GetAliasList
        if (aliaslist):
            for a in aliaslist:
                if a in McObject._callbacks:
                    newcallbacks[a] =McObject._callbacks[a]

        timerlist = world.GetTimerList
        if (timerlist):
            for t in timerlist:
                    if t in McObject._callbacks:
                        newcallbacks[t] =McObject._callbacks[t]

        print "garbage collection. before:%d ,after:%d" % (len(McObject._callbacks), len(newcallbacks))
        McObject._callbacks = newcallbacks



g.CbFacade = lambda *args : McObject._callbacks[args[0]](*args)


# ------------------------
#       Trigger
# ------------------------
class Trigger(McObject):

    def __init__(self, match, name = None, flags = None, **options):        
        if 'script' in options:
            raise KeyError(options, '"script" cannot be used')
        if 'match' in options:
            raise KeyError(options, '"match" cannot in options')    
        if not match:
            raise ValueError(match, "'match' cannot be empty")
        if flags == None:
            flags = TriggerFlags.KeepEval_Re | TriggerFlags.eEnabled
            if name:
                flags = flags | TriggerFlags.eReplace

        super(Trigger, self).__init__(name)

        res = world.AddTriggerEx(self._name, match, "", flags, -1, 0, "", "", 0, 100)
        if res != ErrorNo.eOK:
            raise SystemError(res, 'Adding failed')
        for (key, value) in options.items():
            self[key] = value


    def _set_option(self, key, value):
        return world.SetTriggerOption(self._name, key, value)

    def _get_option(self, key):
        return world.GetTriggerOption(self._name, key)

    def _del(self):
        return world.DeleteTrigger(self._name)

    @staticmethod   
    def exists(name):
        return ErrorNo.eOK == world.IsTrigger(name)

    @staticmethod    
    def disable_group(group):
        world.EnableTriggerGroup (group, False)
    
    @staticmethod        
    def enable_group(group):
        world.EnableTriggerGroup (group, True)

# ------------------------
#       Alias
# ------------------------
class Alias(McObject):

    def __init__(self, match, name = None, flags = None, **options):        
        if 'script' in options:
            raise KeyError(options, '"script" cannot be used')
        if 'match' in options:
            raise KeyError(options, '"match" cannot in options')    
        if not match:
            raise ValueError(match, "'match' cannot be empty")
        if flags == None:
            flags = AliasFlags.Re | TriggerFlags.eTemporary
            if name:
                flags = flags | AliasFlags.eReplace

        super(Alias, self).__init__(name)

        res = world.AddAlias(self._name, match, "", flags, "")
        if res != ErrorNo.eOK:
            raise SystemError(res, 'Adding failed')
        for (key, value) in options.items():
            self[key] = value

    def _set_option(self, key, value):
        return world.SetAliasOption(self._name, key, value)

    def _get_option(self, key):
        return world.GetAliasOption(self._name, key)

    def _del(self):
        return world.DeleteAlias(self._name)

    @staticmethod   
    def exists(name):
        return ErrorNo.eOK == world.IsAlias(name)

    @staticmethod    
    def disable_group(group):
        world.EnableAliasGroup(group, False)
    
    @staticmethod        
    def enable_group(group):
        world.EnableAliasGroup(group, True)

class Timer(McObject):

    def __init__(self, hour, minute, second, name = None, flags = None, **options):        
        if 'script' in options:
            raise KeyError(options, '"script" cannot be used')
        if flags == None:
            flags = TimerFlags.eEnabled | TimerFlags.eTemporary
            if name:
                flags = flags | TimerFlags.eReplace
            else:
                flags = flags | TimerFlags.eOneShot
                

        super(Timer, self).__init__(name)
        res = world.AddTimer(self._name, hour, minute, second, "", flags, "")
        if res != ErrorNo.eOK:
            raise SystemError(res, 'Adding failed')
        for (key, value) in options.items():
            self[key] = value

    def _set_option(self, key, value):
        return world.SetTimerOption(self._name, key, value)

    def _get_option(self, key):
        return world.GetTimerOption(self._name, key)

    def _del(self):
        return world.DeleteTimer(self._name)

    @staticmethod  
    def exists(name):
        return ErrorNo.eOK == world.IsTimer(name)

    @staticmethod    
    def disable_group(group):
        world.EnableTimerGroup (group, False)
    
    @staticmethod        
    def enable_group(group):
        world.EnableTimerGroup (group, True)



def trigger(pattern, name = None, flags = None, **options):    
    tr = Trigger(pattern, name, flags,**options)    
    def CalledOnFunc(func):
        tr.callback(func)
        return func
    return CalledOnFunc


def timer(hour, minute, second, name = None, flags = None, **options):    
    ti = Timer(hour, minute, second, name, flags,**options)    
    def CalledOnFunc(func):
        ti.callback(func)
        return func
    return CalledOnFunc


def alias(pattern, name = None,flags = None, **options):    
    a = Alias(pattern, name, flags,**options)    
    def CalledOnFunc(func):
        a.callback(func)
        return func
    return CalledOnFunc

@timer(0,10,0, name ="gc",flags=TimerFlags.eEnabled | TimerFlags.eTemporary | TimerFlags.eReplace,group="core")
def GC(*args):
    McObject.GC()


