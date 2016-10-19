# coding=gbk

import codecs 
from sys import world  
from mushpy import trigger,alias
import users

me = None


with open("hell/core/token.txt") as _tf:
 	_tokens = { t[:2]:t for t in  _tf.read().splitlines()};


@trigger('^ver1.0,..(..)',name='login_token', group='core')
def _sendToken(*args):
	key = args[2][0]
	world.send(_tokens.get(key))

@trigger('^版本验证成功$',name='login_user', group='core')
def _autoLogin(*args):	
	login(world.getInfo(3))

@alias('^@(.+)')
def _manualLogin(*args):
	if me:
		return
	login(args[2][0])

def login(id):
	global me

	if id != "":	
		me = getattr(users, id, None)
		if me:			
			world.send(me.password)
			init_room(id)#init 是rooms.manager模块注册的方法
		else:
			world.note(id + u" 没有配置")
	else:
		world.note("手动登录：@id")








