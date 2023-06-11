import requests
import random
import telebot


from bs4 import BeautifulSoup as b
URL = 'https://www.anekdot.ru/author-best/years/?years=anekdot'
API_KEY = '6141467332:AAF1WZtoJLQJo-A1UiTQHvPbtXcMBvBUHYs'

def parser(url):
    r = requests.get(URL)
    soup = b(r.text,'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте, это канал Юрлов Евгений, чтобы посмеяться введите любую цифру:')

@bot.message_handler(content_types=['text'])
def Jokes(message):
    if message.text.lower() in '1234567889':
        bot.send_message(message.chat.id,list_of_jokes[0])
        print(message)
        del list_of_jokes[0]
    else: bot.send_message(message.chat.id,'Введите любую цифру:')


bot.polling()
