import telebot
import config
import sqlite3
from telebot import types #Для создания клавиатуры

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def main_menu(message):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Авторазмер клавиатуры
   item1 = types.KeyboardButton("Факультеты")
   item2 = types.KeyboardButton("Порядок приема")
   item3 = types.KeyboardButton("Проф. Тест")
   item4 = types.KeyboardButton("Университет")
   item5 = types.KeyboardButton("Довузовская подготовка")
   item6 = types.KeyboardButton("Военная кафедра")
   item7 = types.KeyboardButton("Адрес")
   markup.add(item1, item2, item3, item4, item5, item6, item7)
   bot.send_message(message.chat.id, "Поздравляю, {0.first_name}!\nЯ - {1.first_name}, а Вы в главном меню!.".format(message.from_user, bot.get_me()), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def fakultet(message):
   if message.chat.type == 'private':
      if message.text == 'Факультеты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Машиностроительный факультет")
            item2 = types.KeyboardButton("Факультет инженерных систем и экологии")
            item3 = types.KeyboardButton("Строительный Факультет")
            item4 = types.KeyboardButton("Факультет Электронно-информационных систем")
            item5 = types.KeyboardButton("Экономический факультет")
            item6 = types.KeyboardButton("В главное меню")

            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, "У нас большой выбор факультетов, пожалуйста, уточните, какой именно Вас интересует?", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Машиностроительный факультет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Сайт факультета: msf.bstu.by.\nМСФ занимается исследованиями и подготовкой высококвалифицированных кадров для отраслей машиностроительного профиля. ", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Факультет инженерных систем и экологии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Сайт факультета: fise.bstu.by.\nФакультет организует подготовку инженеров для решения проблем экологического направления в водохозяйственном строительстве, организации безопасной жизнедеятельности людей, внедрения эффективных технологий для очистки природных и сточных вод.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Строительный Факультет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Сайт факультета: sf.bstu.by.\nСФ – основной факультет университета. Здесь ведется подготовка профессиональных специалистов для различных отраслей строительства. Факультет готовится к тому, чтобы в недалеком будущем выдавать своим выпускникам дипломы, признаваемые в странах ЕС.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Факультет Электронно-информационных систем':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Сайт факультета: feis.bstu.by.\nФЭИС занимается исследованиями и подготовкой высококвалифицированных кадров для быстроразвивающихся в западном регионе Республики Беларусь отраслей информационно-электронного профиля.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Экономический факультет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Сайт факультета: ef.bstu.by.\nЭФ призван решать региональные потребности в специалистах экономической сферы – бухгалтерах, экономистах, менеджерах, маркетологах.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : poryadok_priema(message)

@bot.message_handler(content_types=['text'])
def poryadok_priema(message):
   if message.chat.type == 'private':
      if message.text == "Порядок приема":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Контакты")
            item2 = types.KeyboardButton("Положение об олимпиаде")
            item3 = types.KeyboardButton("Порядок приёма в БрГТУ на 2023 год")
            item4 = types.KeyboardButton("В главное меню")
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "Порядок приема", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Контакты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Консультации по вопросам поступления на заочную форму получения образования в полный срок, на заочную форму получения образования в сокращенный срок (на основе среднего специального образования) и получения второго высшего образования – тел. 32-17-76 (приемная комиссия).", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Положение об олимпиаде':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Ознакомтесь, пожалуйста, с данным файлом:", reply_markup=markup)
            f = open("files//Polozheniye_ob_olimpiade_BrGTU.pdf","rb")
            bot.send_document(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'Порядок приёма в БрГТУ на 2023 год':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Ознакомтесь, пожалуйста, с данным файлом:", reply_markup=markup)
            f = open("files//BrGTU_poryadok_priyema_2023.pdf","rb")
            bot.send_document(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : adres(message)

@bot.message_handler(content_types=['text'])
def adres(message):
   if message.chat.type == 'private':
      if message.text == "Адрес":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Пинский индустриально-педагогический колледж")
         item2 = types.KeyboardButton("Главный корпус")
         item3 = types.KeyboardButton("Политехнический колледж")
         item4 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4)
         bot.send_message(message.chat.id, "Выбирете униврситет", reply_markup=markup)

   if message.chat.type == 'private':
      if message.text == 'Пинский индустриально-педагогический колледж':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id,"Пинский индустриально-педагогический колледж находится по адресу: Беларусь, Пинск, ул. Иркутско-Пинской Дивизии, 27\nhttps://yandex.kz/profile/-/CCU6i-wVTB\n Сайт: http://bspc.bstu.by/ru/", reply_markup=markup)

   if message.chat.type == 'private':
      if message.text == 'Политехнический колледж':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id,"Политехнический филиал находится по адресу: Брест, ул. Карла Маркса, 49\nhttps://yandex.kz/maps/-/CCU6mAbokD\n Сайт: http://bspc.bstu.by/ru/", reply_markup=markup)

   if message.chat.type == 'private':
      if message.text == 'Главный корпус':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id,"Главный корпус находится по адресу: ул.Московская 267, 224017, Брест, Республика Беларусь\nhttps://yandex.kz/profile/-/CCU6mAcM0D\n Сайт: https://www.bstu.by/", reply_markup=markup)
   if message.chat.type == 'private':
      if message.text == 'В главное меню' :
         main_menu(message)
      else : voen_kafedra(message)

