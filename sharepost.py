from lequangminh import *
import os,sys
import threading
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
import time
from threading import Thread
try:
    import requests
except:
    os.system('pip install requests')
    import requests
dem = 0
list_token = []
def clear():
    os.system("cls" if os.name == "nt" else "clear")
text = """
            ███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
            ████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
            ██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
            ██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
            ██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
            ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
Nhấn Enter Để Tiếp Tục 
"""
Anime.Fade(Center.Center(text), Colors.green_to_white, Colorate.Vertical, enter=True)
os.system("cls" if os.name == "nt" else "clear")
def banner():
 banner = print(f"""
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
            \033[1;31m                TOOL SHARE ẢO BẰNG PROFILE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
""")
banner()
share_lock = threading.Lock()
share_index = 0
completed_shares = 0
def run_share(id_post,token):
    global share_index, completed_shares
    headers = {
        'authority': 'graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5'
    }
    try:
        sharepost = requests.get(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
        with share_lock:
            share_index += 1
            completed_shares += 1
            print(Colorate.Diagonal(Colors.green_to_white,f'[●] {datetime.now().strftime("%H:%M:%S")} | Buff Share Thành Công : {share_index}/{so_luong} [ 🌸Nam ~ Dev🌸 ]'))
            if completed_shares >= so_luong:
                os._exit(0)
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_white,f'[●] {datetime.now().strftime("%H:%M:%S")} : FALSE'))

id_post = input(Colorate.Horizontal(Colors.green_to_white, "[●] Nhập ID Post Cần Buff Share: "))
print(Colorate.Horizontal(Colors.red_to_white, "=========================================================="))
so_luong = int(input(Colorate.Horizontal(Colors.green_to_white, "[●] Nhập Số Lượng Share Cần Chạy: ")))
print(Colorate.Horizontal(Colors.red_to_white, "=========================================================="))
print(Colorate.Horizontal(Colors.green_to_white,"""[1] CHƯA CÓ TOKEN PROFILE
==========================================================
[2] NẾU CÓ SẴN TOKEN PROFILE
"""))
print(Colorate.Horizontal(Colors.red_to_white, "=========================================================="))
mode = int(input(Colorate.Horizontal(Colors.green_to_white, "[●] Chọn Chức Năng: ")))
print(Colorate.Horizontal(Colors.red_to_white, "=========================================================="))
if mode == 1:
    try:
        file =  open('token.txt','r',encoding="utf-8").read().split('\n')
        if len(file) >= 1:
            print(Colorate.Horizontal(Colors.green_to_white,'[●] Tìm Thấy Token Trong File' +{file}+ 'Hãy Chắc Chắn Đây Là Token Acc Mẹ Chứa Page Profile Chứ Không Phải Profile'))
            submit = input(Colorate.Horizontal(Colors.green_to_white, "[●] Dùng Token Trong File Này Chứ ? [Y/N]: "))
            if submit == "Y" or submit =="y":
                print(Colorate.Horizontal(Colors.green_to_white, "[●] Xác Nhận Dùng Token Trong File"+ {file}))
                for get in file:
                    tokenn = requests.get('https://graph.facebook.com/me/accounts?access_token='+get).json()['data']
                    for token in tokenn:
                        token_profile = token['access_token']
                        print(Colorate.Horizontal(Colors.green_to_white,'NAME PROFILE : {token["name"]} | ID PROFILE : {token["id"]}'))
                        write_token = open('token_profile.txt','a+').write(token_profile+'\n')
                open_file = open('token_profile.txt','r+',encoding="utf-8").read().split('\n')
                print(Colorate.Horizontal(Colors.green_to_white,'CÓ {len(open_file)} TOKEN PROFILE TRONG FILE TOKEN_PROFILE.TXT'))

            elif submit == "quit":
                quit()
            else:
                while True:
                    try:
                        file = input(Colorate.Horizontal(Colors.green_to_white,'[●] FILE CHỨA COOKIE : '))
                        if file == "quit":quit()
                        open_file =  open(file,'r',encoding="utf-8").read().split('\n')
                        print(f'[●] CÓ {len(open_file)} COOKIE TRONG FILE')
                        break
                    except:
                        print(Colorate.Horizontal(Colors.green_to_white,f'[●] NHẬP FILE CHỨA VÔ ! '))
                for cookie in open_file:
                    token = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token',headers={'cookie':cookie}).url
                    check_token = token.split('#access_token=')[1].split('&data_access')[0]
                    list_token.append(check_token)
                for get in list_token:
                    tokenn = requests.get('https://graph.facebook.com/me/accounts?access_token='+get).json()['data']
                    for token in tokenn:
                        token_profile = token['access_token']
                        print(Colorate.Horizontal(Colors.green_to_white,f'[●] NAME PROFILE : {token["name"]} | ID PROFILE : {token["id"]}'))
                        write_token = open('token_profile.txt','a+').write(token_profile+'\n')
                open_file = open('token_profile.txt','r+',encoding="utf-8").read().split('\n')
                print(Colorate.Horizontal(Colors.green_to_white,f'[●] Có {len(open_file)} Cookie Profile Trong File TOKEN_PROFILE.TXT'))
    except:
        while True:
            try:
                file = input(Colorate.Horizontal(Colors.green_to_white,'[●] FILE CHỨA COOKIE : '))
                if file == "quit":quit()
                open_file =  open(file,'r',encoding="utf-8").read().split('\n')
                print(Colorate.Horizontal(Colors.green_to_white,f'[●] Có {len(open_file)} Cookie Profile Trong File {file}'))
                break
            except:
                print(Colorate.Horizontal(Colors.green_to_white,f'[●] NHẬP FILE CHỨA VÔ ! '))

        for cookie in open_file:
            token = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token',headers={'cookie':cookie}).url
            check_token = token.split('#access_token=')[1].split('&data_access')[0]
            list_token.append(check_token)

        for get in list_token:
            tokenn = requests.get('https://graph.facebook.com/me/accounts?access_token='+get).json()['data']
            for token in tokenn:
                token_profile = token['access_token']
                print(Colorate.Horizontal(Colors.green_to_white,f'[●] NAME PROFILE : {token["name"]} | ID PROFILE : {token["id"]}'))
                write_token = open('token_profile.txt','a+').write(token_profile+'\n')
        open_file = open('token_profile.txt','r+',encoding="utf-8").read().split('\n')
        print(Colorate.Horizontal(Colors.green_to_white,f'[●] Có {len(open_file)} Token Profile Trong File {file}'))

elif mode == 2:
	file = input(Colorate.Horizontal(Colors.green_to_white,f'[●] File Chứa Token Profile: '))
	open_file = open(file,'r',encoding="utf-8").read().split('\n')
	print(Colorate.Horizontal(Colors.red_to_white,f'[●] Có {len(open_file)} Token Profile Trong File {file}'))

time.sleep(1)
clear()
threads = []
for _ in range(so_luong):
    for i in range(0,+1):
    	for token in open_file:
    		Thread(target=run_share,args=(id_post,token)).start()
    	time.sleep(1)
