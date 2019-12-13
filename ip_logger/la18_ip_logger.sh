#!/bin/sh

OUTPUT_FILE=ips.txt
# Grab this server's public IP address
#PUBLIC_IP=`curl -s https://ipinfo.io/ip`
current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
ouput_ips="`sudo arp-scan --localnet | grep [a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]:[a-z0-9][a-z0-9]`"

echo "Date: ${current_date_time}\nIP: ${ouput_ips}\n" | tr --delete \"

echo "${ouput_ips}" | \
    tr --delete \" > \
    ${OUTPUT_FILE}
    
while read a b  c; do 
        echo "IP: "$a"\tMAC: "$b"\tSystem: "$c
        curl -i -XPOST 'localhost:8086/write?db=test_db' --data-binary "iplogger,host=\"${a}\",mac=\"${b}\" system="\"${c}\" # | tr --delete \) 
        #echo "MAC: "$b
        #echo "System: "$c
done < ${OUTPUT_FILE}
#echo $last