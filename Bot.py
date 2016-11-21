import re
import time
import os
import random
import datetime
import telepot
import subprocess


"""
Very Own, Personalised Telegram Bot. Why? Whatsapp bot is too main stream.

"""

def test(chat_id,command):

    g = os.popen(command).read()
    bot.sendMessage(chat_id,g)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/ip':
        bot.sendMessage(chat_id,str(subprocess.Popen(["curl", "ipinfo.io"], stdout=subprocess.PIPE).communicate()[0]))

    if "/getmp3" in command:

        command = msg['text']
        words = command.split()
        s= words[1]
        f = open(s+'.mp3','rb')
        bot.sendAudio(chat_id,audio=f)


    if command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

    if command == '/wakeup':
        bot.sendMessage(chat_id, str("Loading Modules..."))
        time.sleep(1)
        g = os.popen("pwd").read()
        bot.sendMessage(chat_id,str("Running in" + str(g)))
        time.sleep(1)
        bot.sendMessage(chat_id,str("Awaiting Commands...."))

    if "/getpic" in command:

        command = msg['text']
        words = command.split()
        s= words[1]
        f = open(s,'rb')
        bot.sendPhoto(chat_id,photo=f)

    if "/getdoc" in command:

        command = msg['text']
        words = command.split()
        s= words[1]
        f = open(s,'rb')
        bot.sendDocument(chat_id,document=f)


    else:
         test(chat_id,command)



bot = telepot.Bot('YOUR API KEY HERE ')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
