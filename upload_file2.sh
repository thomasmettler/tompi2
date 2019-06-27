

#!/bin/bash

find . -type f -regex '.*/saved/[^/]*\.mp4' -printf '%T@:%p\0' |
  sort -rnz |
  awk -v RS='\0' -F/ '{sub(/[^:]*:/, ""); file = $0; NF--}
                      ++n[$0] <= 10 {print file}'


#for DIR in $1 do
#if [ -d "$DIR"]; then
#    ls -lt "$DIR/*.csv" |grep '^-' |head -n $2
#fi
#done

