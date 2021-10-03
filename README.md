# system_info_devops
Project/code to get some critical system configuration and real time monitoring data

**Code 2: Reference Software (python code)**

Source code link: https://github.com/remykumar/system_info_devops

Reference Software here is a python code (script) which will pull some key system information & monitoring data (CPU usage, Memory usage & disk usage) from the Host Operating System and creates a html page. This html file can be deployed on a web server (http server) to be viewed on a browser. The python code runs continuously every 60 seconds and updates the html – so the system info (or monitoring) page is dynamically updated. 

**Execution instruction for Reference Software:**
1. This code is cloned by the Build script (https://github.com/remykumar/build_system_info) and used for its execution steps. 
Directly running it would result in some errors due to missing supporting software (like http server, python3 ..etc) 

You can still clone it for your reference, using, 
git clone https://github.com/remykumar/build_system_info.git


**Some tasks done by the Reference Software (python code):** 
-	Gets the operating system type and distro
-	Gets the Hostname and Internal/External Ips
-	Gets the Number of CPUs, CPU usage
-	Gets the Memory (RAM) allocated, Memory usage
-	Gets the swap space size and swap space used 
-	Gets the Disk / Filesystem details  
-	Gets the current system time – to know when the last set of monitoring data was polled
-	Creates a html with all the above data 
-	Copies the file to the http server's root folder
-	Code does continuous looping every 60 seconds to collect system statistics & updates the html

