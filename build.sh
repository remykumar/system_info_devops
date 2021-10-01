#!/bin/bash

INT_IP=`hostname -I | awk '{print $1}'`
EXT_IP=`curl -s api.ipify.org`


echo -en "\nBuilding the code ."
PID=`pgrep -f sysinfo.py`
if [ -z $PID ]; then
 nohup ./sysinfo.py 2>/dev/null &
else
 kill -9 $PID
 nohup ./sysinfo.py 2>/dev/null &
fi

for i in {1..4}
do
sleep 2
echo -n .
done

echo "Build Complete!"
echo "-------------------------------------------------------------------------"
sleep 3

echo -en "\nDeploying the code on the http server ."
FINAL_URL=""
RESP=`curl -s -I http://$EXT_IP/systeminfo.html --connect-timeout 3 | grep HTTP | grep OK`

if [[ -z $RESP ]]; then
 RESP=`curl -s -I http://$INT_IP/systeminfo.html --connect-timeout 3 | grep HTTP | grep OK`
 if [[ -z $RESP ]]; then
  echo -e "\n!!! Deploy not successful - Site not reachable!!!!. \nPossible reasons could be :\n
         1. Http server is not running \n
         2. Internet is not working or network issues \n
         3. Firewall blocking port 80 \n"
  exit
 else
 FINAL_URL=http://$INT_IP/systeminfo.html
 fi
else
 FINAL_URL=http://$EXT_IP/systeminfo.html
fi

for i in {1..4}
do
sleep 2
echo -n .
done

echo "Deploy Complete!"
sleep 2
echo -e "-------------------------------------------------------------------------\n"
echo "Please access the System Stats (System Information) page here : "
echo -e "$FINAL_URL\n"