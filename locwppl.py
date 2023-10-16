import requests, os, sys, threading, ctypes,time
from faker import Faker
from faker import Faker
os.system('')
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
def check(mail):
    email=mail.split("@")[0]
    headers = {
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-platform-version': '"6.0.0"',
    'dpr': '1',
    'downlink': '10',
    'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.94", "Google Chrome";v="108.0.5359.94"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'device-memory': '4',
    'rtt': '50',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'viewport-width': '783',
    'Content-Type': 'application/json;charset=utf-8',
    'Referer': 'https://1login.wp.pl/rejestracja?client_id=o2_poczta_o2_pl_nh&flow=registration&login_challenge=CkYKJDEwMWJhYWM4NTlmYjlkY2Q5Y2E1MWY5Y2Q1OWFlZDE4YTY4ORDYjbicBhoYChJvMl9wb2N6dGFfbzJfcGxfbmgSAnYxEiADZ-4RXQrzwzFgHHAhQOzY8YBotUUV_HO9xLQeXAZ1kQ&registrationFlow=newForced&registrationBrand=o2',
    'ect': '4g',
}
    params = {
    'login_challenge': 'CkYKJDEwMWJhYWM4NTlmYjlkY2Q5Y2E1MWY5Y2Q1OWFlZDE4YTY4ORDYjbicBhoYChJvMl9wb2N6dGFfbzJfcGxfbmgSAnYxEiADZ-4RXQrzwzFgHHAhQOzY8YBotUUV_HO9xLQeXAZ1kQ',
}
    json_data = {
    'birthDate': '',
    'email': email+'@wp.pl',
    'lastName': '',
    'name': '',
}
    access=requests.post('https://1login.wp.pl/api/v1/public/ol-identity-provider/register/available', headers=headers, params=params,json=json_data,)
    if ('available":false') in access.text:
        print("[+] \033[1;93mliv\033[1;97m >> " +mail )
        open(live,"a+").write(mail+"\n")
    else:
        print("[+] \033[1;96mdie \033[1;97m>> " + mail )
        open(ds,"a+").write(mail+"\n")
def do_long(thread_step):
    for i in range(thread_step, len(file), thread_count):
            check(file[i]) 
