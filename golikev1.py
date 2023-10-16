import requests,sys,os,time,json
from datetime import date
from datetime import datetime
# tz_VietNam = pytz.timezone('Asia/Ho_Chi_Minh')
ctt = "Nếu bạn cho rằng nội dung này không vi phạm Tiêu chuẩn cộng đồng của chúng tôi,"
cp1 = "Tham gia Facebook hoặc đăng nhập để tiếp tục."
cp2 = "Đăng nhập Facebook để xem bài viết này."
xanh= "\033[1;96m"
xlacay ="\033[0;32m"
den="\033[1;90m"
do="\033[1;91m"
luc="\033[1;92m"
vang="\033[1;93m"
xduong="\033[1;94m"
hong="\033[1;95m"
trang="\033[1;97m"
vang="\033[1;93m"
syan="\033[1;36m"
def inten(do,xanh,xduong,vang,syan):
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
            \033[1;31m                   TOOL GOLIKE V1
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯""")
def cc(title):
    for i in title:
        print(i,end='')
        time.sleep(0.02)
def login(author,t):
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": author,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        # 'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        # 'Sec-Ch-Ua-Mobile':'?0',
        # 'Sec-Ch-Ua-Platform':'"Windows"',
        # 'Sec-Fetch-Dest':'empty',
        # 'Sec-Fetch-Mode':'cors',
        # 'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    try:
        account = requests.get("https://sv5.golike.net/api/tiktok-account",headers=head_login).json()
        if (account['status'] == 200):
            print(xlacay+"LOGIN THÀNH CÔNG                              ")
            f = open("taikhoan.txt","w+")
            f.write(author+"|"+t)
            f.close()
            time.sleep(1)
            os.system('clear')
            inten(do,xanh,xduong,vang,syan)
            return account
        else:
            print(trang+"LOGIN THẤT BẠI VUI LÒNG XEM LẠI             ")
            quit()
    except:
        print(do+"GOLIKE ĐANG LỖI, VUI LÒNG QUAY LẠI SAU!!!           ")
        quit()
os.system('clear')
inten(do,xanh,xduong,vang,syan)
print(do+"["+vang+"1"+do+"]:\033[1;97m Đăng nhập tài khoản GOLIKE lần trước   ")
print(do+"["+vang+"2"+do+"]:\033[1;97m Đăng nhập tài khoản GOLIKE mới         ")
select = int(input(trang+"Nhập "+vang+"1"+trang+" hoặc "+vang+"2"+xlacay+":  "+vang))
if (select == 2):
    authorization = input(trang+"Nhập Authorization: "+vang)
    t = input(trang+"Nhập T: "+vang)
    account = login(authorization,t)
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
elif (select == 1):
    f = open("taikhoan.txt","r")
    tam = f.readline()
    authorization = tam.split("|")[0]
    t = tam.split("|")[1]
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    account = login(authorization,t)
listid = []
listname = []
for i in range(len(account['data'])):
    id = account['data'][i]['id']
    listid.append(id)
    user_id = account['data'][i]['user_id']
    unique_username = account['data'][i]['unique_username']
    listname.append(unique_username)
    print(do+"["+vang+str(i)+do+"]"+do+"   =>   "+vang+"ID: "+trang+str(id)+do+"   =>   "+trang+unique_username)
stt = int(input(trang+"Chọn tài khoản để auto: "+vang))
os.system('clear')
inten(do,xanh,xduong,vang,syan)
print(vang+"TOOL BY NAMDEV")
print(vang+"TÀI KHOẢN ĐANG AUTO: "+trang+listname[stt]+"=> "+vang+"ID:"+trang+str(listid[stt]))
print(trang+"=====================================================================")
tong = 0
while True:
    time.sleep(1)
    print(trang+'ĐANG LẤY NHIỆM VỤ TIKTOK                        ',end="\r")
    while True:
        try:
            getjob = requests.get("https://sv5.golike.net/api/advertising/publishers/tiktok/jobs?account_id="+str(listid[stt])+"&data=null",headers=head_login).json()
            link = getjob['data']['link']
            break
        except:
            continue
    success = 0
    id_job = getjob['data']['id']
    type_acction = getjob['data']['type']
    object_id = getjob['data']['object_id']
    os.system('termux-open '+link)
    # os.system('start '+link)
    for i in range(11,0,-1):
        if (type_acction == "follow"):
            print(vang+'VUI LÒNG THỰC HIỆN FOLLOW TRONG '+trang+str(i)+syan+' GIÂY                                  ',end= "\r")
        elif (type_acction == "like"):
            print(vang+'VUI lÒNG THỰC HIỆN THẢ TIM TRONG '+trang+str(i)+syan+' giây                                 ',end= "\r")
        time.sleep(1)
    hd = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=UTF-8",
        "referer": "https://app.golike.net/",
        "origin": "https://app.golike.net",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    dt = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","async": true,"data": null}}'
    print(vang+"ĐANG NHẬN TIỀN                                                         ",end = "\r")
    getxu = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/complete-jobs',data=dt,headers=hd).json()
    if (getxu['status'] != 200):
        getxu1 = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/complete-jobs',data=dt,headers=hd).json()
        if (getxu1['status'] == 200):
            success = 1
            xu =  getxu1['data']['prices']
        else:
            success = 0
    else:
        success = 1
        xu =  getxu['data']['prices']
    if (success == 1):
        tong = tong + 1 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        title = trang+"_NAM_DEV_"+do+" ❖  "+trang+current_time+do+" ❖  "+vang+type_acction+do+" ❖  "+vang+str(id_job)+do+" ❖  "+trang+"+"+str(xu)+do+" ⇒  "+do+"["+vang+str(tong)+do+"]              \n"
        cc(title)
    elif (success == 0):
        print(do+"JOB LỖI, BỎ QUA NHIỆM VỤ                                    ",end = "\r")
        dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
        skipjob = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
        if (skipjob['status'] == 200):
            print(do+"BÁO LỖI THÀNH CÔNG                                     ",end="\r")