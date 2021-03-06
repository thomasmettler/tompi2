#!/bin/bash

OUTPUT_FILE=ips.txt
# Grab this server's public IP address
#PUBLIC_IP=`curl -s https://ipinfo.io/ip`
current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
ouput_ips="`sudo arp-scan --localnet --retry=3 | grep [a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]`"

#echo "Date: ${current_date_time}\nIP: ${ouput_ips}\n" | tr --delete \"
echo "Date: ${current_date_time}"

echo "${ouput_ips}" | \
    tr --delete \" > \
    ${OUTPUT_FILE}
    
while read a b  c; do 
        echo "IP: "$a" MAC: "$b" System: "$c
        #echo $b
        if [ "$b" == "5c:c3:07:ed:bf:2e" ]; then
          echo "Found you!"
          curl -i -XPOST 'localhost:8086/write?db=mydb' --data-binary "iplogger,host=\"${a}\",mac=\"${b}\" system="\"${c}\" --silent --output /dev/null
        fi
        #echo "MAC: "$b
        #echo "System: "$c
done < ${OUTPUT_FILE}
#echo $last
