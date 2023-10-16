import os,sys,requests,threading
from time import sleep
from datetime import datetime
os.system('title TOOL REACTION STORY')
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
dem = 0
listcx = []
list_page_pro5 = []
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
# ====================== [ FUNCTION ] ======================
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('────────────────────────────────────────────────────────────')
def nam_delay(o):
    while(o>1):
        o=o-1
        print(f'[NAM-DEV][.....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[NAM-DEV][X....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[NAM-DEV][XX...][{o}]','     ',end='\r');sleep(1/6)
        print(f'[NAM-DEV][XXX..][{o}]','     ',end='\r');sleep(1/6)
        print(f'[NAM-DEV][XXXX.][{o}]','     ',end='\r');sleep(1/6)
        print(f'[NAM-DEV][XXXXX][{o}]','     ',end='\r');sleep(1/6)
def tangcxstr(x, dem, linkstr, dataurlstr):
    camxuc = listcx[0]
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_page_pro5[x].split('|')[0]
    name_page = list_page_pro5[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': linkstr,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'useStoriesSendReplyMutation',
        'x-fb-lsd': '4CR-snjduLBRfA-cdgjhg_',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        '__a': '1',
        '__dyn': '7AzHxqU5a5Q1ryUbFuC0BVU98nwgU29zEdEc8co2qwJxS1Nw9m3y4o1DU2_CxS320om782Cwwwqo465o-cw5MKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewGwkUtxGm2SUbElxm0zK5pUfE2FBx_wHwfCm2Sq2-azo2NwkQ0z8c84qifxe3u362-2B0oobo8o',
        '__csr': 'gP4nezNiOqiaH9H5qlPP_vilnFSncKIJESBc_riHQiGRB_iIgRl3maBgy8mlXp9oLD-XggV8zhaGbLBCUnCx-eDAKm78pCxim2yfUoJ12UGcUC3au6UgG9K225opwyxG9wFgfFE4S0MEkwyxOfxK1fwqouw9G1RwPx-0Q82jwoU5C1Twai0d3w2MUvw1Jy3e05ro03l7w1JG01MRw0iY8W0I81bU1G81zE0hZxC0D8',
        '__req': 'r',
        '__hs': '19325.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1006641324',
        '__s': 'vcrj03:a4aoft:01km45',
        '__hsi': '7171454504668598048',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': '4CR-snjduLBRfA-cdgjhg_',
        '__aaid': '497084035286445',
        '__spin_r': '1006641324',
        '__spin_b': 'trunk',
        '__spin_t': '1669734368',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useStoriesSendReplyMutation',
        'variables': '{"input":{"attribution_id_v2":"StoriesCometSuspenseRoot.react,comet.stories.viewer,via_cold_start,1669734368520,55579,,","lightweight_reaction_actions":{"offsets":[0],"reaction":"'+str(camxuc)+'"},"message":"'+str(camxuc)+'","story_id":"'+str(dataurlstr)+'","story_reply_type":"LIGHT_WEIGHT","actor_id":"100088148974138","client_mutation_id":"2"}}',
        'server_timestamps': 'true',
        'doc_id': '4826141330837571',
    }

    runtanglikestr = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
    if 'data' in runtanglikestr:
        print('['+str(dem)+'] | '+str(time)+' | SUCCESS | '+str(uid_page)+' | '+str(name_page)+' | '+str(camxuc)+' | '+str(dataurlstr)+' ')
    else:
        print('Tăng Cảm Xúc Thất Bại')
# =================[ CLEAR + THÔNG SỐ ADMIN ]===========================
clear()
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
            \033[1;31m              TOOL BUFF REACT STORY BẰNG PROFILE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯""")
cookie = input(f'{trang}Nhập Cookie Facebook: {vang}')
# GET fb_dtsg + jazoest
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
}
    
try:
    print(f"\033[1;32mĐang Check Live Cookie...", end="\r")
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    exit(f"{do}Cookie Die")

# get id + name page
headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_page_pro5.append(gomlist)
# NHẬP THÔNG SỐ ĐỂ CHẠY TOOL
clear()
print(f'{lam}Đã Tìm Thấy '+str(len(list_page_pro5))+' Page')
thanh()
linkstr = input(f'{trang}Vui Lòng Nhập Link Story: {vang}')
# TÁCH DATA TRONG URL STR
dataurlstr = linkstr.split('/')[5].split('/?')[0]
# GET THÀNH CÔNG
thanh()
print('Success id: : '+str(dataurlstr)+'')
thanh()
print('Nhập Số [1] Để Tăng Cảm Xúc Like')
print('Nhập Số [2] Để Tăng Cảm Xúc Love')
print('Nhập Số [3] Để Tăng Cảm Xúc Care')
print('Nhập Số [4] Để Tăng Cảm Xúc Haha')
print('Nhập Số [5] Để Tăng Cảm Xúc Wow')
print('Nhập Số [6] Để Tăng Cảm Xúc Sad')
print('Nhập Số [7] Để Tăng Cảm Xúc Angry')
thanh()
cx = int(input('\033[1;37mVui Lòng Nhập Lựa Chọn: \033[1;33m'))
if cx == 1:
    listcx.append('👍')
if cx == 2:
    listcx.append('❤️')
if cx == 3:
    listcx.append('🤗')
if cx == 4:
    listcx.append('😆')
if cx == 5:
    listcx.append('😮')
if cx == 6:
    listcx.append('😢')
if cx == 7:
    listcx.append('😡')
thanh()
soluongcx = int(input('\033[1;37mSố Reaction Cần Tăng: \033[1;33m'))
thanh()
delay = int(input('\033[1;37mNhập Delay Reaction: \033[1;33m'))
thanh()
while True:
    for x in range(int(len(list_page_pro5))):
        dem=dem+1
        threading.Thread(target=tangcxstr,args=(x, dem, linkstr, dataurlstr, )).start()
        nam_delay(delay)
        if dem == soluongcx:
            thanh()
            exit('Success '+str(soluongcx)+' Cảm Xúc ')
            thanh()