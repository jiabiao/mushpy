from objects import Trigger,Timer
from consts import *

class Task(object):
    result = None

    def __init__(self, name):
        self.name = name

    def begin(self):
        raise NotImplementedError

    def end(self, *args):
        print(self.name,"end")
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
    
    def __init__(self, match, name='matchTask'):
        super(MatchTask, self).__init__(name)
        self.match = match

    def begin(self):
        trig = Trigger(self.match, flags=TriggerFlags.eEnabled | TriggerFlags.eTemporary | TriggerFlags.eKeepEvaluating | TriggerFlags.eTriggerRegularExpression, one_shot = 1)        
        trig.callback(self.end)

 
class TimerTask(Task):
    """done after special period"""

    def __init__(self, hh, mm, ss):
        super(TimerTask, self).__init__(None)
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def begin(self):
        timer = Timer(self.hh, self.mm, self.ss, flags=TimerFlags.eEnabled | TimerFlags.eOneShot)        
        timer.callback(self.end)

 
class CombineTask(Task):
    def __init__(self, tasks, name='combineTask'):
        super(CombineTask, self).__init__(name)
        self.tasks=tasks

    def begin(self):
        self.next(None)

    def next(self,lastResult):
        try:
            nextchild = self.tasks.send(lastResult)
            nextchild.parent = self    
            print(self.name,">>",nextchild.name)        
            nextchild.begin()
        except StopIteration:
            self.tasks.close()
            if hasattr(self,"parent"):           
                self.end()  
      
 
def async(func):
    def createTask(*args,**kw):
        tasks = func(*args,**kw)
        name = None
        if "name" in kw:
            name = kw["name"]
        return CombineTask(tasks,name)
    return createTask
 
 
