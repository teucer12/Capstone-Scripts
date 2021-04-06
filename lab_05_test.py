# This script will check ITC2480 Lab 5 for successful completion
import subprocess
import os
import os.path
import requests

#variables used for telling the user what is installed and not installed at the end of script
Ip_set = False
Index_file_exists = False
Apache_port_open = False
Logtail_file_exists  = False
Php_installed = False
Mariadb_installed = False
Php_mysql_installed = False
print("-" * 45)

# Auto grab username of currently logged in user to prevent input needed
who_output = subprocess.run("who", capture_output=True, text=True, shell=True)
who_split = who_output.stdout.split()
username = str(who_split[0])

#Get IP address
IPfull = subprocess.run("ip address show", capture_output=True, text=True, shell=True)
IP = IPfull.stdout[IPfull.stdout.find("inet 172.17.50.") +15: IPfull.stdout.find("/24")]
ipadd = "172.17.50."+IP
# print (ipadd)
print ("Verify that your assigned IP address is:", ipadd)

#counts completion of tasks scored
def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 8 tasks for this lab!")
    if done == 8:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)
done = 0
print("-" * 45)

#Check if ip address responds to icmp requests "ping"
hostname = ipadd
response = subprocess.run("ping -c 1 " + "172.17.50.28", capture_output=True, text=True, shell=True)
if "1 received" in response.stdout:
   pingstatus = "Good work. Your Server is responding to ping requests at your assigned IP!"
   done = done + 1
   Ip_set = True
else:
    pingstatus = "Try Again! Network Error - Your Server is not responding to ping requests"
print(pingstatus)

#Request information from index.html file to verify custom link page
Index_file = os.path.exists('/var/www/html/index.html')
if Index_file == True:
    print("Good work. Your index.html file has been created!")
    done = done + 1
    Index_file_exists = True
else:
    print("Your index.file appears to be missing, are you able to visit your server page in a browser?")

#Check for open Port 80 (Apache)
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
if "80/tcp" in scan.stdout:
    print("Good work. Port 80 has been opened to allow access to your web page and Apache Server!")
    done = done + 1
    Apache_port_open = True
else:
    print("Apache is not functional")

#Check for employees.sql file to verify the tarball was extracted
Employees_sql_file = os.path.exists('/home/'+username+'/employees_db/employees.sql')
if Employees_sql_file == True:
    print("Good work. Your sample database was extracted and the employees.sql exists!")
    done = done + 1
    Index_file_exists = True
else:
    print("Your employees.sql file appears to be missing, did you experiment with MySQL files?")

#check for tail redirection file
Logtail_file = os.path.isfile('/home/'+username+'/logtail.txt')
if Logtail_file == True:
    print("Good work. You have created a logtail.txt file in your home directory!")
    done = done + 1
    Logtail_file_exists = True
else:
    print('Try Again. There is no logfile.txt file in your home directory.')

#check to see if PHP, MySQL, MariaDB packages are installed
php_version = subprocess.run("apt list php", capture_output=True, text=True, shell=True)
if "php" and "[installed]" in php_version.stdout:
    print("Good work. You have installed PHP!")
    done = done + 1
    Php_installed = True
else:
    print("You have NOT installed any version of PHP.")

#check for Mariadb
mariadb_version = subprocess.run("apt list php", capture_output=True, text=True, shell=True)
if "mariadb" and "[installed]" in mariadb_version.stdout:
    print("Good work. You have installed Mariadb or MySQL!")
    done = done + 1
    Mariadb_installed = True
else:
    print("You have NOT installed Mariadb or MySQL.")

#check for php-mysql
php_mysql_version = subprocess.run("apt list php", capture_output=True, text=True, shell=True)
if "php-mysql" and "[installed]" in php_mysql_version.stdout:
    print("Good work. You have installed PHP-MySQL!")
    done = done + 1
    Php_mysql_installed = True
else:
    print("You have NOT installed PHP-MySQL.")

completion()







