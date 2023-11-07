import os,sys,re
import datetime
import json
import random
try:
  import requests
except ImportError:
  os.system('pip install requests')
else:
  pass
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
else:
  pass
try:
  import time
except ImportError:
  os.system('pkg install time')
else:
  pass
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
else:
  pass
from colorama import Back, Fore, Fore, Style, init
import requests
from bs4 import BeautifulSoup
import time
from time import sleep
import json
import platform
import webbrowser
os.system('clear')
 
init(autoreset=True)



def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.datetime.now()

  time = current_time.strftime("%M:%S")
  return time





def changetoken(red,green,white,cyan):
  if not os.path.exists("cache_golike_auth.txt"):
   pass
  else:
    text=f'''{cyan}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{yellow}1{red}] ĐỔI AUTH
{red}[{yellow}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=int(input(f'{white}NHẬP LỰA CHỌN: {yellow}'))
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass
      







def banner(red,green,blue,yellow,cyan,pink):
  text=f"""    
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
            \033[1;31m                   TOOL GOLIKE V2
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯"""
  pr3(text)






def checkver():
  vs= 'https://ghichu.vn/QmspP'
  
  # Sử dụng thư viện requests để tải trang web
  response1 = requests.get(vs)
  
  # Kiểm tra xem tải trang thành công hay không (HTTP status code 200 là thành công)
  if response1.status_code == 200:
      # Parse nội dung HTML bằng BeautifulSoup
      soup1 = BeautifulSoup(response1.text, 'html.parser')
  
      # Tìm thẻ <textarea> bằng class 'content'
      textarea = soup1.find('textarea', {'class': 'content'})
  
      # Lấy nội dung bên trong thẻ <textarea>
      if textarea:
          content = textarea.string.strip()  # Sử dụng .string để lấy nội dung và .strip() để loại bỏ khoảng trắng thừa
          return content
      else:
          print(f'{Fore.LIGHTRED_EX}KIỂM TRA MẠNG CỦA BẠN')
def newtool():
    print(f"{magenta}Version 2.0")
    newversion = 'https://ghichu.vn/rwSyz'


    datanewversion= requests.get(newversion)

# Kiểm tra xem tải trang thành công hay không (HTTP status code 200 là thành công)
    if datanewversion.status_code == 200:
        # Parse nội dung HTML bằng BeautifulSoup
        boctach = BeautifulSoup(datanewversion.text, 'html.parser')
    
        # Tìm thẻ <textarea> bằng class 'content'
        trongdata = boctach.find('textarea', {'class': 'content'})
def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :
    if not os.path.exists("cache_golike_auth.txt"):
      auth=str(input(f'~[+]{white}NHẬP AUTHORIZATION:{yellow} '))
      headers ={
    'Authorization'	:auth,
    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
 }
      check=requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).json()
      if check['status']==200:
              name=check['data'][0]['username']
              hea={
'Authorization':auth
}
# Chuỗi JSON đầu vào
              data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).json()
              #data = json.loads(json_string)
              
              # Tính tổng pending coin
              total_pending_coin = 0
              for key, value in data.items():
                  if isinstance(value, dict) and 'pending_coin' in value:
                      total_pending_coin += value['pending_coin']
              xht=data['current_coin']
              text=f'~[+]{green}THÀNH CÔNG'
              text=f'{white}TÊN TÀI KHOẢN: {yellow} {name}'
              pr(text)
              text=f'{white}XU HIỆN TẠI : {yellow}{xht}'
              pr(text)
              # In tổng pending coin
              text=f'{white}XU CHỜ DUYỆT: {yellow}{total_pending_coin}'
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              text=f'~[+]{white}CHỌN TÀI KHOẢN LÀM NHIỆM VỤ: {yellow} '
              pr(text)
              nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
              for i, nickname in enumerate(nicknames, start=1):
                  globals()[f'{i}'] = nickname
              # In giá trị của các biến
              for i, nickname in enumerate(nicknames, start=1):
                  text=f'{red}[{cyan}{i}{red}]: {globals()[f"{i}"]}'
                  pr(text)
              with open("cache_golike_auth.txt", "w") as state_file:
                state_file.write(auth)
              return auth,check
      else:
        text=f'~[+]{red}FAIL AUTH KHÔNG CHÍNH XÁC>>{cyan}VUI LÒNG NHẬP LẠI'
        continue 
    else:
        with open('cache_golike_auth.txt') as f:
            lines = f.readlines()
            auth=lines[0]
            headers ={
          'Authorization'	:auth,
          't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
}
            check=requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).json()
            if check['status']==200:
              name =check['data'][0]['username']
              hea={
'Authorization':auth
}
# Chuỗi JSON đầu vào
              data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).json()
              #data = json.loads(json_string)
              
              # Tính tổng pending coin
              total_pending_coin = 0
              for key, value in data.items():
                  if isinstance(value, dict) and 'pending_coin' in value:
                      total_pending_coin += value['pending_coin']
              xht=data['current_coin']
              text=f'{white}TÊN TÀI KHOẢN: {yellow} {name}'
              pr(text)
              text=f'{white}XU HIỆN TẠI : {yellow}{xht}'
              pr(text)
              # In tổng pending coin
              text=f'{white}XU CHỜ DUYỆT: {yellow}{total_pending_coin}'
              pr(text)
              nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
              for i, nickname in enumerate(nicknames, start=1):
                  globals()[f'{i}'] = nickname
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              text=f'~[+]{white}CHỌN TÀI KHOẢN LÀM NHIỆM VỤ '
              pr(text)
              # In giá trị của các biến
              for i, nickname in enumerate(nicknames, start=1):
                  text=f'{red}[{cyan}{i}{red}]: {globals()[f"{i}"]}'
                  pr(text)
                  
            return auth, check
def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :
    
    user_input=input(f'~[+]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {white}CHỌN ACC TIKTOK MUỐN CHẠY JOB:{yellow} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{white}ID CỦA NICKNAME SỐ {n} LÀ: {yellow}{idtiktok}"
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              return idtiktok 
          else:
              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue 
    except ValueError:
          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")
          continue 
def open_webpage(link):
    # Kiểm tra loại thiết bị
    device = platform.system()
    if device == "Windows":
        # Nếu là máy tính cá nhân chạy Windows, mở trang web bằng trình duyệt mặc định của máy tính
        webbrowser.open(link)
    elif device == "Darwin":
        # Nếu là máy tính cá nhân chạy macOS, mở trang web bằng trình duyệt mặc định của macOS
        webbrowser.open(link)
    elif device == "Linux":
        # Nếu là máy tính cá nhân chạy Linux, mở trang web bằng trình duyệt mặc định của Linux
        webbrowser.open(link)
    else:
        # Nếu là thiết bị di động hoặc không xác định, mở trang web bằng trình duyệt mặc định của thiết bị
        webbrowser.open(link)
def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  while True :
    hea={
    'Authorization':	auth,
    't':	'VFZSWk5VOUVUWHBOVkUxM1QwRTlQUT09'
}
    a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
    link=a['data']['link']
    id=a['data']['id']
    object_id=a['lock']['object_id']
    open_webpage(link)
    
    for k in range(delay,-1,-1):
      mau=random.choice(ranmau)
      print(f'{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>>  {yellow}NVỤ MỚI SAU  {random.choice(ranmau)}>>  {random.choice(ranmau)}[{k}s]',end='\r')
      sleep(1)
    headers = {
        'authorization': auth,
        't': 'VFZSWk5VOUVUVFZOVkZsNVRrRTlQUT09',
}
    
    json_data = {
        'ads_id': id,
        'account_id': idtiktok ,
        'async': True,
        'data': None,
    }
    
    g = requests.post(
        'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
        headers=headers,
        json=json_data,
    ).json()
    
    if g['status']==200:
      print(f'{green}[{startmaxjob}]{cyan} [{time()}] | {random.choice(ranmau)}SUCCESS |  {green}FOLLOW | {yellow}+{xuthem(auth)}đ')
      startmaxjob+=1
      if startmaxjob == maxjob+1:
        print(f'~[+]{pink}ĐÃ ĐẠT HOÀN THÀNH JOB. ')
        return
    if g['status'] !=200:
      headers = {
          'authorization': auth,
          't': 'VFZSWk5VOUVVWGhQVkZFeFRsRTlQUT09',
      }
      
      json_data = {
          'description': 'Báo cáo hoàn thành thất bại',
          'users_advertising_id': id,
          'type': 'ads',
          'provider': 'tiktok',
          'fb_id': idtiktok ,
          'error_type': 3,
      }
      
      requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data).json()
     
      
      headers = {
          'authorization': auth,
          't': 'VFZSWk5VOUVVWGhQVkZFeFQwRTlQUT09',
 }
      
      json_data = {
          'ads_id': id,
          'object_id': object_id,
          'account_id': idtiktok ,
          'type': 'follow',
      }
      skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
          headers=headers,
          json=json_data,
      ).json()
      print(f'{green}[{startmaxjob}] {cyan}[{time()}] {end}| {random.choice(ranmau)}  FAIL  {end}|{green} FOLLOW  {end}| {red}ĐÃ BỎ QUA JOB')
      startmaxjob+=1
      if startmaxjob == maxjob+1:
        print(f'~[+]{cyan}ĐÃ HOÀN THÀNH SỐ JOB')
        return 
def xuthem(auth):
  headers = {
      'authorization': auth,
  }
  
  params = {
      'page': '1',
  }
  xu = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/logs', params=params, headers=headers).json()
  if xu['status']==200:
                a = [item['prices'] for item in xu['data'] if 'prices' in item]
                a=a[0]
                return a
#green='\033[38;5;10m'
blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
banner(red,green,blue,yellow,cyan,pink)
ver=checkver()       
if ver == 'Version 2.0':
  print(f'{pink}VERSION 2.0')
  changetoken(red,green,white,cyan) 
  auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  
  idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  delay =int(input(f'~[+]{white}NHẬP DELAY: {yellow}'))
  maxjob= int(input(f'~[+]{white}NHẬP SỐ JOB: {yellow}'))
  print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
  sleep(1)
  getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
else:
  newtool()