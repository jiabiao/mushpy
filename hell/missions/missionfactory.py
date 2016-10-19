from mushpy import McObject,ManualEndTask,async


class MissionFactory():

	factories = {}

	@classmethod
	def register_factory(cls, name, entry):
		factory = MissionFactory(name, entry)
		cls.factories[name] = factory
		return factory

	@classmethod
	@async("create_mission")
	def create(cls, config):
		name = config["name"]
		factory = cls.factories(name)
		McObject.enable_group(name)
		yield factory.entry(config)
		yield factory.met


	def __init__(self, name , entry):	
		self.name = name
		self.entry = entry
		self.met = ManualEndTask(name)



	def end(self):
		McObject.disable_group(self.name)
		self.met.end()	

