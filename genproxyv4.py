import requests
import concurrent.futures
import os, sys,time
import requests
from time import strftime
print(' Đang chạy tiến trình')
logo = """  
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
            \033[1;31m    TOOL HEN PROXY V4
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ 
"""
print(logo)
time.sleep(2)
filename = "allproxy.txt"
a = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000000&country=CN&ssl=all&anonymity=all')
b = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000000&country=VN&ssl=all&anonymity=all')
c = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10099999900&country=UK&ssl=all&anonymity=all')
d = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=US&ssl=all&anonymity=all')
e = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=BR&ssl=all&anonymity=all')
f = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=ID&ssl=all&anonymity=all')
h = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=JP&ssl=all&anonymity=all')
k = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=NL&ssl=all&anonymity=all')
i = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=FI&ssl=all&anonymity=all')
y = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=ES&ssl=all&anonymity=all')
z = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=PL&ssl=all&anonymity=all')
l = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=929929199&country=BD&ssl=all&anonymity=all')
print(' \033[1;32mĐào Proxy Thành Công !')
print(' \033[1;36mLưu Trong File allproxy.txt !')
open(filename,"a").write(a.text)
open(filename,"a").write(b.text)
open(filename,"a").write(c.text)
open(filename,"a").write(d.text)
open(filename,"a").write(e.text)
open(filename,"a").write(f.text)
open(filename,"a").write(h.text)
open(filename,"a").write(k.text)
open(filename,"a").write(i.text)
open(filename,"a").write(y.text)
open(filename,"a").write(z.text)
open(filename,"a").write(l.text)