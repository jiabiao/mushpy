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

    def __init__(self):
        McObject._index += 1
        self._name = "mc" +  str(McObject._index)
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
    def disable_group(self,group):
        world.EnableGroup(group, 1)
    
    @staticmethod        
    def enable_group(self):
        world.EnableGroup(group, 0)    

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


    def GC():
        if len(McObject._callbacks) < 30:
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
        for t in timerlist:
                if t in McObject._callbacks:
                    newcallbacks[t] =McObject._callbacks[t]

        print("garbage collection. before:%s ,after:%s",len(McObject._callbacks),len(newcallbacks))
        McObject._callbacks = newcallbacks


g.CbFacade = lambda *args : McObject._callbacks[args[0]](*args)

# ------------------------
#       Trigger
# ------------------------
class Trigger(McObject):

    def __init__(self, match, flags = None, **options):        
        if 'script' in options:
            raise KeyError(options, '"script" cannot be used')
        if 'match' in options:
            raise KeyError(options, '"match" cannot in options')    
        if not match:
            raise ValueError(match, "'match' cannot be empty")
        if flags == None:
            flags = TriggerFlags.KeepEval_Re | TriggerFlags.eEnabled

        super(Trigger, self).__init__()

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
    def disable_group(self,group):
        world.EnableTriggerGroup (group, 1)
    
    @staticmethod        
    def enable_group(self):
        world.EnableTriggerGroup (group, 0)

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
            flags = AliasFlags.Re

        super(Alias, self).__init__()

        res = world.AddAlias(name, match, "", flags, "")
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
    def disable_group(self,group):
        world.EnableAliasGroup(group, 1)
    
    @staticmethod        
    def enable_group(self):
        world.EnableAliasGroup(group, 0)

class Timer(McObject):

    def __init__(self, hour, minute, second, flags = None, **options):        
        if 'script' in options:
            raise KeyError(options, '"script" cannot be used')
        if flags == None:
            flags = TimerFlags.OneShot

        super(Timer, self).__init__()
        print(self._name,hour,minute,second)
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
    def disable_group(self,group):
        world.EnableTimerGroup (group, 1)
    
    @staticmethod        
    def enable_group(self):
        world.EnableTimerGroup (group, 0)
