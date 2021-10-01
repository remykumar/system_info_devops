[sysadm@lou-l-smtbr-p01 system_info]$ cat rwd_build.sh
#!/bin/bash

PID=`pgrep -f rwd_systeminfo.py`
if [ -z $PID ]; then
 nohup ./rwd_systeminfo.py 2>/dev/null &
else
 exit
fi

echo -n "Building the code ."
for i in {1..4}
do
sleep 2
echo -n .
done

echo "Build Complete!"
echo "-------------------------------------------------------------------------"
sleep 3

echo -n "Deploying the code on the http server ."
for i in {1..4}
do
sleep 2
echo -n .
done

echo "Deploy Complete!"
sleep 2
echo ""
echo "Please access the System Stats page here : "
echo http://`hostname -I | awk '{print $1}'`/rwd_system.html
#cp rwd_system.html /var/www/html/
