from datetime import datetime as dt
import time

hosts_temp=r"C:\Users\India\PycharmProjects\untitled\hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect ="192.168.0.19"
websites=["www.facebook.com","facebook.com"]
now=dt.now()

while True:
#    if 8 <= dt.now().hour <= 16 :
    if dt(now.year,now.month,now.day,8) < now < dt(now.year,now.month,now.day,10):
        with open(hosts_path , "r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write( redirect + " " + website + "\n")
        print("Working hours")

    else:
        with open(hosts_path , "r+") as file:
            content=file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in websites):

                    file.write(line)

            file.truncate()
        print("Fun hours ")

    time.sleep(5)