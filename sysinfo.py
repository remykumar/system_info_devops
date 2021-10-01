#!/usr/bin/env python3

import os
import time

# This code does continuous looping every 60 seconds to collect system statistics
while True:
 # Get the operating system type and distro
 osType = os.popen('uname').read().strip()
 osDistro = os.popen('hostnamectl | grep "Operating" | awk -F ":" \'{print $2}\'').read().strip()

 # Get the Hostname and Internal/External IPs
 hostName = os.popen('hostname').read().strip()
 intIp = os.popen('hostname -I | awk \'{print $1}\'').read().strip()
 extIp = os.popen('curl -s api.ipify.org').read().strip()

 # Get the Number of CPUs, CPU usage
 numCpu = os.popen('nproc').read().strip()
 cpuUse = os.popen('vmstat 1 3 | tail -1 | awk \'{print 100 - $15}\'').read().strip()

 # Get the Memory(RAM)set, Memory usage
 numMem = os.popen('free | grep "Mem:" | awk \'{print $2}\'').read().strip()
 numMem = round(int(numMem)/1000000,0)
 memUse = os.popen('free | grep "Mem:" | awk \'{print $3}\'').read().strip()
 memUse = round(int(memUse)/1000000,0)

 # Get the swapsize and swap used
 swapSize = os.popen('swapon | grep -v NAME | awk \'{print $3}\'').read().strip()
 swapUsed = os.popen('swapon | grep -v NAME | awk \'{print $4}\'').read().strip()

 #diskUsageRoot = os.popen('df -h | awk \'$NF=="/"{printf "Disk Usage: %d/%dGB (%s)\n", $3,$2,$5}\'').read().strip()

 # Get the Disk / Filesystem details & frame a table string for the html page
 diskUsage = os.popen('df -h | egrep \'Filesystem|^/dev\'').read().strip()
 diskUsage = diskUsage.replace("on", "")
 diskUsage = diskUsage.replace("Mounted", "MountedOn")
 diskUsage = diskUsage.replace("Avail", "Available")
 dusage="<table>"
 for line in diskUsage.splitlines():
  #print(line)
  dusage = dusage+"<tr>"
  for word in line.split():
   #print(word)
   dusage = dusage+"<td style=color:dimgray>"+word+"</td>"
  dusage = dusage+"</tr>"
 dusage=dusage+"</table>"
 #print(dusage)

 # Get the current system time
 currTime = os.popen('date').read().strip()

 # This is for debugging
 """
 print(f'Hostname = {hostName}')
 print(f'IP = {intIp}')
 print(f'Ext IP = {extIp}')
 print(f'Number of CPUs = {numCpu}')
 print(f'CPU used  = {cpuUse}')
 print(f'Memory(RAM) allocated  = {numMem}GB')
 print(f'Memory(RAM) use  = {memUse}GB')
 print(f'Swapsize set  = {swapSize}')
 print(f'Swapsize used  = {swapUsed}')
 """

 # Create the system info file and open it for write
 stats_file="systeminfo.html"
 os.system('touch '+stats_file+'')
 outfile = open(stats_file, 'w')

 outfile.write('<html><head><meta http-equiv="refresh" content="60"></head><style>table { width:100%;} table, th, td { border: 1px solid black;} th, td {padding: 9px;text-align: left;} th {background-color: darkred;color: white;}</style><table>')
 outfile.write('<body><p style="text-align:center;"><img src="images\devops3.png" alt="logo"></p>')
 outfile.write("\n")
 outfile.write('<tr><th><h2>Metric/Parameter</h2></th><th><h2>System Info Value</h2></th><th><h2>Current Metric Value/Usage</h2></th></tr>')
 outfile.write("\n")
 outfile.write(f'<tr><td style=color:dimgray><h2>OS / Hostname</h2></td><td style=color:dimgray><h2>{osType} / {hostName}</h2></td><td style=color:darkred><h2>{osDistro} / {hostName}</h2></td></tr>')
 outfile.write("\n")
 outfile.write(f'<tr><td style=color:dimgray><h2>IP (INTERNAL / EXTERNAL)</h2></td><td style=color:dimgray><h2>{intIp} / {extIp}</h2></td><td style=color:darkred><h2>{intIp} / {extIp}</h2></td></tr>')
 outfile.write("\n")
 outfile.write(f'<tr><td style=color:dimgray><h2>CPU</h2></td><td style=color:dimgray><h2>Number of CPUs = {numCpu}</h2></td><td style=color:darkred><h2>CPU Utilization = {cpuUse}%</h2></td></tr>')
 outfile.write("\n")
 outfile.write(f'<tr><td style=color:dimgray><h2>Memory / RAM</h2></td><td style=color:dimgray><h2>Memory Allocated = {numMem}GB</h2></td><td style=color:darkred><h2>Memory Usage = {memUse}GB</h2></td></tr>')
 outfile.write("\n")
 outfile.write(f'<tr><td style=color:dimgray><h2>Swap Space</h2></td><td style=color:dimgray><h2>Swap Allocated = {swapSize}B</h2></td><td style=color:darkred><h2>Swap Usage = {swapUsed}B</h2></td></tr>')
 outfile.write("\n")
 outfile.write(f'</table><h3><p style="color:darkred;"> Disk / Filesystem Usage :<br></p></h3>')
 outfile.write(f'{dusage}')
 outfile.write(f'<h3><p style="color:darkred;">Data last polled @ {currTime}</p></h3><h3><p style="color:dimgray;">Note : Page refreshes every 60 seconds to update latest stats</p></h3></body></html>')
 outfile.close()

 # Copy the file to the http server's root folder
 discard1 = os.popen('sudo cp systeminfo.html /var/www/html/').read()
 discard2 = os.popen('sudo cp devops3.png /var/www/html/images/').read()
 time.sleep(60)
