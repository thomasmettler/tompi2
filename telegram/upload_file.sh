

#!/bin/bash

#find $1 -type d -exec bash -c 'echo "next dir: ${1}" ; ls -lt "$1" |
#    grep ^- |
#    head -n 5' bash {} \;

#for x in $(find $1 -type f -name *.mp4 -printf "%T@ %p\n" |
for x in $(find $1 -type f  -printf "%T@ %p\n" |
    sort -nr |
    awk 'NR=='$2+1' { exit; } {$1=""; print; }')
do
  echo $x
  bash /home/pi/Software/Dropbox-Uploader/dropbox_uploader.sh -s upload $x /Raspi_data/daily_motion
done

#for DIR in $1 do
#if [ -d "$DIR"]; then
#    ls -lt "$DIR/*.csv" |grep '^-' |head -n $2
#fi
#done

#for x in $(find $1 -type f -name *.mp4 | head -n $2);
#do
#  echo $1
#  echo $x
  #bash /home/pi/Dropbox/Dropbox-Uploader/dropbox_uploader.sh -s upload $x /Raspi_data/daily_motion
  #echo $(basename $1)
  #echo $(basename $x)
  
#done
