#screen -d -m -S telegram bash -c 'python /home/pi/TomStuff/tompi2/telegram/get_update.py'
#echo "telegram bot started"
#sleep 1
#screen -d -m -S DAQ bash -c 'python /home/pi/TomStuff/tompi2/DAQ/MQ_DAQ.py'
#echo "DAQ MQ started"
#sleep 1
screen -d -m -S rasp2 bash -c 'python /home/pi/Tom_Stuff/tompi2/DAQ/rasp2.py'
echo "Rasp Stat started"
#sleep 1
#screen -d -m -S temp bash -c 'sudo pigpiod && /bin/bash /home/pi/TomStuff/tompi2/DAQ/temp_daq/DHTXXD -g17 -i5'
#echo "Temp DAQ started"
#sleep 1
#echo "DAQ started in screen sessions"
