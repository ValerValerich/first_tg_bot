import telebot
from telebot import types
import datetime


with open('token.txt') as f:
    x=f.readline()
    
bot = telebot.TeleBot(x)



@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Я - бот калькулятор\n Введи пример текстом\n (пример:\n a+(b/c))")
    

@bot.message_handler(content_types=['text'])
def calc(message):
    
    try:
        bot.send_message(message.chat.id, f"{eval(str(message.text))}")
        bot.send_message(message.chat.id, f"Введи новый пример или нажми /start")
        
        
    except:
        bot.send_message(message.chat.id, "Такое посчитать нельзя")
        bot.send_message(message.chat.id, f"Введи новый пример или нажми /start")
        
    
#def calculator(message):
 #   return eval(str(message))
'''   
@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Сделать предложение")
    but2 = types.KeyboardButton("Узнать время")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "Сделать предложение":
        bot.send_message(message.chat.id, "Введи фамилию и имя")
        bot.register_next_step_handler(message, sentence)
        
    elif message.text == "Узнать время":
        bot.send_message(message.chat.id, datetime.datetime.now())
        button(message)





def sentence(message):
    text=message.text
    name=text.split()[1]
    surname=text.split()[0]
    bot.send_message(message.chat.id, f"Тебя зовут {name} {surname}" )
    button(message)
'''


bot.infinity_polling()