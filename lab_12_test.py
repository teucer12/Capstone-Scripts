#This script will check the ITC2480 lab 12
import os, subprocess

#Variables used for telling the user what is installed nan not installed at the end of the script
Zabbix_server_installed = False
Zabbix_frontend_installed = False
Zabbix_conf_exists = False
print("-" * 45)

#counts completion of tasks scored
def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 3 tasks for this lab!")
    if done == 3:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)

done = 0

#check to see if packages are installed
Zabbix_server_installed = subprocess.run("apt list zabbix-server-mysql", capture_output=True, text=True, shell=True)
if "zabbix-server-mysql" in Zabbix_server_installed.stdout:
    print("Good work. You have installed Zabbix Server!")
    done = done + 1
    Zabbix_server_installed = True
else:
    print("Zabbix Server is not installed.")

Zabbix_frontend_installed = subprocess.run("apt list zabbix-frontend-php", capture_output=True, text=True, shell=True)
if "zabbix-frontend-php" and "[installed]" or "upgradable" in Zabbix_frontend_installed.stdout:
    print("Good work. You have installed Zabbix Frontend!")
    done = done + 1
    Zabbix_frontend_installed = True
else:
    print("Zabbix frontend is not installed.")

#Verify zabbix.conf.php exists
Zabbix_conf_exists = os.path.exists('/etc/zabbix/zabbix_server.conf')
if Zabbix_conf_exists == True:
    print("Good work. Your zabbix.conf.php file exists!")
    done = done + 1
    Zabbix_conf_exists = True
else:
    print("Your zabbix.conf.php appears to be missing, are you able to log in to Zabbix?")

completion()
