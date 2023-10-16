import requests,sys,os
import random
import string
import time
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
thanh_dep=trang+do+'['+xanh_la+'⟨⟩'+do+'] '+xanh_duong+'➩ Tài Khoản : '+trang
os.system("cls" if os.name == "nt" else "clear")
def banner():
  banner = ("""
    
            \033[1;36m╭─⋞─────────────────────────────────────────────────────╮
            \033[1;31m███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
            \033[1;32m████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
            \033[1;33m██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
            \033[1;34m██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
            \033[1;35m██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
            \033[1;36m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
            \033[1;34m Youtube : \033[1;37mhttps://youtube.com/@NamTool1
            \033[1;34m Nhóm Zalo : \033[1;37mhttps://zalo.me/g/kfmgqm225
            \033[1;34m Facebook   : \033[1;37mhttps://facebook.com/nam.nhn131 
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ 
            \033[1;31m              TOOL REG ACC GARENA V1
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
""")
  
  for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
banner()
def random_string(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))
def run():
    email = random_string(6)
    user = random_string(13)
    cookies = {
        '_ga': 'GA1.1.1387551280.1675945855',
        '_ga_1M7M9L6VPX': 'GS1.1.1679023440.5.0.1679023440.0.0.0',
        'datadome': '27C1Pcv_jCl-KwLPU~D_6BKInqYJXem76NkOLb8rRUHFg3JqTYERXCNoWMATgRGyxujwdCFuhzPcB8tInjY0fQIoxQYAc0F1DQKGD3rpzooj5P9OHOAXNYrLxQn3TqRe',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.1387551280.1675945855; _ga_1M7M9L6VPX=GS1.1.1679023440.5.0.1679023440.0.0.0; datadome=27C1Pcv_jCl-KwLPU~D_6BKInqYJXem76NkOLb8rRUHFg3JqTYERXCNoWMATgRGyxujwdCFuhzPcB8tInjY0fQIoxQYAc0F1DQKGD3rpzooj5P9OHOAXNYrLxQn3TqRe',
        'Origin': 'https://sso.garena.com',
        'Referer': 'https://sso.garena.com/ui/register?locale=vi',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/111.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'x-datadome-clientid': '27C1Pcv_jCl-KwLPU~D_6BKInqYJXem76NkOLb8rRUHFg3JqTYERXCNoWMATgRGyxujwdCFuhzPcB8tInjY0fQIoxQYAc0F1DQKGD3rpzooj5P9OHOAXNYrLxQn3TqRe',
    }

    data = {
        'username': user,
        'email': f'{email}@gmail.com',
        'password': 'c4a38762f9a6d9fd7c3da7e12fc07842bdc0caa73aca9a82c034d37a8cb984215e1b7ff45818b9d18c82e69ef3388e24e8398d46de666e1d6fd3791a1f71fa2084cb544bad3639fa7f6c7445cf29e10c75b4b3d8b6b1a50267026df70ca4a879e3958800ab5fa8589efa649bdd89beae993a06b10f874df322e8f18c041bdc20',
        'location': 'VI',
        'redirect_uri': '',
        'locale': 'vi',
        'mobile_no': '',
        'otp': '',
        'format': 'json',
        'id': '1692419939745',
    }

    response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data).json()
    #print(response)
    check = response['username']
    if check == user:
        print(thanh_dep +user+"  \033[1;32m| Mật Khẩu: \033[1;37mNam@2007  \033[1;32m| \033[0;31mĐã lưu Vào File garena.txt")
        with open("garena.txt", "a+", encoding="utf-8") as f:
            f.write(user+" | Nam@2007"+"\n")
while True:
    try:
        run()
    except:
        print("\033[0;31mLỗi xảy ra, đang thử lại...")
        time.sleep(5)
        continue
    time.sleep(10)