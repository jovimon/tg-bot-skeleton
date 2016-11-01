#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Telegram bot skeleton, developed by @jovimon
# 
# based on https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
# 
# Prerrequisites: 
# $ sudo pip install python-telegram-bot
# $ sudo pip install python-daemon
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

__author__ = '@jovimon'
__version__ = 0.1


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import bot
import logging
import ConfigParser
import sys
import json

# Strip the script name
my_name = sys.argv[0].split('.')[0]

# Default config file to be used
cfg_file = my_name + '.cfg'

# Authorized chat IDs. Loaded from config file
chat_id = []

# Create file logger
logger = logging.getLogger("DaemonLog")

def start(bot, update):
    bot_chat_id = update.message.chat.id
    if chat_id != [] and bot_chat_id not in chat_id:
        logger.warning("Unauthorized access from %d detected !" % bot_chat_id)
        logger.warning(update)
    else:
        message = """
        Welcome to %s Telegram bot.
        """ % (my_name)
        update.message.reply_text(message)

def help(bot, update):
    bot_chat_id = update.message.chat.id
    if chat_id != [] and bot_chat_id not in chat_id:
        logger.warning("Unauthorized access from %d detected !" % bot_chat_id)
        logger.warning(update)
    else:
        message = """
        %s Telegram bot Help.

        blah blah blah
        """ % (my_name)
        update.message.reply_text(message)

def echo(bot, update):
    bot_chat_id = update.message.chat.id
    if chat_id != [] and bot_chat_id not in chat_id:
        logger.warning("Unauthorized access from %d detected !" % bot_chat_id)
        logger.warning(update)
    else:
        update.message.reply_text(update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    global chat_id
    # Read config file
    config = ConfigParser.ConfigParser()
    config.read(cfg_file)

    # Load config options
    logfile = config.get('Log','logfile')
    loglevel = config.getint('Log','loglevel')

    logger.setLevel(loglevel)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(module)s - %(message)s")
    handler = logging.FileHandler(logfile)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.warning("Starting %s Telegram Bot", my_name)

    bot_token = config.get('Bot','token')

    # Warn if no chat_id configured
    if config.has_option('Bot','chat_id'):
        chat_id = json.loads(config.get("Bot","chat_id"))
        logger.info('chat_id found. Only updates from your chat_id will be taken care of.')
    else:
        logger.info('chat_id not found. Anyone can interact with your chat. Proceed with caution.')

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()