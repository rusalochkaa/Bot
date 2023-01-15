import telebot
from telebot import types
from settings import TOKEN


bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('Карта офиса')
itembtn2 = types.KeyboardButton('Коллевтив')
itembtn3 = types.KeyboardButton('Прочее')
markup.add(itembtn1, itembtn2, itembtn3)

markup2 = types.ReplyKeyboardMarkup(row_width=1)
itembtn12 = types.KeyboardButton('Сделать справку')
itembtn22 = types.KeyboardButton('Оформить отпускной лист')
itembtn32 = types.KeyboardButton('Где покушать?')
itembtn42 = types.KeyboardButton('Назад')
markup2.add(itembtn12, itembtn22, itembtn32, itembtn42)

photo1 = open('1 вход.jpg', 'rb')
photo2 = open('2 администратор.jpg', 'rb')
photo3 = open('3 кухня.jpg', 'rb')
photo4 = open('4 отдел логистики.jpg', 'rb')
photo5 = open('5 отдел продаж.jpg', 'rb')
photo6 = open('6.jpg', 'rb')
photo7 = open('7.jpg', 'rb')
photo8 = open('8.jpg', 'rb')
photo9 = open('9.jpg', 'rb')



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Приветствуем Вас в компании ТранкомС!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text=='Карта офиса')
def office_map(message):
    bot.send_message(message.chat.id, 'Небольшая экскурсия по месту,в котором ты проведешь ближайшие пару лет (надеемся:))')
    bot.send_photo(message.chat.id, photo1, caption='Вход')
    bot.send_photo(message.chat.id, photo2, caption='Администратор')
    bot.send_photo(message.chat.id, photo3, caption='Кухня')
    bot.send_photo(message.chat.id, photo4, caption='Отдел логистики')
    bot.send_photo(message.chat.id, photo5, caption='Отдел продаж')
    
@bot.message_handler(func=lambda message: message.text=='Коллевтив')
def collegues(message):
    bot.send_message(message.chat.id, 'Наш дружный коллевтив')
    bot.send_photo(message.chat.id, photo6, caption='Генеральный директор-Серебренников Роман Алексеевич')
    bot.send_photo(message.chat.id, photo7, caption='Главный бухгалтер-Пивоварова Татьяна Глебовна')
    bot.send_photo(message.chat.id, photo8, caption='Секретарь-Борт Виктория')
    bot.send_photo(message.chat.id, photo9, caption='Начальник отдела логистики- Серебренников Алексей Васильевич.')
    
@bot.message_handler(func=lambda message: message.text=='Где покушать?')
def food(message):
    bot.send_message(message.chat.id, '1. Главный бухгалтер советует вкуснецкое местечко «Кусь».  Находится: первый этаж нашего бизнес-центра.\n2. Роман Алексеевич говорит, что сытные порции и выгодный бизнес-ланч можно встретить в «Pepela».Адрес: Пр. Просвещения 38, этаж.\n3. Ну,а если ты не прихотлив, спускайся на 3 этажа вниз в столовку.\n')
    
@bot.message_handler(func=lambda message: message.text=='Прочее')
def others(message):
    bot.send_message(message.chat.id, 'тут будет прочее', reply_markup=markup2)
    
@bot.message_handler(func=lambda message: message.text=='Сделать справку')
def spravka(message):
    bot.send_message(message.chat.id, 'Запрос отправлен! Получить документ можно в течение 2-ух рабочих днех у секретаря')

    
@bot.message_handler(func=lambda message: message.text=='Оформить отпускной лист')
def otpysk(message):
    bot.send_message(message.chat.id, 'Необходимо наполнить заявление за 14 дней до отпуска и согласовать с руководством')
    
@bot.message_handler(func=lambda message: message.text=='Назад')
def back(message):
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()