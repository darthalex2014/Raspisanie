import os
import telebot
import time
import datetime

# Получаем токен бота из переменных окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if BOT_TOKEN is None:
    print("Ошибка: переменная окружения BOT_TOKEN не установлена.")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

def get_schedule(month, day, weekday):
    schedule = []

    if weekday == 0:  # Понедельник
        if month == 9 and day in [2, 9, 16, 23, 30]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })
        elif month == 10 and day in [7, 14, 21, 28]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })
        elif month == 11 and day in [11, 18, 25]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })
        elif month == 12 and day in [2, 9, 16, 23]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })

    elif weekday == 1:  # Вторник
        if month == 10 and day == 8:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "лекция"
            })
        elif month == 10 and day == 29:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "семинар"
            })
        elif month == 11 and day == 19:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "лекция"
            })
        elif month == 12 and day == 10:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Современные информационно-коммуникационные технологии и стратегическое управление",
                "type": "семинар"
            })

        if month == 9 and day == 17:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Основные тенденции мирового развития",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Основные тенденции мирового развития",
                "type": "лекция"
            })
        elif month == 10 and day == 1:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Основные тенденции мирового развития",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Основные тенденции мирового развития",
                "type": "лекция"
            })
        elif month == 10 and day == 22:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Основные тенденции мирового развития",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Основные тенденции мирового развития",
                "type": "семинар"
            })
        elif month == 11 and day == 12:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Основные тенденции мирового развития",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Основные тенденции мирового развития",
                "type": "семинар"
            })
        elif month == 12 and day == 3:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Основные тенденции мирового развития",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Основные тенденции мирового развития",
                "type": "семинар"
            })

        if month == 9 and day == 10:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "лекция"
            })
        elif month == 9 and day == 24:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "лекция"
            })

        elif month == 10 and day == 15:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "семинар"
            })

        elif month == 11 and day == 26:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "лекция"
            })
        elif month == 11 and day == 5:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "семинар"
            })
        elif month == 12 and day == 17:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Дипломатия: эволюция и современная практика",
                "type": "семинар"
            })

    elif weekday == 2:  # Среда
        if month == 9 and day in [4, 11, 18, 25]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })
        elif month == 10 and day in [2, 9, 16, 23, 30]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })
        elif month == 11 and day in [6, 13, 20, 27]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })
        elif month == 12 and day in [4, 11, 18]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Иностранный язык",
                "type": "пара"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Иностранный язык",
                "type": "пара"
            })

    elif weekday == 3:  # Четверг
        if month == 9 and day == 19:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "лекция"
            })
        elif month == 10 and day in [10, 31]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "лекция"
            })
        elif month == 11 and day == 21:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "семинар"
            })
        elif month == 12 and day == 12:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "семинар"
            })

    elif weekday == 4:  # Пятница
        if month == 9 and day in [13, 27]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Внешнеполитический процесс современной России(лекция Штоль В.В.) 424 каб.",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Внешнеполитический процесс современной России(лекция Штоль В.В.) 424 каб.",
                "type": "лекция"
            })
        elif month == 10 and day == 18:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Внешнеполитический процесс современной России(лекция Штоль В.В.) 424 каб.",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Внешнеполитический процесс современной России(лекция Штоль В.В.) 424 каб.",
                "type": "лекция"
            })

        if month == 11 and day in [8, 29]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Внешнеполитический процесс современной России(семинар Сафонов А.С.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Внешнеполитический процесс современной России(семинар Сафонов А.С.) 478 каб.",
                "type": "семинар"
            })
        elif month == 12 and day == 20:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Внешнеполитический процесс современной России(семинар Сафонов А.С.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Внешнеполитический процесс современной России(семинар Сафонов А.С.) 478 каб.",
                "type": "семинар"
            })

        if month == 9 and day in [6, 20]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "лекция"
            })
        elif month == 9 and day == 20:
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "лекция"
            })

        elif month == 10 and day == 11:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "лекция"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "лекция"
            })
        elif month == 10 and day == 25:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "семинар"
            })

        elif month == 11 and day in [1, 22]:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "семинар"
            })
        elif month == 12 and day == 13:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name":
                "Гуманитарная помощь и гуманитарные проблемы в мировой политике (Борисов А.В.) 478 каб.",
                "type": "семинар"
            })

        if month == 10 and day == 4:
            schedule.append({
                "number": 7,
                "time": "19:00-20:20",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 8,
                "time": "20:40-22:00",
                "name": "Актуальные проблемы мировой политики (Жильцов С.С) 478 каб.",
                "type": "лекция"
            })

    elif weekday == 5:  # Суббота
        if month == 10 and day == 12:
            schedule.append({
                "number": 3,
                "time": "12:55-14:15",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "лекция"
            })
            schedule.append({
                "number": 4,
                "time": "14:30-15:50",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "лекция"
            })
        elif month == 10 and day == 26:
            schedule.append({
                "number": 3,
                "time": "12:55-14:15",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 4,
                "time": "14:30-15:50",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "семинар"
            })

        elif month == 11 and day == 9:
            schedule.append({
                "number": 3,
                "time": "12:55-14:15",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "лекция"
            })
            schedule.append({
                "number": 4,
                "time": "14:30-15:50",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "лекция"
            })
        elif month == 11 and day in [16, 30]:
            schedule.append({
                "number": 3,
                "time": "12:55-14:15",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 4,
                "time": "14:30-15:50",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "семинар"
            })
        elif month == 11 and day == 30:
            schedule.append({
                "number": 5,
                "time": "16:00-17:20",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "лекция"
            })

        elif month == 12 and day == 14:
            schedule.append({
                "number": 3,
                "time": "12:55-14:15",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "семинар"
            })
            schedule.append({
                "number": 4,
                "time": "14:30-15:50",
                "name":
                "Региональные подсистемы и международные организации. (Тимакова О.А.) 478 каб.",
                "type": "семинар"
            })

    return schedule


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Привет! Я бот, который показывает расписание. \n"
        "Доступные команды: \n"
        "/day - расписание на сегодня \n"
        "/tomorrow - расписание на завтра \n"
        "/week - расписание на эту неделю \n"
        "/nweek - расписание на следующую неделю")


