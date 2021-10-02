# system_info_devops
Project/code to get some critical system configuration and real time monitoring data

**Code 2: Reference Software**

Source code link: https://github.com/remykumar/system_info_devops

Reference Software here is a python code (script) which pull some key system information & monitoring data (CPU usage, Memory usage & disk usage) from the Host Operating System 
and creates a html page. This html file can be deployed on a web server (http server) to be viewed on a browser. 
The python code runs continuously every 60 seconds and updates the html – so the system info (or monitoring) page dynamically is updated. 

**Execution instruction for Reference Software:**
1. This code is cloned by the Build script (https://github.com/remykumar/build_system_info) and used for it’s execution steps. 
Directly running it would result in some errors due to missing supporting software (like http server, python3 ..etc) 

You can still clone it for your reference, using, 
git clone https://github.com/remykumar/build_system_info.git
