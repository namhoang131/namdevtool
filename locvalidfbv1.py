from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests
import bs4
import time
import datetime
import os
import random
#import ActiveKey
import sys
#import file
from threading import Thread
import smtplib
import requests
from multiprocessing import Process
#from email.message import EmailMessage
yellow='\u001b[33;1m'
red='\u001b[31;1m'
green='\u001b[36;1m'
yellows='\u001b[32;1m'
trang='\u001b[37;1m'
hong='\033[1;35m'
def clear():
    if os.name=='nt':os.system('cls')
    else:os.system('clear')
clear()
def logo():
    logo = f"""
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
            \033[1;31m    TOOL LỌC VALID FACEBOOK V1
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n """
    for pr in logo:
        sys.stdout.write(pr)
        sys.stdout.flush()


def run():
    a = input(Colorate.Diagonal(Colors.green_to_white, "\nFile Mail: "))
    filee = open(a, encoding='utf-8')
    list_mail = []
    for i in filee:
        list_mail.append(i.strip('\n'))
#    print(f'''Có {len(list_mail)} Mail Cần Check Liên Kết''')
    l = input(Colorate.Diagonal(Colors.green_to_white, "File Proxy: "))
    lp = open(l, encoding='utf-8')
    list_proxy = []
    for i in lp:
        list_proxy.append(i.strip('\n'))
    luong = int(input(Colorate.Diagonal(Colors.green_to_white, "Thead: ")))
    clear()
    logo()
    print("\n")
    link1 = 'https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'
    h1 = {
        'Accept': '*/*',
        'Pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko' }
    ses = requests.Session()
    get_data = ses.get(link1,headers = h1)
    cookie = get_data.cookies.get_dict()['datr']
    get_data = get_data.text
    lsd = get_data.split('"lsd" value="')[1].split('"')[0]
    jazoest = get_data.split('"jazoest" value="')[1].split('"')[0]
    
    def check_ip():
        abc = random.choice(list_proxy)
        proxy = {
            'http': f'''http://{abc}/''',
            'https': f'''http://{abc}/''' }
        data = f'''lsd={lsd}&jazoest={jazoest}&email=hanqvu2005@gmail.com&did_submit=Rechercher'''
        link2 = 'https://business.facebook.com/login/identify/?ctx=recover&from_login_screen=0'
        h2 = {
            'Accept': 'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*',
            'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=2&ars=facebook_login&alternate_search=0&toggle_search_mode=1',
            'Accept-Language': 'vi,fr;q=0.8,ar-DZ;q=0.5,ar;q=0.3',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729',
            'Host': 'm.facebook.com',
            'Connection': 'Keep-Alive',
            'Cache-Control': 'no-cache',
            'Cookie': f'''datr={cookie}''',
            'Content-Length': '84' }
        check = requests.post(link2,headers= h2,data=data, proxies=proxy)
        if ('mật khẩu' in check.text) == True:
            return True

    
    def run_check_valid():
        if list_mail:
            abc = random.choice(list_proxy)
            proxy = {
                'http': f'''http://{abc}/''',
                'https': f'''http://{abc}/''' }
            mailfb = random.choice(list_mail)
            emailfb = mailfb.split(':')[0]
            data = f'''lsd={lsd}&jazoest={jazoest}&email={emailfb}&did_submit=Rechercher'''
            link2 = 'https://business.facebook.com/login/identify/?ctx=recover&from_login_screen=0'
            h2 = {
                'Accept': 'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*',
                'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=2&ars=facebook_login&alternate_search=0&toggle_search_mode=1',
                'Accept-Language': 'vi,fr;q=0.8,ar-DZ;q=0.5,ar;q=0.3',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729',
                'Host': 'm.facebook.com',
                'Connection': 'Keep-Alive',
                'Cache-Control': 'no-cache',
                'Cookie': f'''datr={cookie}''',
                'Content-Length': '84' }
            
            try:
                stt = ''
                check = requests.post(link2, headers=h2, data=data, proxies=proxy)
                if ('mật khẩu' in check.text) == True:
                    list_mail.remove(mailfb)
                    soup = bs4.BeautifulSoup(check.content, 'html.parser')
                    a = soup.find_all('div', {
                        'class': 'bt bu' })
                    lk = ' ==> Có Liên Kết '
                    for i in a:
                        lk = lk + i.decode_contents().strip()
                    if (emailfb in lk) == True:
                        print(yellows+mailfb + lk)
                        open('Mail_Liên_Kết.txt', 'a',encoding= 'utf-8').write(mailfb + lk + '\n')
                    else:
                        print(green+mailfb+" ==> Liên Kết Ẩn")
                      #  clear()
                    #    open('Mail_Liên_Kết_Ẩn.txt', 'a', encoding ='utf-8').write(mailfb + lk + '\n')
                elif ('Tìm kiếm không trả về kết quả nào' in check.text) == True:
                    lk = ''
                    if check_ip() == True:
                        print(red+mailfb+" ==> Không Liên Kết")
                    #    open('Custom.txt', 'a',encoding="utf-8").write(mailfb + '\n')
                    else:
                        print(yellow+mailfb+" ==> Block IP Check Lại")
                    #    open('Retry.txt', 'a',encoding="utf-8").write(mailfb + '\n')
               # print(yellows+mailfb + lk)
            #    clear()
            except:
                abc#print(green+abc+" ==> Kết Nối Proxy Lỗi")
            #time.sleep(20)
            if not list_mail:
                return None
            #return None
            run_check_valid()


    for j in range(int(luong)):
        t = Thread(target=run_check_valid).start()



logo()
run()
#check()