import requests, re , colorama ,random
from colorama import Fore, Back, Style
from requests.structures import CaseInsensitiveDict
colorama.init()
import os

url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


resp = requests.get(url, headers=headers)

data = resp.json()
countries = data['countries']
os.system("cls")
print(Fore.LIGHTGREEN_EX +"""
╔═╗╔═╗╔╦╗  ╔╦╗╦ ╦╔╦╗╔═╗╔═╗╦═╗
║  ╠═╣║║║───║║║ ║║║║╠═╝║╣ ╠╦╝
╚═╝╩ ╩╩ ╩  ═╩╝╚═╝╩ ╩╩  ╚═╝╩╚═
\033[1;37m+-----------------------------+
| \033[1;31m[#] \033[1;37mDeveloper : Erfan Noori |
| \033[1;31m[#] \033[1;37mInstagram : @n.erfvn    |                                 
| \033[1;31m[#] \033[1;37mTelegram : @Radar_db    |
| \033[1;31m[#] \033[1;37mVersion : 1.0.1         |
+-----------------------------+                         
""")


for key, value in countries.items():
    print(f""" \033[1;30m[+] \033[1;37mCountry : {value["country"]}
 \033[1;30m[+] \033[1;37mCountry Code : ({key})
 \033[1;30m[+] \033[1;37mOnline Camera\033[1;37m(\033[1;32m{value["count"]}\033[1;37m)
 +-----------------------------------+""")
    print("")



try:
   

    country = input(" Enter the Country Code : ")
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        with open(f'{country}.txt', 'w') as f:
          for ip in find_ip:
              print("")
              print("\033[1;30m[+] \033[1;37m", ip)
              f.write(f'{ip}\n')
except:
    pass
finally:
    print("\033[1;37m")
    print('\033[37mSave File : '+country+'.txt')

    exit()
