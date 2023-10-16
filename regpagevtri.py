
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
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
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
def banner():
 banner = f"""
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
            \033[1;31m    TOOL REG PAGE VỊ TRÍ BẰNG TOKEN
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()

token1 = str(input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mNhập Token Facebook: \033[1;33m "))
pageid = str(input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mNhập ID Page \033[1;34m: \033[1;33m"))
trangthai = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mBạn Có Muốn Tách Và Thêm Vào BM Sau Khi Reg(y/n): \033[1;33m')
if trangthai == 'y' or trangthai =='Y':
    cookie = str(input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mNhập Cookie Facebook \033[1;34m: \033[1;33m "))
    idbm = str(input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;37mNhập ID BM \033[1;34m: \033[1;33m"))
phone = ("0987654321")
if 'instagram.com/accounts/signup' in token1:
    token = token1.split('?#access_token=')[1].split('&data_access')[0]
else:
    token = token1
try:
    tkfb = requests.get(f'https://graph.facebook.com/{pageid}?fields=access_token&access_token={token}').json()['access_token']
except:
    print("\033[1;31mSai Token Hoặc ID Page....")
    exit()
delay = int(input("\033[38;5;220m[\033[38;5;190m●\033[0m\033[38;5;220m]\033[38;0m \033[1;33mNhập Delay Mỗi Lần REG \033[1;34m: \033[1;33m"))
vitri = ['2599270|21|105', '2609757|21|105', '2597193|21|105', '2597962|21|105', '2606884|10|105', '2580006|17|106', '2595023|9|106', '2595010|9|106', '2586264|10|105', '2589937|9|106', '2587704|10|106', '2589889|20|106', '2594850|10|106',  '2589889|20|106', '2594850|10|106', '2604596|10|105', '2579460|20|106', '2589701|11|106', '2605902|20|106', '2600067|20|105', '2599270|21|105', '2609757|21|105', '2597193|21|105', '2597962|21|105', '2606884|10|105', '2580006|17|106', '2595023|9|106', '2595010|9|106', '2586264|10|105', '2589937|9|106', '2587704|10|106', '2589889|20|106', '2594850|10|106',  '2589889|20|106', '2594850|10|106', '2604596|10|105', '2579460|20|106', '2589701|11|106', '2605902|20|106', '2600067|20|105']
logo()
print("             \033[1;36mList Page Tạo Thành Công:")
for i in range(len(vitri)):
    
    dulieu  = vitri[i]
    city_id = dulieu.split('|')[0]
    dau1 = dulieu.split('|')[1]
    dau2 = dulieu.split('|')[2]
    latitude = random.randrange(99999)
    laytokenpage = requests.get('https://graph.facebook.com/v11.0/'+pageid+'?fields=access_token&access_token='+token).json()
    tokenpage = laytokenpage['access_token']
    longitude = random.randrange(99999)
    stt = random.randrange(20000)
    name = requests.get('https://story-shack-cdn-v2.glitch.me/generators/korean-name-generator/male?count=2').json()['data'][0]['name']
    data = {
    '_reqName': 'object:page/locations',
    '_reqSrc': 'LocationManagerUtils',
    'always_open': 'false',
    'differently_open_offerings': '{}',
    'id': pageid,
    'ignore_warnings': 'true',
    'is_franchise': 'false',
    'locale': 'vi_VN',
    'location': '{"city_id":'+city_id+',"latitude":"'+dau1+'.'+str(latitude)+'","longitude":"'+dau2+'.'+str(longitude)+'","street":"'+name+'","zip":"10000"}',
    'method': 'post',
    'permanently_closed': 'false',
    'phone': phone,
    'pickup_options': '[]',
    'place_topics': '["123377808095874","530553733821238"]',
    'pretty': '0',
    'store_name': name,
    'store_number': stt,
    'suppress_http_code': '1',

    }
    don = requests.post(f'https://graph.facebook.com/v11.0/{pageid}/locations?access_token={tkfb}',data=data).json()
    
    try:
        
        idpagereg  = don['id']
        getpage = requests.get(f'https://graph.facebook.com/v11.0/{idpagereg}?access_token={tkfb}')

        idpg = getpage.json()['id']
        name  = getpage.json()['name']
        if trangthai == 'y' or trangthai =='Y':
            tach = requests.get('https://graph.facebook.com/'+pageid+'/locations?method=delete&access_token='+tokenpage+'&location_page_id='+idpagereg).json()
            if tach == True:
            
                
                

                

                headers = {
                    'authority': 'graph.facebook.com',
                    'accept': '*/*',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    # Requests sorts cookies= alphabetically
                    'cookie': cookie,
                    'origin': 'https://business.facebook.com',
                    'referer': 'https://business.facebook.com/',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
                }

                tokenbm = {
                    'access_token': token,
                }

                data = {
                    '_reqName': 'object:business/owned_pages',
                    '_reqSrc': 'PageActions.brands',
                    'access_type': 'OWNER',
                    'code': '',
                    'ig_password': '',
                    'locale': 'vi_VN',
                    'method': 'post',
                    'page_id': idpg,
                    'pretty': '0',
                    'suppress_http_code': '1',
                    'xref': 'ff55505d303a2c',
                }

                themvaobm = requests.post('https://graph.facebook.com/v12.0/'+idbm+'/owned_pages', params=tokenbm,  headers=headers, data=data)
                print(f'\033[1;33mTách Thành Công ID Page: {idpg} Tên Page: {name}')
                print('\033[1;33mThêm Vào BM Thành Công')
                for i in range(delay, -1, -1):
                    print('Chờ ' +str(i)+' Giây [-]          ',end='\r')
                    sleep(0.2)
                    print('Chờ ' +str(i)+' Giây [\]          ',end='\r')
                    sleep(0.2)
                    print('Chờ '+str(i)+' Giây [|]          ',end='\r')
                    sleep(0.2)
                    print('Chờ '+str(i)+' Giây [/]          ',end='\r')
                    sleep(0.2)
                    print('Chờ '+str(i)+' Giây [🔥]          ',end='\r')
                    sleep(0.2)
            else:
                print(f'\033[1;33mTách Không Thành Công ID Page: {idpg} Tên Page: {name} Page Sẽ Lưu Trong Doanh Nghiệp')
                for i in range(delay, -1, -1):
                    print('Chờ ' +str(i)+' Giây [-]          ',end='\r')
                    sleep(0.2)
                    print('Chờ ' +str(i)+' Giây [\]          ',end='\r')
                    sleep(0.2)
                    print('Chờ '+str(i)+' Giây [|]          ',end='\r')
                    sleep(0.2)
                    print('Chờ '+str(i)+' Giây [/]          ',end='\r')
                    sleep(0.2)
                    print('Chờ '+str(i)+' Giây [🔥]          ',end='\r')
                    sleep(0.2)
        else:
            print(f'\033[1;33mReg Thành Công ID Page: {idpg} Tên Page: {name} ')
            for i in range(delay, -1, -1):
                print('Chờ ' +str(i)+' Giây [-]          ',end='\r')
                sleep(0.2)
                print('Chờ ' +str(i)+' Giây [\]          ',end='\r')
                sleep(0.2)
                print('Chờ '+str(i)+' Giây [|]          ',end='\r')
                sleep(0.2)
                print('Chờ '+str(i)+' Giây [/]          ',end='\r')
                sleep(0.2)
                print('Chờ '+str(i)+' Giây [🔥]          ',end='\r')
                sleep(0.2)
    except:
        pass
    













