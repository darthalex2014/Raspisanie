import os
from background import keep_alive
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
import datetime

bot = telebot.TeleBot('7361322981:AAF2LdejPyfxsg1_JwV-Ypv0_7RqU5xym3M')

def get_schedule(month, day, weekday):
    schedule = []

    if weekday == 0:  # Понедельник
        if month == 9 and day in [2, 9, 16, 23, 30]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})
        elif month == 10 and day in [7, 14, 21, 28]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})
        elif month == 11 and day in [11, 18, 25]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})
        elif month == 12 and day in [2, 9, 16, 23]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})

    elif weekday == 1:  # Вторник
        if month == 10 and day == 8:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "лекция"})
        elif month == 10 and day == 29:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "семинар"})
        elif month == 11 and day == 19:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "лекция"})
        elif month == 12 and day == 10:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Современные информационно-коммуникационные технологии и стратегическое управление", "type": "семинар"})

        if month == 9 and day == 17:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Основные тенденции мирового развития", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Основные тенденции мирового развития", "type": "лекция"})
        elif month == 10 and day == 1:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Основные тенденции мирового развития", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Основные тенденции мирового развития", "type": "лекция"})
        elif month == 10 and day == 22:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Основные тенденции мирового развития", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Основные тенденции мирового развития", "type": "семинар"})
        elif month == 11 and day == 12:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Основные тенденции мирового развития", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Основные тенденции мирового развития", "type": "семинар"})
        elif month == 12 and day == 3:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Основные тенденции мирового развития", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Основные тенденции мирового развития", "type": "семинар"})

        if month == 9 and day == 10:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Дипломатия: эволюция и современная практика", "type": "лекция"})
        elif month == 9 and day == 24:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Дипломатия: эволюция и современная практика", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Дипломатия: эволюция и современная практика", "type": "лекция"})

        elif month == 10 and day == 15:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Дипломатия: эволюция и современная практика", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Дипломатия: эволюция и современная практика", "type": "семинар"})

        elif month == 11 and day == 26:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Дипломатия: эволюция и современная практика", "type": "лекция"})
        elif month == 11 and day == 5:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Дипломатия: эволюция и современная практика", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Дипломатия: эволюция и современная практика", "type": "семинар"})
        elif month == 12 and day == 17:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Дипломатия: эволюция и современная практика", "type": "семинар"})


    elif weekday == 2:  # Среда
        if month == 9 and day in [4, 11, 18, 25]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})
        elif month == 10 and day in [2, 9, 16, 23, 30]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})
        elif month == 11 and day in [6, 13, 20, 27]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})
        elif month == 12 and day in [4, 11, 18]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Иностранный язык", "type": "пара"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Иностранный язык", "type": "пара"})

    elif weekday == 3:  # Четверг
        if month == 9 and day == 19:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "лекция"})
        elif month == 10 and day in [10, 31]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "лекция"})
        elif month == 11 and day == 21:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "семинар"})
        elif month == 12 and day == 12:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "семинар"})

    elif weekday == 4:  # Пятница
        if month == 9 and day in [13, 27]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Внешнеполитический процесс современной России(лекция Штоль В.В.)", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Внешнеполитический процесс современной России(лекция Штоль В.В.)", "type": "лекция"})
        elif month == 10 and day == 18:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Внешнеполитический процесс современной России(лекция Штоль В.В.)", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Внешнеполитический процесс современной России(лекция Штоль В.В.)", "type": "лекция"})

        if month == 11 and day in [8, 29]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Внешнеполитический процесс современной России(семинар Сафонов А.С.)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Внешнеполитический процесс современной России(семинар Сафонов А.С.)", "type": "семинар"})
        elif month == 12 and day == 20:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Внешнеполитический процесс современной России(семинар Сафонов А.С.)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Внешнеполитический процесс современной России(семинар Сафонов А.С.)", "type": "семинар"})


        if month == 9 and day in [6, 20]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "лекция"})
        elif month == 9 and day == 20:
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "лекция"})

        elif month == 10 and day == 11:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "лекция"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "лекция"})
        elif month == 10 and day == 25:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "семинар"})

        elif month == 11 and day in [1, 22]:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "семинар"})
        elif month == 12 and day == 13:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.)", "type": "семинар"})

        if month == 10 and day == 4:
            schedule.append({"number": 7, "time": "19:00-20:20", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "семинар"})
            schedule.append({"number": 8, "time": "20:40-22:00", "name": "Актуальные проблемы мировой политики (Жильцов С.С)", "type": "лекция"})


    elif weekday == 5:  # Суббота
        if month == 10 and day == 12:
            schedule.append({"number": 3, "time": "12:55-14:15", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "лекция"})
            schedule.append({"number": 4, "time": "14:30-15:50", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "лекция"})
        elif month == 10 and day == 26:
            schedule.append({"number": 3, "time": "12:55-14:15", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "семинар"})
            schedule.append({"number": 4, "time": "14:30-15:50", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "семинар"})

        elif month == 11 and day == 9:
            schedule.append({"number": 3, "time": "12:55-14:15", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "лекция"})
            schedule.append({"number": 4, "time": "14:30-15:50", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "лекция"})
        elif month == 11 and day in [16, 30]:
            schedule.append({"number": 3, "time": "12:55-14:15", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "семинар"})
            schedule.append({"number": 4, "time": "14:30-15:50", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "семинар"})
        elif month == 11 and day == 30:
            schedule.append({"number": 5, "time": "16:00-17:20", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "лекция"})

        elif month == 12 and day == 14:
            schedule.append({"number": 3, "time": "12:55-14:15", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "семинар"})
            schedule.append({"number": 4, "time": "14:30-15:50", "name": "Региональные подсистемы и международные организации. (Тимакова О.А.)", "type": "семинар"})

    return schedule

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Привет! Я бот, который показывает расписание. \n"
                        "Доступные команды: \n"
                        "/day - расписание на сегодня \n"
                        "/tomorrow - расписание на завтра \n"
                        "/week - расписание на эту неделю \n"
                        "/nweek - расписание на следующую неделю")

