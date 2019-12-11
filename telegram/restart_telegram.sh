#!/bin/bash

if pgrep -f "python get_update.py" &>/dev/null; then
    echo "Telegram Bot is already running"
    exit
elif pgrep -f "SCREEN -d -m -S telegram bash -c python /home/pi/TomStuff/tompi2/telegram/get_update.py" &>/dev/null; then
    echo "Telegram Bot is already running"
    exit
else
    echo "Restart telegram bot!"
    screen -X -S telegram kill
    screen -d -m -S telegram bash -c 'python /home/pi/TomStuff/tompi2/telegram/get_update.py'
fi
