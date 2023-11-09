#!/bin/sh

# parse parameters from query string
eval $(echo ${QUERY_STRING//&/;})

# validate x and y are integers
! [ "$x" -eq "$x" ] && x=0
! [ "$y" -eq "$y" ] && y=0

payload="${x}x${y}"

# run motors
motor -x ${x} -y ${y}

echo "HTTP/1.1 200 OK
Content-type: application/json
Pragma: no-cache
Expires: $(TZ=GMT0 date +'%a, %d %b %Y %T %Z')
Etag: \"$(cat /proc/sys/kernel/random/uuid)\"

${payload}
"
