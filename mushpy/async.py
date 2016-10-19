from mcobjects import Trigger,Timer
from consts import *




class Task(object):
    result = None

    def __init__(self, name):
        self.name = name
        self.prefix=""

    def begin(self):
        raise NotImplementedError

    def end(self, *args):
        #print self.prefix + "<-" + self.name
        self.parent.next(self.result)  


class MockTask(Task):
    """docstring for MockTask"""
    def __init__(self, name):
        super(MockTask, self).__init__(name)
        self.name = name
        
    def begin(self):
        print("working:" + self.name)
        self.end()                        


class MatchTask(Task):
    """done after match special text"""        
    
    def __init__(self, match, tname='matchTask', **options):
        super(MatchTask, self).__init__(tname)
        options["one_shot"] = 1
        self.match = match
        self.options = options 

    def begin(self):
        trig = Trigger(self.match, flags=TriggerFlags.eEnabled | TriggerFlags.eReplace | TriggerFlags.eTemporary | TriggerFlags.eKeepEvaluating | TriggerFlags.eTriggerRegularExpression, **self.options)        
        trig.callback(self.callback)

    def callback(self, *args):
        self.result = args
        self.end(args)

 
class TimerTask(Task):
    """done after special period"""

    def __init__(self, hh, mm, ss, name = None):
        super(TimerTask, self).__init__(name or "timer")
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def begin(self):
        timer = Timer(self.hh, self.mm, self.ss, flags=TimerFlags.eEnabled | TimerFlags.eOneShot)        
        timer.callback(self.end)



class ManualEndTask(Task):
    """manual end task"""
    def __init__(self,name='manual_end_task'):
        super(ManualEndTask, self).__init__(name)

    def begin(self):
        pass

class ValueTask(Task):
    """only for return value"""        
    
    def __init__(self, result, name='valueTask'):
        super(ValueTask, self).__init__(name)
        self.result = result

    def begin(self):
        self.end(None)
        
 
class CombineTask(Task):
    def __init__(self, tasks, name='combineTask'):
        super(CombineTask, self).__init__(name)
        self.tasks=tasks

    def begin(self):
        self.next(None)

    def next(self,lastResult):
        try:
            gen = self.tasks
            if gen == None:
                self.end()
                return
            nextchild = gen.send(lastResult)
            nextchild.parent = self  
            nextchild.prefix = self.prefix + "\t"
            #print nextchild.prefix + "->" + nextchild.name
            nextchild.begin()
        except StopIteration:
            self.result = lastResult    
            self.tasks.close()
            if hasattr(self,"parent"):     
                self.end() 

      
 
# def async(func):
#     def createTask(*args,**kw):
#         tasks = func(*args,**kw)

#         return CombineTask(tasks,name)
#     return createTask


def async(name = None):
    def decorator(func):
        def createTask(*args, **kw):
            tasks = func(*args,**kw)
            task_name = name or func.__name__ 
            return CombineTask(tasks,task_name)
        return createTask
    return decorator 
 
