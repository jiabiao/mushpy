mushpy
======
**mushpy** : Encapsulate the [MUSHclient][1] API via Python script. write 'synchronous' code, and excute asynchronously. 
[1]: http://www.mushclient.com/ "a mud client"

## sample

```Python
	@async
	def work(name):
		world.DoAfter(3,'hi')
		yield MatchTask(u'^你双手抱拳，作了个揖道：各位英雄请了！$'）
	
		world.send('hp')
		yield TimerTask(0,0,5)
		
		yield sleep()
		world.send('say all done')
	
	@async
	def sleep():
		world.send('sleep')
		yield TimerTask(0,0,5)
		world.note('awake')
	
	
	#then call in command line:work('name').begin()
```

## references
[mushpy][2]: another Python framework on top of Mushclient's API
[2]:http://mushclient.com/forum/?id=10283