@bot.message_handler(commands=['day', 'tomorrow', 'week', 'nweek'])
def send_schedule(message):
    now = datetime.datetime.now()
    command = message.text[1:]  # Убираем '/' из команды

    if command == "day":
        month = now.month
        day = now.day
        weekday = now.weekday()
        schedule = get_schedule(month, day, weekday)
        response = "Расписание на сегодня:\n"

    elif command == "tomorrow":
        tomorrow = now + datetime.timedelta(days=1)
        month = tomorrow.month
        day = tomorrow.day
        weekday = tomorrow.weekday()
        schedule = get_schedule(month, day, weekday)
        response = "Расписание на завтра:\n"

    elif command == "week":
        start_date = now - datetime.timedelta(days=now.weekday())
        response = "Расписание на эту неделю:\n"
        for i in range(7):
            current_date = start_date + datetime.timedelta(days=i)
            month = current_date.month
            day = current_date.day
            weekday = current_date.weekday()
            schedule = get_schedule(month, day, weekday)
            response += f"\n{current_date.strftime('%Y-%m-%d')} ({current_date.strftime('%A')}):\n"
            if schedule:
                for lesson in schedule:
                    response += f"{lesson['number']}/{lesson['time']}/{lesson['name']}/{lesson['type']}\n"
            else:
                response += "Нет пар.\n"
        bot.reply_to(message, response)
        return

    elif command == "nweek":
        start_date = now + datetime.timedelta(days=(7 - now.weekday()))
        response = "Расписание на следующую неделю:\n"
        for i in range(7):
            current_date = start_date + datetime.timedelta(days=i)
            month = current_date.month
            day = current_date.day
            weekday = current_date.weekday()
            schedule = get_schedule(month, day, weekday)
            response += f"\n{current_date.strftime('%Y-%m-%d')} ({current_date.strftime('%A')}):\n"
            if schedule:
                for lesson in schedule:
                    response += f"{lesson['number']}/{lesson['time']}/{lesson['name']}/{lesson['type']}\n"
            else:
                response += "Нет пар.\n"
        bot.reply_to(message, response)
        return

    else:
        bot.reply_to(message, "Неверная команда.")
        return


    if schedule:
        for lesson in schedule:
            response += f"{lesson['number']}/{lesson['time']}/{lesson['name']}/{lesson['type']}\n"
    else:
        response += "Нет пар.\n"

    bot.reply_to(message, response)

keep_alive()
bot.polling(non_stop=True, interval=0)
