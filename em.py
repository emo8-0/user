import webbrowser
import getpass
webbrowser.open('https://t.me/mrmbl6')
import os
import requests
import threading
import random
code = 'mortada'
import datetime
now = datetime.datetime.now()
ta = now.year
bu = now.month
ha = now.day
ho = now.hour
hs = now.minute
#############
H = "\x1b[38;5;208m" # 
S = '\x1b[1;33m'   # 
E = '\033[1;31m'  # 
Z = '\033[1;31m'  # 
X = '\033[1;33m'  # 
F = '\033[2;32m'  # 
C = "\033[2;35m"  # 
B = '\033[2;36m'  # 
Y = '\033[1;34m'  # 
M = '\x1b[1;37m'  # 
S = '\033[1;33m'  # 
U = '\x1b[1;37m'  # 
BRed = '\x1b[1;31m'  # 
BGreen = '\x1b[1;32m'  # 
BYellow = '\x1b[1;33m'  # 
BBlue = '\x1b[1;34m'  # 
BPurple = '\x1b[1;35m'  # 
BCyan = '\x1b[1;36m'  # 

try:
 from cfonts import render, say
except:
    os.system('pip install python-cfonts')
output = render('MALAZ',colors=['green','red'], align='center')
print(output)
token = input(f'\033[1;37#m'+"TOKEN : ")
print('\n')
iD = input(f'\033[1;37#m'+"ID : ")
print('\n')
os.system('clear')


def AA(user):
    try:
        headers = {
            "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
        }
        
        response = requests.get(f'https://www.tiktok.com/@{user}', headers=headers)
        tikinfo = response.text
        getting = tikinfo.split('webapp.user-detail"')[1].split('"RecommendUserList"')[0]
        user_id = getting.split('id":"')[1].split('",')[0]
        followers = getting.split('followerCount":')[1].split(',"')[0]
        following = getting.split('followingCount":')[1].split(',"')[0]
        print(f"{Z}BAD : {user}")
        print(f'{X}__'*20)
    except (KeyError, IndexError):
        print(f"{F}Good User : {user}")
        print(f'{X}__'*20)
        tlg = f'''✅ 𝘜𝘚𝘌𝘙  : {user}
BY - @emo_80'''
        requests.post(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={iD}&video=https://t.me/emopvb/2&caption="+str(tlg))
    except requests.exceptions.ConnectionError:
        print("النت ضعيف حاول مجددآ ")

def mortada():
    while True:
        v5 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for _ in range(1))
        v6 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for _ in range(1))
        v7 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for _ in range(1))
        v8 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for _ in range(1))
                  
        X2 = v5 + '_' + v6 + '_' + v7
        mo = v5 + v6 + v7 + v8
        rr = v5 + '.' + v6 + '.' + v8
        xx = v5 + v6 + v8 + v7 + '_'
        PYTHON = [X2,mo,rr,xx]
        user = random.choice(PYTHON)
        AA(user)

Threads = []
for _ in range(2):
    t = threading.Thread(target=mortada)
    t.start()
    Threads.append(t)

for thread in Threads:
    thread.join()