@bot.message_handler(commands=['day', 'tomorrow', 'week', 'nweek'])
def send_schedule(message):
    now = datetime.datetime.now()
    command = message.text[1:]  # Убираем '/' из команды

    # Словарь для перевода месяцев на русский
    month_names = {
        1: "Января",
        2: "Февраля",
        3: "Марта",
        4: "Апреля",
        5: "Мая",
        6: "Июня",
        7: "Июля",
        8: "Августа",
        9: "Сентября",
        10: "Октября",
        11: "Ноября",
        12: "Декабря"
    }

    # Словарь для перевода дней недели на русский
    weekday_names = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    if command == "day":
        month = now.month
        day = now.day
        weekday = now.weekday()
        schedule = get_schedule(month, day, weekday)
        response = f"*Расписание на сегодня* ({weekday_names[weekday]}, {day} {month_names[month]}):\n"
        if schedule:
            for lesson in schedule:
                response += f"{lesson['time']}\n"
                response += f"*{lesson['name']}*\n"
                response += f"{lesson['type']}\n"
        else:
            response += "*Нет пар.*\n"
        bot.reply_to(message, response, parse_mode='Markdown')

    elif command == "tomorrow":
        tomorrow = now + datetime.timedelta(days=1)
        month = tomorrow.month
        day = tomorrow.day
        weekday = tomorrow.weekday()
        schedule = get_schedule(month, day, weekday)
        response = f"*Расписание на завтра* ({weekday_names[weekday]}, {day} {month_names[month]}):\n"
        if schedule:
            for lesson in schedule:
                response += f"{lesson['time']}\n"
                response += f"*{lesson['name']}*\n"
                response += f"{lesson['type']}\n"
        else:
            response += "Нет пар.\n"
        bot.reply_to(message, response, parse_mode='Markdown')

    elif command == "week":
        start_date = now - datetime.timedelta(days=now.weekday())
        bot.reply_to(message,
                     "Расписание на эту неделю:")  # Отправляем заголовок
        for i in range(7):
            current_date = start_date + datetime.timedelta(days=i)
            month = current_date.month
            day = current_date.day
            weekday = current_date.weekday()
            schedule = get_schedule(month, day, weekday)
            response = f"*{day} {month_names[month]} ({weekday_names[weekday]}):*\n"  # Формируем сообщение для каждого дня
            if schedule:
                for lesson in schedule:
                    response += f"{lesson['time']}\n"
                    response += f"*{lesson['name']}*\n"
                    response += f"{lesson['type']}\n\n"
            else:
                response += "*Нет пар*\n"
            bot.send_message(
                message.chat.id, response, parse_mode='Markdown'
            )  # Отправляем отдельное сообщение для каждого дня
        return

    elif command == "nweek":
        start_date = now + datetime.timedelta(days=(7 - now.weekday()))
        bot.reply_to(message,
                     "Расписание на следующую неделю:")  # Отправляем заголовок
        for i in range(7):
            current_date = start_date + datetime.timedelta(days=i)
            month = current_date.month
            day = current_date.day
            weekday = current_date.weekday()
            schedule = get_schedule(month, day, weekday)
            response = f"*{day} {month_names[month]} ({weekday_names[weekday]}):*\n"  # Формируем сообщение для каждого дня
            if schedule:
                for lesson in schedule:
                    response += f"{lesson['time']}\n"
                    response += f"*{lesson['name']}*\n"
                    response += f"{lesson['type']}\n\n"
            else:
                response += "Нет пар\n"
            bot.send_message(
                message.chat.id, response, parse_mode='Markdown'
            )  # Отправляем отдельное сообщение для каждого дня
        return

    else:
        bot.reply_to(message, "Неверная команда.")
        return

bot.polling(non_stop=True, interval=0)
