from mushpy import McObject,ManualEndTask,async


class Mission():

	def __init__(self, name , entry):	
		self.name = name
		self.entry = entry
		self.met = ManualEndTask(name)


	def end(self):
		McObject.disable_group(self.name)
		self.met.end()	


missions = {}

def register_mission(name, entry):
	mission = Mission(name, entry)
	missions[name] = mission
	return mission

@async("mission")
def start(config):
	name = config["name"]
	McObject.enable_group(name)
	mission = missions[name]
	yield mission.entry(config)
	yield mission.met