print("""
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
            \033[1;31m    TOOL LỌC WPPL
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n
""")
name=input("\033[1;96mFile Contains Mail \033[1;94m>\033[1;91m>\033[1;95m ")
ds=input("\033[1;96mSave Mail Die \033[1;94m>\033[1;91m>\033[1;95m ")
live=input("\033[1;96mSave Mail Liv \033[1;94m>\033[1;91m>\033[1;95m ")
thread_count=int(input("\033[1;96mNumber of Cages \033[1;94m>\033[1;91m>\033[1;95m "))
print ('\033[1;37mLoading.', end='\r')
time.sleep(0.03)
print ('\033[1;37mLoading..', end='\r')
time.sleep(0.03)
print ('\033[1;37mLoading...', end='\r')
time.sleep(0.03)
print ('\033[1;37mLoading....', end='\r')
time.sleep(0.03)
print ('\033[1;37m                 ', end='\r')
time.sleep(0.00)
print ('\033[1;37mKích Hoạt Đa Luồng Sau.', end='\r')
time.sleep(0.5)
print ('\033[1;37mKích Hoạt Đa Luồng Sau..', end='\r')
time.sleep(0.5)
print ('\033[1;37mKích Hoạt Đa Luồng Sau...', end='\r')
time.sleep(0.5)
print ('\033[1;37m                              ', end='\r')
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
print ('\033[1;31mBản Quyền\033[1;97m => \033[1;96mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;32mBản Quyền\033[1;97m => \033[1;95mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;33mBản Quyền\033[1;97m => \033[1;94mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;34mBản Quyền\033[1;97m => \033[1;93mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;35mBản Quyền\033[1;97m => \033[1;92mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;36mBản Quyền\033[1;97m => \033[1;91mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;31mBản Quyền\033[1;97m => \033[1;96mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;32mBản Quyền\033[1;97m => \033[1;95mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;33mBản Quyền\033[1;97m => \033[1;94mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;34mBản Quyền\033[1;97m => \033[1;93mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;35mBản Quyền\033[1;97m => \033[1;92mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;36mBản Quyền\033[1;97m => \033[1;91mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;31mBản Quyền\033[1;97m => \033[1;96mNAM-TOOL', end='\r')
time.sleep(0.3)
print ('\033[1;32mBản Quyền\033[1;97m => \033[1;95mNAM-TOOL', end='\r')
time.sleep(0.3)
print ('\033[1;33mBản Quyền\033[1;97m => \033[1;94mNAM-TOOL', end='\r')
time.sleep(0.3)
print ('\033[1;34mBản Quyền\033[1;97m => \033[1;93mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;35mBản Quyền\033[1;97m => \033[1;92mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;36mBản Quyền\033[1;97m => \033[1;91mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;31mBản Quyền\033[1;97m => \033[1;96mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;32mBản Quyền\033[1;97m => \033[1;95mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;33mBản Quyền\033[1;97m => \033[1;94mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;34mBản Quyền\033[1;97m => \033[1;93mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;35mBản Quyền\033[1;97m => \033[1;92mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;36mBản Quyền\033[1;97m => \033[1;91mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;31mBản Quyền\033[1;97m => \033[1;95mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;32mBản Quyền\033[1;97m => \033[1;94mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;33mBản Quyền\033[1;97m => \033[1;93mNAM-TOOL', end='\r')
time.sleep(0.03)
print ('\033[1;34mBản Quyền\033[1;97m => \033[1;92mNAM-TOOL', end='\r')
time.sleep(0.3)
print ('\033[1;35mBản Quyền\033[1;97m => \033[1;91mNAM-TOOL', end='\r')
time.sleep(0.3)
print ('\033[1;36mBản Quyền\033[1;97m => \033[1;94mNAM-TOOL', end='\r')
time.sleep(0.3)
print ('\033[1;37m                                              ', end='\r')
time.sleep(0.00)
print ('\033[1;34m<>', end='\r')
time.sleep(0.1)
print ('\033[1;31m<><>', end='\r')
time.sleep(0.1)
print ('\033[1;32m<><><>', end='\r')
time.sleep(0.1)
print ('\033[1;33m<><><><>', end='\r')
time.sleep(0.1)
print ('\033[1;34m<><><><><>', end='\r')
time.sleep(0.1)
print ('\033[1;35m<><><><><><>', end='\r')
time.sleep(0.1)
print ('\033[1;36m<><><><><><><>', end='\r')
time.sleep(0.1)
print ('\033[1;37m<><><><><><><><>', end='\r')
time.sleep(0.1)
print ('\033[1;31m<><><><><><><><><>', end='\r')
time.sleep(0.1)
print ('\033[1;32m<><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;33m<><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;34m<><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;35m<><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;36m<><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;37m<><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;31m<><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;32m<><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;33m<><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;34m<><><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;35m<><><><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;36m<><><><><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;31m<><><><><><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;32m<><><><><><><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;33m<><><><><><><><><><><><><><><><><><><><><><><><>', end='\r')
time.sleep(0.01)
print ('\033[1;34m<><><><><><><><><><><><><><><><><><><><><><><><><>\033[1;97m', end='\r')
time.sleep(0.01)
print ('\033[1;34m                                                    ', end='\r')
time.sleep(0.000001)
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
print ('\033[1;32m                                            ', end='\r')
time.sleep(0.001)
print ('\033[1;37m                                          ', end='\r')
print("Xin Lưu Ý Mạng Kém Sẽ Dẫn Đến Sự Việc Sau                     ")
print("Văng Code Khỏi Luồng - Chạy MAX Speed Nhưng Mail Không Lên")
print("Nhưng Đừng Lo Ngại Vì Chúng Không Ảnh Hưởng Đến Mail Và Tool")
print("Xin Cảm Ơn...")
concacduma=input("Enter Nào !!")
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
mo=open(name,"r")
file=mo.read().split("\n")
for i in range(thread_count):
    new_thread=threading.Thread(target=do_long, args=(i,)).start()