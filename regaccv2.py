import os,sys,time,requests,string,random
os.system('cls' if os.name=='nt' else 'clear')
#@ Color
trang = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

#@ Banner
def Banner():
    os.system('cls' if os.name=='nt' else 'clear')
    logo = f'''
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
            \033[1;31m              TOOL REG ACC GARENA V2
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
'''
    for X in logo:
        sys.stdout.write(X)
        sys.stdout.flush() 
        time.sleep(0.00)
#@ Lines
def line():
    print('\033[1;37m=======================================================')
#@ Random Username
def GetRandomString(length):
    allowed_chars = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(allowed_chars) for i in range(length))
    return random_string
#@ Delay 
def delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[ \033[1;31mN\033[1;33mA\033[1;36mM \033[1;35mD\033[1;34mE\033[1;32mV\033[1;37m ] \033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[ \033[1;31mN\033[1;33mA\033[1;36mM \033[1;35mD\033[1;34mE\033[1;32mV\033[1;37m ] \033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[ \033[1;31mN\033[1;33mA\033[1;36mM \033[1;35mD\033[1;34mE\033[1;32mV\033[1;37m ] \033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[ \033[1;31mN\033[1;33mA\033[1;36mM \033[1;35mD\033[1;34mE\033[1;32mV\033[1;37m ] \033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[ \033[1;31mN\033[1;33mA\033[1;36mM \033[1;35mD\033[1;34mE\033[1;32mV\033[1;37m ] \033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[ \033[1;31mN\033[1;33mA\033[1;36mM \033[1;35mD\033[1;34mE\033[1;32mV\033[1;37m ] \033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
#@ Input Requirements
Banner()
file_acc = open('file_acc.txt','a')
useragent = input(f"{trang}Nhập UserAgent ( Lấy Ở my-user-agent.com) : {vang}")
datadome = input(f"{trang}Nhập DataDome : {vang}")
typeUS = int(input(f"{trang}Chọn Chế Độ Username:\n1.Random\n2.Tự Điền\n==> Chế Độ :{vang}"))
dl = int(input("Delay : "))
time.sleep(1.5)
Banner()
#@ Go Job
if typeUS==1:
    dem=1
    while True:
        getDataDome = requests.get("https://sso.garena.com/ui/register?locale=VI")
        username = GetRandomString(8)
        email = GetRandomString(12)+'@gmail.com'
        
        cookies = {
            'datadome': datadome,
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'vi-VN,vi;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'datadome=0aSb76EKQo9ZPs0WRETUu-pGWi2o2RiyjVz7Swe~txDQ4remg1M_TFJryihLtFRK4NFt23w4XUE-n8Kh4sUWMaxbKc8r4402xA4ICTr52AOBQ2Ei1sEwNA_YW~j4fHov',
            'Origin': 'https://sso.garena.com',
            'Referer': 'https://sso.garena.com/ui/register?locale=VI',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': useragent,
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-datadome-clientid': datadome,
        }

        data = {
            'username': username,
            'email': email,
            'password': 'c4a38762f9a6d9fd7c3da7e12fc07842bdc0caa73aca9a82c034d37a8cb984215e1b7ff45818b9d18c82e69ef3388e24e8398d46de666e1d6fd3791a1f71fa2084cb544bad3639fa7f6c7445cf29e10c75b4b3d8b6b1a50267026df70ca4a879e3958800ab5fa8589efa649bdd89beae993a06b10f874df322e8f18c041bdc20',
            'location': 'VI',
            'redirect_uri': '',
            'locale': 'VI',
            'mobile_no': '',
            'otp': '',
            'format': 'json',
            'id': '1692419939745',
        }

        response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data).json()
        try:
            if response['username']==username:
                print(f"{whiteb}[{dem}] Reg Thành Công : {xduong}{username}|Nam@2007")
                file_acc.write(f"{username}|Nam@2007\n")
                dem+=1
                delay(o=dl)
        except:
            print(f"{do}Reg Fail !",end="\r")
            datadome = input("DataDome Cũ Đã Die, DataDome Mới : ")
            headers.update({'x-datadome-clientid':datadome})
elif typeUS==2:
    dem=1
    us = input(f"{trang}Nhập UserName : {vang}")
    sll1 = int(input("Nhập Số Bắt Đầu : "))
    sll2 = int(input("Nhập Số Kết Thúc : "))
    for i in range(sll1,sll2+1):
        username = us+str(i)
        email = username+'@gmail.com'

        cookies = {
            'datadome': datadome,
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'vi-VN,vi;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'datadome=0aSb76EKQo9ZPs0WRETUu-pGWi2o2RiyjVz7Swe~txDQ4remg1M_TFJryihLtFRK4NFt23w4XUE-n8Kh4sUWMaxbKc8r4402xA4ICTr52AOBQ2Ei1sEwNA_YW~j4fHov',
            'Origin': 'https://sso.garena.com',
            'Referer': 'https://sso.garena.com/ui/register?locale=VI',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': useragent,
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-datadome-clientid': datadome,
        }

        data = {
            'username': username,
            'email': email,
            'password': 'c4a38762f9a6d9fd7c3da7e12fc07842bdc0caa73aca9a82c034d37a8cb984215e1b7ff45818b9d18c82e69ef3388e24e8398d46de666e1d6fd3791a1f71fa2084cb544bad3639fa7f6c7445cf29e10c75b4b3d8b6b1a50267026df70ca4a879e3958800ab5fa8589efa649bdd89beae993a06b10f874df322e8f18c041bdc20',
            'location': 'VI',
            'redirect_uri': '',
            'locale': 'VI',
            'mobile_no': '',
            'otp': '',
            'format': 'json',
            'id': '1692419939745',
        }

        response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data).json()
        print(response)
        try:
            if response['username']==username:
                print(f"{whiteb}[{dem}] Reg Thành Công : {xduong}{username}|Nam@2007")
                file_acc.write(f"{username}|Nam@2007\n")
                dem+=1
                delay(o=dl)
        except:
            print(f"{do}Reg Fail !",end="\r")
            datadome = input("DataDome Cũ Đã Die, DataDome Mới : ")
            headers.update({'x-datadome-clientid':datadome})