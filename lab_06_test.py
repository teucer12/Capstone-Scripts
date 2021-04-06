import requests, subprocess, os.path

def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 3 tasks for this lab!")
    if done == 3:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)
    else:
        print("-" * 45)


done = 0
total = 3

def requesting(ipaddress):
    try:
        r=requests.get(ipaddress)
        r2 = r.text
        r3 = (r2[r2.find("<title>") + 7: r2.find("</title>")])
        return r3
    except(requests.exceptions.ConnectionError):
        pass


print("------------------------------------------")

#get IP address of machine
IPfull = subprocess.run("ip address show", capture_output=True, text=True, shell=True)
IP = IPfull.stdout[IPfull.stdout.find("inet 172.17.50.") +15: IPfull.stdout.find("/24")]
ipadd = "172.17.50."+IP
# print (ipadd)

#Test Wordpress
wordpress_title = requesting("http://"+ipadd+"/blog")
if wordpress_title == None:
    print("No blog was found at "+ipadd+"/blog")
else:
    #print(wordpress_title)
    print('A blog with title "'+wordpress_title+'" was found')
    done = done + 1

#Test MyBB
mybb_title = requesting("http://"+ipadd+"/forum")
if mybb_title == None:
    print("No forum was found at "+ipadd+"/forum")
else:
    #print(mybb_title)
    print('A forum with title "'+mybb_title+'" was found')
    done = done + 1

#Test RSS
if os.path.exists("/var/www/html/rss.html"):
    print("Your RSS reader was found")
    done = done + 1
else:
    print("Your RSS feed reader was not found at /var/www/html/rss.html")

completion()