from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
System.Clear()
System.Title("Yêu")
System.Size(140, 40)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
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
            \033[1;31m    TOOL ĐẾM LẦN YÊU
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
 """
    print(logo)
logo()   
ban = input(f"{trang}Nhập Tên Bạn: {vang}")
nguoiay = input(f"{trang}Nhập Tên Người Bạn Muốn:{vang} ")
sinhbn = input(f"{trang}Nhập Ngày Tháng Năm Sinh Của Bạn:{vang} ")
sinhho = input(f"{trang}Nhập Ngày Tháng Năm Sinh Của Người Ấy: {vang}")
banner = f"""
ẤN ENTER ĐỂ VÀO ĐỂ BẮT ĐẦU
"""
Anime.Fade(Center.Center(banner), Colors.red_to_white, Colorate.Vertical, enter=True)
dem = 0
while dem<=3000:
      print (f'{do}[{vang}{dem}{do}]{vang}{ban} {do}Yêu {do}{nguoiay} {lam}Rất {luc}Rất {hong}Nhìu!! ')
      dem = dem + 1
      sleep(0.005)
      dem > 10
else:
    sleep (1.5)
    print (f"{do}=> {hong}Đợi {vang}Xíu {lam}Đang {luc}Kết {hong}Nối {lam}Sever {xduong}Tình {do}Yêu")
    sleep (2.5)
    System.Clear()
    sleep(1)
logo = f"""
    Ấn ENTER ĐỂ KẾT SEVER TÌNH YÊU
    """
Anime.Fade(Center.Center(logo), Colors.red_to_yellow, Colorate.Vertical, enter=True)
p = 0
while p<=9:
    p= p + 1
    print(f'{do}[  {vang}Đang Kết Nối {do}]{do}[{lam}|{do}]{tim}[LO......][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[ {xam} Đang Kết Nối {do}]{do}[{black}/{do}]{luc}[LOA.....][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[ {hong} Đang Kết Nối {do}]{do}[{tim}-{do}]{vang}[LOAD....][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[  {luc}Đang Kết Nối{do}]{do}[{luc}+{do}]{xduong}[LOADI...][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[  {lam}Đang Kết Nối {do}]{do}[{xam}\{do}]{trang}[LOADIN..][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[  {trang}Đang Kết Nối {do}][{xduong}|{do}]{xam}[LOADING.][{p}]','     ',end='\r');sleep(1/6)
else:
    sleep(1.5)
    System.Clear()
n = 0
while n<=4:
    n = n + 1
    print(f'{do}Đã {vang}Kết {lam}Nối {tim}Thành {luc}Công','     ',end='\r');sleep(1/6)
    print(f'{tim}Đã {lam}Kết {luc}Nối {do}Thành {xam}Công','     ',end='\r');sleep(1/6)
    print(f'{luc}Đã {black}Kết {trang}Nối {vang}Thành {xduong}Công','     ',end='\r');sleep(1/6)
    print(f'{lam}Đã {xam}Kết {hong}Nối {luc}Thành {trang}Công','     ',end='\r');sleep(1/6)
    sleep(1.5)
    System.Clear()
else:
    sleep(0.5)
print(f"{hong}┌═════════════════════════════════════════════════════┐         ")
print(f"{hong}║                                                     ║       ")
print(f"{hong}║                                                     ║")
print(f"{hong}║                                                     ║")
print(f"{hong}║             {trang}Hiện Tại Là {vang}{current_time} {trang}Rồi Dậy Đi :)))     {hong}║")
print(f"{hong}║             {trang}Yêu {vang}{nguoiay} {trang}Nhìu Vler Luôn!!!          {hong}║")
print(f"{hong}║                                                     ║")
print(f"{hong}║                                                     ║")
print(f"{hong}║                                                     ║")
print(f"{hong}└═════════════════════════════════════════════════════┘      ")
hup = f"""
　　　{trang}　　　　　　　　　　　　　　　　　　　_¶¶
　　　　{trang}　　　　　　　　　　　　　　　　　　　¶¶¶¶
　　　　　　{trang}　　　　　　　　　　　　　　　　¶¶¶¶¶¶¶
　　　　　　　　　{trang}　　　　　　　　　　　　¶¶¶¶¶¶¶¶¶¶¶
　　　　　　　　　　　　{trang}　　　　　　　　_¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　　　　　{do}¶¶¶¶¶¶¶¶¶　　　　¶¶¶¶¶¶¶¶¶{trang}__{trang}¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　　　_{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶{trang}_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　　{trang}_{do}¶¶¶¶¶¶¶{trang}_____{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{do}　¶¶¶¶¶{trang}____{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶{trang}_{do}¶¶¶¶¶
　{do}¶¶¶¶¶{trang}__{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　_{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　_{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　　　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{trang}_{xam}¶{trang}_{do}　¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{xam}¶¶　　{trang}_{do}¶¶¶{trang}_do¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{xam}¶¶¶{trang}___{xam}¶¶{trang}_{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{xam}¶{trang}_{xam}¶¶¶¶{trang}_{xam}¶¶　{do}¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
　{xam}¶{trang}__{xam}¶{trang}__{xam}¶¶　　{trang}_{do}¶¶¶¶¶¶¶¶¶¶¶¶¶
{trang}_{xam}¶{trang}_____{xam}¶¶¶　　　　{do}¶¶¶¶¶¶¶
{xam}¶{trang}________{xam}¶¶¶　　　　{do}¶¶
{xam}¶¶¶¶¶¶¶¶¶¶¶¶¶

"""
print(hup)
print(f"Yêu {nguoiay} Nhìu Lắm Lun Ó! Tặng {nguoiay} Đó❤❤")
print(f"{trang}Thông tin của bạn là:")
print(f"{trang}Name:{vang}{ban}")
print(f"{trang}Ngày Tháng Năm:{vang}{sinhbn}")
print(f"{trang}=======================================================")
print(f"{trang}Name:{vang}{nguoiay}")
print(f"{trang}Ngày Tháng Năm:{vang}{sinhho}")
print(f"{trang}=======================================================")
o = 0
sleep(1)
while o<=6:
    o = o + 1
    print(f'{do}Bắt {vang}Đầu {lam}Phân {tim}Tích','     ',end='\r');sleep(1/6)
    print(f'{tim}Bắt {lam}Đầu {luc}Phân {do}Tích','     ',end='\r');sleep(1/6)
    print(f'{luc}Bắt {black}Đàu {trang}Phân {vang}Tích','     ',end='\r');sleep(1/6)
    print(f'{lam}Bắt {xam}Đầu {hong}Phân {luc}Tích','     ',end='\r');sleep(1/6)
    sleep(1)
else:
    System.Clear()
    sleep(1)
z = 0
while z<=4:
    z = z + 1
    print(f'{do}Đang {vang}Phân {lam}Tích {tim}Năm {luc}Sinh','     ',end='\r');sleep(1/6)
    print(f'{tim}Đang {lam}Phân {luc}Tích {do}Năm {xam}Sinh','     ',end='\r');sleep(1/6)
    print(f'{luc}Đang {black}Phân {trang}Tích {vang}Năm {xduong}Sinh','     ',end='\r');sleep(1/6)
    print(f'{lam}Đang {xam}Phân {hong}Tích {luc}Năm {trang}Sinh','     ',end='\r');sleep(1/6)
else:
    sleep(1)
    System.Clear()
    sleep(1)
print(f"                                                               {do}Kết Quả")
sleep(0.5)
print(f"{luc}Ngày Tháng Năm Sinh Của {vang} {ban} {trang}và {vang}{nguoiay} {trang}Hợp Nhau Nhưng Sẽ Có Đôi Lúc Cãi Vã Giận Dỗi Nhau Nếu Nhường Nhịn Nhau Sẽ Lâu Dài Bền Chặt Hơn")
sleep(0.5)
print(f"                                                         {do}Chúc Hai Bạn Hạnh Phúc Bên Nhau")
print('Cảm Ơn Bạn Đã Dùng Tool') 
exit