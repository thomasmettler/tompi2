screen -d -m -S mq2 bash -c 'python /home/pi/Tom_Stuff/MQ2_DAQ.py'
echo "DAQ MQ2 started"
sleep 1
screen -d -m -S mq3 bash -c 'python /home/pi/Tom_Stuff/MQ3_DAQ.py'
echo "DAQ MQ3 started"
sleep 1
screen -d -m -S mq7 bash -c 'python /home/pi/Tom_Stuff/MQ7_DAQ.py'
echo "DAQ MQ7 started"
sleep 1
screen -d -m -S mq8 bash -c 'python /home/pi/Tom_Stuff/MQ8_DAQ.py'
echo "DAQ MQ8 started"
sleep 1
screen -d -m -S mq135 bash -c 'python /home/pi/Tom_Stuff/test.py'
echo "DAQ MQ135 started"
sleep 1
screen -d -m -S para bash -c 'python /home/pi/Tom_Stuff/rasp2.py'
echo "DAQ parameters started"
sleep 1
echo "DAQ started in screen sessions"
