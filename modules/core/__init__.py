class Main():
	def __init__(self, irc, conf):
		self.irc = irc
		self.conf = conf
		print 'Core loaded'
	def execute(self):
		print 'Core thread loaded'
		print 'Joining ' + self.conf.get('channel', '#HBs')
		import time
		time.sleep(2)
		self.irc.send('JOIN ' + self.conf.get('channel', '#HBs') + '\r\n')
		self.irc.send('PRIVMSG ' + self.conf.get('channel', '#HBs') + ' :NickBhottu now loaded\r\n')
	def e(self, args):
		pass