#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from datetime import datetime


def get_time_till_next_session():
    game_time = datetime.strptime('2021-03-13 18:00:00', '%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    result = {"passed": True}
    if now < game_time:
        td = game_time - now
        result["days"] = td.days
        result["hours"], remainder = divmod(td.seconds, 3600)
        result["minutes"], result["seconds"] = divmod(remainder, 60)
        result["passed"] = False
    return result


def when(update, context):
    result = get_time_till_next_session()
    if not result["passed"]:
        message = "עוד "
        if result["days"]:
            message += "{} ימים, ".format(result["days"])
            message = message.replace(" 2 ימים", " יומיים").replace(" 1 ימים", " יום")
        if result["hours"]:
            message += "{} שעות, ".format(result["hours"])
            message = message.replace(" 2 שעות", " שעתיים").replace(" 1 שעות", " שעה")
        if result["minutes"]:
            message += "{} דקות ".format(result["minutes"])
            message = message.replace(" 1 דקות", " דקה")
        if result["seconds"]:
            message += "ו {} שניות, ".format(result["seconds"])
            message = message.replace(" 1 שניות", " שניה")
        message += "אבל מי סופר?"
        if result["seconds"] and not result["minutes"] and not result["hours"] and not result["days"]:
            message = "וואי וואי משחקים רק עוד {} שניות!! תיכנסו לדיסקורד ולרול20 כבר".format(result["seconds"])
    else:
        message = "אללה המשחק היה אמור להתחיל כבר מה אתם שולחים לי הודעות? לכו לדיסקורד!"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def hype(update, context):
    result = get_time_till_next_session()
    if not result["passed"]:
        if result["days"] < 1:
            if not result["hours"]:
                message = "עוד פחות משעה הייפ הייפ הייפ הייפ הייפ הייפ"
            else:
                message = "עוד פחות מיום!! הייפ!! @hasovel יש הייפפפפפפפ אבייייייייי"
        elif result["days"] < 7:
            message = "עוד פחות משבוע!! הייפ!! @hasovel אבי יש הייפ"
        else:
            message = "יש עוד מלא זמן אני לא בהייפ בכלל :("
    else:
        message = "יש דיאנדי יש דיאנדי יש דיאנדי יש דיאנדי יש דיאנדי הייפ הייפ הייפ הייפ"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def ze_ata(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="It's you, Avi!")


def pump(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="מי שלא ידע שמחת בית השואבה לא ידע שמחה מימיו")


def juice(update, context):
    picture = 'https://media.discordapp.net/attachments/762255884554076171/779774450710216734/unknown.png'
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=picture)


updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
when_handler = CommandHandler('when', when)
hype_handler = CommandHandler('hype', hype)
avi_handler = CommandHandler('omermankal', ze_ata)
pump_handler = CommandHandler('pump', pump)
juice_handler = CommandHandler('juice', juice)

dispatcher.add_handler(when_handler)
dispatcher.add_handler(hype_handler)
dispatcher.add_handler(avi_handler)
dispatcher.add_handler(pump_handler)
dispatcher.add_handler(juice_handler)

updater.start_polling()
