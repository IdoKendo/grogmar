#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from datetime import datetime


def when(update, context):
    game_time = datetime.strptime('2020-10-17 20:00:00', '%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    if now < game_time:
        td = game_time - now
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        message = "עוד "
        if days:
            message += "{} ימים, ".format(days)
            message = message.replace(" 2 ימים", " יומיים").replace(" 1 ימים", " יום")
        if hours:
            message += "{} שעות, ".format(hours)
            message = message.replace(" 2 שעות", " שעתיים").replace(" 1 שעות", " שעה")
        if minutes:
            message += "{} דקות ".format(minutes)
            message = message.replace(" 1 דקות", " דקה")
        if seconds:
            message += "ו {} שניות, ".format(seconds)
            message = message.replace(" 1 שניות", " שניה")
        message += "אבל מי סופר?"
        if seconds and not minutes and not hours and not days:
            message = "וואי וואי משחקים רק עוד {} שניות!! תיכנסו לדיסקורד ולרול20 כבר".format(seconds)
    else:
        message = "אללה המשחק היה אמור להתחיל כבר מה אתם שולחים לי הודעות? לכו לדיסקורד!"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('when', when)
dispatcher.add_handler(start_handler)

updater.start_polling()
