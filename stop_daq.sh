screen -X -S telegram kill
echo "telegram stop"
screen -X -S DAQ kill
echo "MQ DAQ stop"
screen -X -S rasp2 kill
echo "Rasp Stat stop"
screen -X -S temp kill
echo "Temp DAQ stop"
echo "DAQ parameter stop"

