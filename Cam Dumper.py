import requests, re, colorama
from colorama import Fore, Back, Style
from requests.structures import CaseInsensitiveDict
import os

colorama.init()

def get_geolocation(ip):
    api_url = f"http://ip-api.com/json/{ip}"
    response = requests.get(api_url)
    data = response.json()

    if data['status'] == 'success':
        city = data.get('city', 'Unknown')
        state = data.get('regionName', 'Unknown')
        country = data.get('country', 'Unknown')
    else:
        city = state = country = 'Unknown'

    return city, state, country

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

os.system("cls" if os.name == "nt" else "clear")

print(Fore.LIGHTGREEN_EX + """
╔═╗╔═╗╔╦╗  ╔╦╗╦ ╦╔╦╗╔═╗╔═╗╦═╗
║  ╠═╣║║║───║║║ ║║║║╠═╝║╣ ╠╦╝
╚═╝╩ ╩╩ ╩  ═╩╝╚═╝╩ ╩╩  ╚═╝╩╚═
\033[1;37m+-----------------------------+
| \033[1;31m[#] \033[1;37mDeveloper : Luis Arano  |
| \033[1;31m[#] \033[1;37mOriginal : https://github.com/erfannoori/Cam-Dumper    |
| \033[1;31m[#] \033[1;37mVersion : 1.0.2         |
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
                ip_address = ip.split("//")[1].split(":")[0]  # Extracting IP address
                city, state, country_geo = get_geolocation(ip_address)
                print(f"\033[1;30m[+] \033[1;37m {ip}")
                print(f"    City: {city}, State: {state}, Country: {country_geo}")
                f.write(f'{ip} - City: {city}, State: {state}, Country: {country_geo}\n')
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("\033[1;37m")
    print('\033[37mSave File : '+country+'.txt')
