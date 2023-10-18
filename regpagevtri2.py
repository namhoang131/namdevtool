#Code By Nguyễn Hoàng Nam
try:import requests
except:import os;os.system('pip install requests')
from datetime import datetime
import requests,random,os,sys
from time import sleep,strftime

def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo="""
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
            \033[1;31m          TOOL REG PAGE VỊ TRÍ BẰNG TOKEN
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯   """
    print(logo)

def concac_delay(o):
    while(o>1):
        o=o-1
        print(f'[BNamxHnam][.....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[BNamxHnam][X....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[BNamxHnam][XX...][{o}]','     ',end='\r');sleep(1/6)
        print(f'[BNamxHnam][XXX..][{o}]','     ',end='\r');sleep(1/6)
        print(f'[BNamxHnam][XXXX.][{o}]','     ',end='\r');sleep(1/6)
        print(f'[BNamxHnam][XXXXX][{o}]','     ',end='\r');sleep(1/6)

list_token_page=[]
list_id_page=[]
token_s=1
logo()
print('[ENTER - DỪNG NHẬP]')
while(True):
    token_fb=input(f'\033[1;37mNhập Token Facebook {token_s} : \033[1;33m')
    if token_fb=='' and len(list_token_page)>0:break
    id_page=input(f'\033[1;37mNhập ID Page Mẹ {token_s} : \033[1;33m')
    print(f"\033[1;36mLấy ID Page Mẹ Tại: https://business.facebook.com/business_locations ")
    get_token_page=requests.get(f'https://graph.facebook.com/{id_page}?fields=access_token&access_token={token_fb}').json()
    if 'access_token' in get_token_page:
        token_page=get_token_page['access_token']
        list_token_page.append(token_page)
        list_id_page.append(id_page)
        token_s=token_s+1
    elif 'error' in get_token_page:print(get_token_page['error']['message'])
    else:print(get_token_page)
logo()
choice=input('[ENTER - TỰ TÁCH][BẤT KÌ - KHÔNG TỰ TÁCH]\nNHẬP LỰA CHỌN: ')
while(True):
    try:delay=int(input('DELAY: '));break
    except:print('[Hoàng Nam][?]');sleep(0.5)
s=0
logo()
while(True):
    print('[WAITING...]','          ',end='\r')
    for x in range(len(list_token_page)):
        try:
            token_page=list_token_page[x]
            id_page=list_id_page[x]
            latitude=random.randrange(9999)
            longitude=random.randrange(3333)
            store_number=random.randrange(999)
            #name='T O K E N'
            name=requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/female?count=2').json()['data'][0]['name']
            register=requests.post(f'https://graph.facebook.com/v12.0/{id_page}/locations?access_token={token_page}',data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','always_open': 'false','differently_open_offerings': '{}','id': id_page,'ignore_warnings': 'true','is_franchise': 'false','locale': 'vi_VN','location': '{"city_id":2599270,"latitude":"21.'+str(latitude)+'","longitude":"105.2'+str(longitude)+'","street":"'+name+'","zip":"10000"}','method': 'post','permanently_closed': 'false','phone': '+84395581887','pickup_options': '[]','place_topics': '["123377808095874","530553733821238"]','pretty': '0','price_range': 'Unspecified','store_name': name,'store_number': store_number,'suppress_http_code': '1'}).json()
            if 'id' in register:
                s=s+1
                id_register=register['id']
                time=datetime.now().strftime("%H:%M:%S")
                if choice=='':
                    print(f'[{s}][SUCCESSFULY REGISTRATION][{time}][{name.upper()}][{id_register}]',end='\r')
                    tach=requests.post(f'https://graph.facebook.com/v12.0/{id_page}/locations?access_token={token_page}',data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','locale': 'vi_VN','location_page_id': id_register,'method': 'delete','pretty': '0','store_number': store_number,'suppress_http_code': '1'}).json()
                    if 'success' in tach:print(f'[{s}][SUCCESSFULY REGISTRATION + DELETED][{time}][{name.upper()}][{id_register}]')
                else:print(f'[{s}][SUCCESSFULY REGISTRATION][{time}][{name.upper()}][{id_register}]')
                huykazuto_delay(delay)
            elif 'error' in register:print(register['error']['message']);huykazuto_delay(25)
            else:print(register);huykazuto_delay(55)
        except:print('[NETWORK ERROR !]','          ',end='\r')
