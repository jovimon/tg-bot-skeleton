# Telegram bot skeleton

Based on https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py

## Prerrequisites

`$ sudo pip install python-telegram-bot`

## Usage
Just create functions to define what you want to do with the bot, and link it to [commands](https://github.com/jovimon/tg-bot-skeleton/blob/master/skeleton.py#L117) or [messages](https://github.com/jovimon/tg-bot-skeleton/blob/master/skeleton.py#L121).

There are just three example functions: one for the `/start` command, other for the `/help` command and the last one that echoes all incoming messages.

The bot token goes on the config file (see sample attached).

You can also specify on the config file a list of chat ids so the bot only speaks to whoever you decide.
