from config import TOKEN

import datetime
import telebot as tb

bot = tb.TeleBot(TOKEN)

class ConstantValue:

    def __init__(self):

        self.commandlist = [ '/start', '/command', '/data', '/stop' ]

        self.commanddisc = [ 'start bot', 'command list', 'current data', 'stop bot' ]


@bot.message_handler(commands=['start', 'stop'])
def getStartEndMessege(message):

    if message.text == '/start':

        bot.send_message(message.from_user.id, 'Hello!')

    else:

        bot.send_message(message.from_user.id, 'Bye!')
        bot.stop_bot()

@bot.message_handler(commands=['command'])
def getComList(message):

    list = ConstantValue().commandlist
    discrip = ConstantValue().commanddisc

    out  = ''

    for i in list:

        out += i + ' ' + discrip[ list.index(i) ] + '\n'

    bot.send_message(message.from_user.id, out)

@bot.message_handler(commands=['data'])
def getData(message):
    bot.send_message(message.chat.id, str( datetime.datetime.utcfromtimestamp(message.date + 10800) ) )

bot.polling()