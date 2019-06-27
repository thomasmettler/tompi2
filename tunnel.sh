screen -d -m -S tunnel bash -c '/bin/bash /home/pi/Tom_Stuff/open_tunnels.sh'
echo "tunnel opened"
sleep 10
screen -X -S tunnel kill
echo "tunnel screen stop"
