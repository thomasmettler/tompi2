#!/bin/sh

OUTPUT_FILE=server_location.txt
# Grab this server's public IP address
PUBLIC_IP=`curl -s https://ipinfo.io/ip`
current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
# Call the geolocation API and capture the output
curl -s https://ipvigilante.com/${PUBLIC_IP} | \
        jq '.data.latitude, .data.longitude, .data.city_name, .data.country_name' | \
        while read -r LATITUDE; do
                read -r LONGITUDE
                read -r CITY
                read -r COUNTRY
                echo "Date: ${current_date_time}\nCoordinates: ${LATITUDE},${LONGITUDE}\nCity: ${CITY}\nCountry: ${COUNTRY}\n" | \
                        tr --delete \" > \
                        ${OUTPUT_FILE}
                #lat = `awk ${LATITUDE}`
                #CITY2="test"
                #[ $CITY=="null" ] && CITY2=unknown || CITY2=$CITY
                #curl -i -XPOST "localhost:8086/write?db=mydb" --data-binary "IP_location,host=1 latitude=${LATITUDE},longitude=${LONGITUDE},country=${COUNTRY}" | tr --delete \" | tr --delete \\ # --silent --output /dev/null
                curl -i -XPOST "localhost:8086/write?db=test_db" --data-binary "IP_location,city=${CITY} latitude=${LATITUDE},longitude=${LONGITUDE},country=${COUNTRY}" | tr --delete \" | tr --delete \\ # --silent --output /dev/null
                echo "Date: ${current_date_time}\nCoordinates: ${LATITUDE},${LONGITUDE}\nCity: ${CITY}\nCountry: ${COUNTRY}\n" | tr --delete \"
        done