@bot.message_handler(content_types=['text'])
def voen_kafedra(message):
   if message.chat.type == 'private':
      if message.text == "Военная кафедра":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Задачи")
         item2 = types.KeyboardButton("Контакты и адрес")
         item3 = types.KeyboardButton("Специальности")
         item4 = types.KeyboardButton("Формат обучения")
         item5 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4, item5)
         bot.send_message(message.chat.id, "Постановлением Совета Министров Республики Беларусь от 14 апреля 2020 года № 220 «Об изменении в постановление Совета Министров Республики Беларусь от 5 ноября 2003 года № 1469» учреждение образования «Брестский государственный технический университет» включен в Перечень учреждений высшего и среднего специального образования, в которых проводится обучение граждан на военных кафедрах.", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Задачи':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Обучение студентов и учащихся по программам военной подготовки;\nРазработка учебно-методической документации;\nПроведение научных исследований;\nСовершенствование учебно-материальной базы.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Контакты и адрес':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Адрес: 224030, г. Брест, ул. Дзержинского, 22\nE-mail: vk@bstu.by\nСсылка на сайт: https://www.bstu.by/obrazovanie/voennaya-kafedra", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Специальности':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Боевое применение мотострелковых подразделений, воинских частей и соединений на боевых машинах пехоты\nБоевое применение минометных подразделений, воинских частей и соединений\nБоевое применение подразделений, воинских частей и соединений вооруженных ракетными системами залпового огня до 220-мм включительно\n", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Формат обучения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Набор для обучения осуществляется на конкурсной основе\nСрок обучения – 2 года. В период обучения со студентами проводятся лекции, групповые и практические занятия\nЗавершается обучение итоговой практикой и экзаменом в воинской части.\n\n", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : dovuz_podgotovka(message)

@bot.message_handler(content_types=['text'])
def dovuz_podgotovka(message):
   if message.chat.type == 'private':
      if message.text == "Довузовская подготовка":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Проходные баллы по специальностям в 2022 г.")
         item2 = types.KeyboardButton("Виды подготовки к вступительным испытаниям")
         item3 = types.KeyboardButton("Ссылка на страницу")
         item4 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4)
         bot.send_message(message.chat.id,"Довуз.подготовка", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Проходные баллы по специальностям в 2022 г. (бюджет)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "Проходные баллы для разных специальностей", reply_markup=markup)
            f = open("files//ПРОХОДНЫЕ БАЛЛЫ_БЮДЖЕТ_2022.doc","files//ПРОХОДНЫЕ БАЛЛЫ_ПЛАТНО_2022.doc","rb")
            bot.send_document(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'Виды подготовки к вступительным испытаниям':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "вечерние курсы со сроком обучения 8 месяцев (октябрь-май), формируются группы по 5-6 человек;\nкурсы выходного дня: занятия по субботам в течение 6 месяцев (декабрь-май), формируются группы до 12 человек;\nвечерние курсы со сроком обучения 4 месяца (февраль-май), формируются группы до 12 человек;\nкраткосрочные курсы интенсивной подготовки (май-июнь) в течение 5 дней перед каждым тестовым испытанием, формируются группы до 12 человек.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Ссылка на страницу':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "https://www.bstu.by/abiturientam/dovuzovskaya-podgotovka", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : universitet(message)

@bot.message_handler(content_types=['text'])
def universitet(message):
   if message.chat.type == 'private':
      if message.text == "Университет":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Структура и контакты")
         item2 = types.KeyboardButton("Идеологическая и воспитательная работа")
         item3 = types.KeyboardButton("Руководство")
         item4 = types.KeyboardButton("Филиалы")
         item5 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4, item5)
         bot.send_message(message.chat.id,"Основная информация по университету", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Структура и контакты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "https://www.bstu.by/universitet/struktura-i-kontakty\nE-mail: canc@bstu.by (по официальным вопросам)\nТелефоны: +375 162 32-17-32 (приемная ректора), +375 162 32-17-76 (приемная комиссия)\nФакс: +375 162 32-17-55\n", reply_markup=markup)
            f= open("files//funct-struct-2022.pdf","rb")
            bot.send_document(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'Идеологическая и воспитательная работа':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "https://www.bstu.by/universitet/ivr", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Руководство':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "https://www.bstu.by/universitet/rukovodstvo\nБаханович Александр Геннадьевич\nРектор\nдоктор технических наук\nдоцент\n+375 162 32-17-32 (приёмная)", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Филиалы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "Политехнический коллледж\n http://bspc.bstu.by/ru/\nПинский индустриально-педагогический колледж\nhttps://uo-pgipk.bstu.by/", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : prof(message)

conect = sqlite3.connect("test.db", check_same_thread=False)
cursor = conect.cursor()
conect.commit()
a= 0
n= ""
m= ""
marks = '''()'",'''
def que_one_res():
   global m
   cursor.execute("SELECT que_one FROM test")
   res_one = cursor.fetchall()
   m = res_one[a]
   m= str(m)
   for x in m:  
      if x in marks:  
         m = m.replace(x, "") 
def que_two_res():
   global n
   cursor.execute("SELECT que_two FROM test")
   res_two = cursor.fetchall()
   n = res_two[a]
   n = str(n)
   for x in n:  
      if x in marks:  
         n = n.replace(x, "") 
que_one_res()
que_two_res()
first_count= 1
second_count= 1
que_count = 0

@bot.message_handler(content_types=['text'])
def prof(message):
   global a, first_count, second_count, que_count
   if message.chat.type == 'private':
      if message.text == 'Проф. Тест':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton(text= m)
         item2 = types.KeyboardButton(text= n)
         markup.add(item1, item2)
         bot.send_message(message.chat.id, "Выбери то, что тебе ближе", reply_markup=markup)
         print(n,m)
   if message.chat.type == 'private':
      if message.text == n:
         second_count += 1
         que_count +=1
         a+=1
         que_one_res()
         que_two_res()
         print (n,m)
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton(text= m)
         item2 = types.KeyboardButton(text= n)
         markup.add(item1, item2)
         bot.send_message(message.chat.id, "Выбери то, что тебе ближе", reply_markup=markup)
         print ("Очки 2 вопроса:",second_count)
         print ("Всего вопросов:",que_count)
         if que_count == 14:
            otvet_tg(message)

   if message.chat.type == 'private':
      if message.text == m:
         first_count += 1
         que_count +=1
         a+=1
         que_one_res()
         que_two_res()
         print (n,m)
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton(text= m)
         item2 = types.KeyboardButton(text= n)
         markup.add(item1, item2)
         bot.send_message(message.chat.id, "Выбери то, что тебе ближе", reply_markup=markup)
         print ("Очки 1 вопроса:",first_count)
         print ("Всего вопросов:",que_count)
         if que_count == 14:
            otvet_tg(message)
def otvet():
   global tip
   percent = (first_count/que_count)*100
   if percent < 10:
      tip = ("1 професия")
   if 10< percent < 20:
      tip = ("2 професия")
   if 20< percent < 30:
      tip = ("3 професия")
   if 30< percent < 40:
      tip = ("4 професия")
   if 40< percent < 50:
      tip = ("5 професия")
   if 50< percent < 60:
      tip = ("6 професия")
   if 60< percent < 70:
      tip = ("7 професия")
   if 70< percent < 80:
      tip = ("8 професия")
   if 80< percent < 90:
      tip = ("9 професия")
   if 90< percent < 100:
      tip = ("10 професия")
   if 100< percent:
      tip = ("11 Профессия")
tip = ""
tip = str(tip)
@bot.message_handler(content_types=['text'])
def otvet_tg(message): 
   global a, first_count, second_count, que_count, tip
   otvet()
   if message.chat.type == 'private':
      if message.text == "Шифровальщик" or "Искусствовед":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id, "Поздравляю, У Вас " + tip, reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
bot.polling(none_stop=True)