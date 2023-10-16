luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
dem = 0
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
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
            \033[1;31m                TOOL GET TOKEN PROFILE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯

"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
# import lib
import requests, threading
import os, sys
from time import sleep
from datetime import datetime
try:
	import requests,pystyle
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system('pip install requests && pip install bs4 && pip install pystyle')
# ==========================[ FUNCTION ]===========================================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
def thanh():
    print('\033[1;37m──────────────────────────────────────────────────────')
# =================[ CLEAR + THÔNG SỐ ADMIN ]===========================  
token = input(trang+'Vui Lòng Nhập Token Facebook'+trang+': '+vang)
thanh()
file_save = input(trang+'Vui Lòng Nhập Tên File Muốn Lưu'+trang+': '+vang)
# JSON GET TOKEN PRO5+PAGE THƯỜNG
thanh()
get_token = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
# RUN
for get in get_token:
    time = datetime.now().strftime("%H:%M:%S")
    dem = dem+1
    tokenpro5 = get['access_token']
    namepro5 = get["name"]
    idpro5 = get['id']
    print(''+do+'['+vang+str(dem)+do+'] | '+xnhac+str(time)+do+' | '+vang+'SUCCESS '+do+' | '+trang+str(idpro5)+do+' | '+trang+str(namepro5)+do+' | '+trang+str(tokenpro5)+'')
    thanh()
    open(''+file_save+'', "a+").write(f'{idpro5}|{tokenpro5}\n')
print(do+'['+vang+'SUCCESS'+do+']'+trang+': '+luc+'Đã Lưu Thành Công Vào File, '+xnhac+file_save+' ')