#/usr/bin/env python
import socket, random, threading, re
from time import sleep
import os
import inspect
import json

def curDir():
   return os.path.dirname(inspect.getsourcefile(curDir))

mods = {}
for directory, dirnames, filenames in os.walk('./'):
   if os.path.basename(directory) == 'modules':
      for package in dirnames:
         mods[package] = {'instance': __import__('modules.' + package), 'conf': json.loads(open(os.path.join(curDir(), 'modules/' + package + '/conf'), 'r').read())}

a = """
paused = False
global paused

def worker(sock, groups, admin):
   sock.send('PRIVMSG '+ admin +' :Initiating nick cycling and grabbing procedure \r\n')
   while not paused:
      for nick in wantedNicks:
         if not paused:
            sock.send('PRIVMSG NickServ :info ' + nick + '\r\n')
            sleep(69)

def cyclerWorker(sock, groups):
   while not paused:
      for group in groups:
         for nick in group['nicks']:
            sock.send('NICK ' + nick + '\r\n')
            sleep(1)
            sock.send('PRIVMSG NickServ :identify ' + group['password'] + '\r\n')
            sleep(interval)

def auth():
   irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   irc.connect((network, port))
   print irc.recv(4096)
   irc.send('NICK '+ tempnick + '\r\n')
   irc.send('USER '+ tempnick +' '+ tempnick +' '+ tempnick +' :Nick Bottu\r\n')
   print irc.recv(4096)
   irc.send('JOIN ' + channel + '\r\n')
auth()

snipeThread = threading.Thread(target=worker, args=(irc, groups, admin))
snipeThread.setDaemon(True)
snipeThread.start()

cycleThread = threading.Thread(target=cyclerWorker, args=(irc, groups))
cycleThread.setDaemon(True)
cycleThread.start()

while True:
   data = irc.recv(4096)
   if data == '':
      auth()
      continue

   m = re.match(".*Nick \x02(.*)\x02 isn't registered.", data.replace('\r\n', '').strip())
   if m != None:
      irc.send('NICK ' + m.group(1) + '\r\n')
      sleep(2)
      irc.send('PRIVMSG NickServ :group ' + groupTo['nick'] + ' ' + groupTo['password'] + '\r\n')
      sleep(5)
      irc.send('NICK ' + tempnick + '\r\n')
      print '!!!! TRIED TO SNAG ' + m.group(1) + ' !!!!'


   if data.find('PING') != -1:
      try:
         irc.send('PONG ' + data.split()[1] + '\r\n')
         print 'Answered PING probe' 
      except:
         pass
"""