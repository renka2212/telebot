import telebot
import csv

bot = telebot.TeleBot('6083858885:AAHZFDPNbyxRmvqVkWxsiCLOkMQ4TSWlJIE')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>! Чтобы заполнить анкету, нажми /anketa'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['anketa'])
def anketa(message):
    bot.send_message(message.chat.id, 'Как вас зовут?')
    bot.register_next_step_handler(message, ask_instagram)

def ask_instagram(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Твои никнеймы (@) в Instagram и TikTok?')
    bot.register_next_step_handler(message, ask_age)

def ask_age(message):
    global instagram
    instagram = message.text
    bot.send_message(message.chat.id, 'Твой возраст?')
    bot.register_next_step_handler(message, ask_device)

def ask_device(message):
    global age
    age = message.text
    bot.send_message(message.chat.id, 'На что снимаешь? (Точная модель девайса (-ов))')
    bot.register_next_step_handler(message, ask_city)

def ask_city(message):
    global device
    device = message.text
    bot.send_message(message.chat.id, 'В каком городе находишься? В каком городе/городах есть возможность снимать?')
    bot.register_next_step_handler(message, ask_software)

def ask_software(message):
    global city
    city = message.text
    bot.send_message(message.chat.id, 'Какой софт используешь для монтажа? (Adobe Premiere Pro; VN; CapCut; DaVinci Resolve и тп.)')
    bot.register_next_step_handler(message, end)

def end(message):
    global software
    software = message.text

    # Открываем файл для записи в режиме 'a' (добавление)
    with open('anketa.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # записываем данные пользователя в CSV-файл
        writer.writerow([name, instagram, age, device, city, software])

    bot.send_message(message.chat.id, 'Теперь выполните обязательное задание, которое поможет нам понять Ваш уровень съемки.'
                                      '\nСнимите 2 коротких видео (12-15 секунд) по заданным темам и музыке:'
                                      '\n\n1. Снимите машину. Трек: Metro Boomin, Future - Superhero'
                                      '\n2. Снимите город. Трек: Drake - Jumbotron Shit Poppin, '
                                      '\n\nГотовые видео скидывай в Telegram @kkknapskyyy .')

    bot.send_message(message.chat.id, 'Спасибо за заполнение анкеты, она уже находится в обработке!')

bot.polling(none_stop=True)
