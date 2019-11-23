# tompi2

# TomPi
Software developed for MQ sensors etc and a raspberry pi controlled by telegram app

# how to use:
install autossh:
  sudo apt-get install autossh
  sudo apt-get install screen
  
  pip install influxdb
  pip install telegram
  pip install pyjokes
  
write into crontab:
 crontab -e
 @reboot /bin/bash /home/pi/TomStuff/tompi2/autoreverse_ssh.sh
 


Install motioneye
    sudo apt-get install motion
    wget https://github.com/ccrisan/motioneye/wiki/precompiled/ffmpeg_3.1.1-1_armhf.deb
    dpkg -i ffmpeg_3.1.1-1_armhf.deb
    apt-get install python-pip python-dev curl libssl-dev libcurl4-openssl-dev libjpeg-dev libx264-142 libavcodec56 libavformat56 libmysqlclient18 libswscale3 libpq5
    pip install motioneye
    mkdir -p /etc/motioneye cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf
    mkdir -p /var/lib/motioneye
    cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service systemctl daemon-reload
    systemctl enable motioneye systemctl start motioneye 
Install Adafruits
    curl https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/master/scripts/install.sh | sudo sh
Install Dropboxuploader
    https://github.com/andreafabrizi/Dropbox-Uploader.git
Install required python libaries

Install grafana
  #wget https://github.com/fg2it/grafana-on-raspberry/releases/download/v5.1.4/grafana_5.1.4_armhf.deb
  #sudo dpkg -i grafana_5.1.4_armhf.deb
  
  wget https://dl.grafana.com/oss/release/grafana_6.4.4_armhf.deb
  sudo dpkg -i grafana_6.4.4_armhf.deb

  sudo systemctl enable grafana-server 
  sudo systemctl start grafana-server
  
  <embed src="http://130.92.139.28:8081/" width="800" height="600" type="image/jpeg"></embed>

Install influxdb
  curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
  echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
  sudo apt update
  sudo apt install influxdb  
  sudo systemctl enable influxdb
  sudo systemctl start influxdb 
  influx

# Telegram:
Install telegram bot
    pip install python-telegram-bot


Stecker:
https://ch.farnell.com/fischer-elektronik/sl11-smd-062-40z/stiftleiste-smd-2x-20pol-2-54mm/dp/9729054?st=20%20SL%2011%20SMD%20062

restart spidev:
cd
dtc -I dtb -O dts -o /tmp/ads7846.dts /boot/overlays/ads7846.dtbo
//ls
nano /tmp/ads7846.dts //set all disabeld to okay...
rm /boot/overlays/ads7846.dtbo
sudo rm /boot/overlays/ads7846.dtbo
dtc -I dts -O dtb -o /boot/overlays/ads7846.dtbo /tmp/ads7846.dts
sudo dtc -I dts -O dtb -o /boot/overlays/ads7846.dtbo /tmp/ads7846.dts
sudo reboot 0
