import telebot
from telebot import types
import time
token = '1489830132:AAGuqXjSZXukE4oJDmofhtl-eTJ6hBMJ2Ao'
bot = telebot.TeleBot(token)
user={}

@bot.message_handler(commands=['start'])
def first(message):
    if message.chat.id in user:
        user[message.chat.id]=[]
        bot.send_message(message.chat.id, "Введіть ваше Ім'я:")
        print(message.text)
        bot.register_next_step_handler(message, second)
    else:
        user.update({message.chat.id:[]})
        bot.send_message(message.chat.id, "Введіть ваше Ім'я:")
        print(message.text)
        bot.register_next_step_handler(message, second)
def second(message):
    name = message.text
    if len(name)>2 and len(name)<20:
        user[message.chat.id].append(name)
        send=bot.send_message(message.chat.id, f"У профіль було додано імя - {message.text}")
        send=bot.send_message(message.chat.id, f"Напишіть свій вік")
        bot.register_next_step_handler(message, age1)
    else:
        send=bot.send_message(message.chat.id, "Введіть ваше Ім'я:")
        bot.register_next_step_handler(send, second)
    print(user)
def age1(message):
    age = message.text
    try:
        int(age)
        user[message.chat.id].append(age)
        send=bot.send_message(message.chat.id, f"У профіль був додан вік - {message.text}")
        send = bot.send_message(message.chat.id, f"Напишіть вашу стать \n-ч\n-ж")
        bot.register_next_step_handler(send, stat1)
    except:
        send=bot.send_message(message.chat.id, "Введіть ваш вік коректно:")
        bot.register_next_step_handler(send, age1)
    print(user)
def stat1(message):
    stat = message.text
    if stat =='ч' or stat =='ж':
        user[message.chat.id].append(stat)
        bot.send_message(message.chat.id, f"У профіль була додана стать - {stat}")
        bot.send_message(message.chat.id,'Профіль заповнен')
        #bot.register_next_step_handler(send, menua)
        send_welcome(message)
    else:
        send = bot.send_message(message.chat.id, "Введіть вашу стать коректно:")
        bot.register_next_step_handler(message, stat1)

def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Інфа про мене','Налаштування') #Имена кнопок
    msg = bot.reply_to(message, 'Меню', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)
def process_step(message):
    if message.text=='Інфа про мене':
        bot.send_message(message.chat.id, f'Ваше імя - {user[message.chat.id][0]}\n'
                                          f'Ваш вік - {user[message.chat.id][1]}\n'
                                          f'Ваша стать - {user[message.chat.id][2]}')
        send_welcome(message)
    elif message.text=='Налаштування' or message.text=='Назад':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Змінити вік', 'Змінити стать')
        keyboard.add("Змінити Ім'я")
        keyboard.add("Назад")
        msg = bot.reply_to(message, 'Меню', reply_markup=keyboard)
        bot.register_next_step_handler(msg, process_step2)
def process_step2(message):
    if message.text=='Назад':
        send_welcome(message)
    elif message.text=='Змінити вік':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Змінити вік')
        keyboard.add("Назад")
        msg = bot.reply_to(message, 'Змінити вік', reply_markup=keyboard)
        bot.register_next_step_handler(msg, vik)
    elif message.text=="Змінити Ім'я":
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("Змінити Ім'я")
        keyboard.add("Назад")
        msg = bot.reply_to(message, "Змінити Ім'я", reply_markup=keyboard)
        bot.register_next_step_handler(msg, vik1)
    elif message.text=='Змінити стать':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Змінити стать')
        keyboard.add("Назад")
        msg = bot.reply_to(message, 'Змінити стать', reply_markup=keyboard)
        bot.register_next_step_handler(msg, vik2)

def vik2(message):
    if message.text == 'Назад':
        process_step(message)
    elif message.text == 'Змінити стать':
        send = bot.send_message(message.chat.id, f"Введіть стать на яку ви хочете змінити")
        bot.register_next_step_handler(send, zmina2)

def zmina2(message):
    m=message.text
    if m=='ч' or m=='ж':
        user[message.chat.id][2] = m
        bot.send_message(message.chat.id, f"Змінено")
        send_welcome(message)
    else:
        bot.send_message(message.chat.id, f"Ввели некоректні данні")
        send_welcome(message)

def vik1(message):
    if message.text == 'Назад':
        process_step(message)
    elif message.text == "Змінити Ім'я":
        send = bot.send_message(message.chat.id, f"Введіть Ім'я на яке ви хочете змінити")
        bot.register_next_step_handler(send, zmina1)
def zmina1(message):
    m=message.text
    if len(m)>2 and len(m)<20:
        user[message.chat.id][0] = m
        bot.send_message(message.chat.id, f"Змінено")
        send_welcome(message)
    else:
        bot.send_message(message.chat.id, f"Ввели некоректні данні")
        send_welcome(message)
def vik(message):
    if message.text=='Назад':
        process_step(message)
    elif message.text=='Змінити вік':
        send=bot.send_message(message.chat.id, f"Введіть вік на який ви хочете змінити")
        bot.register_next_step_handler(send,zmina)
def zmina(message):
    try:
        m = int(message.text)
        user[message.chat.id][1] = m
        bot.send_message(message.chat.id, f"Змінено")
        send_welcome(message)
    except:
        bot.send_message(message.chat.id, f"Ввели некоректні данні")
        send_welcome(message)

if __name__ == '__main__':  # Блок запуска бота
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PollingError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(5)  # Делаем паузу в 5 секунд и выполняем команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота
