import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
  from random import randint
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  from faker import Faker
  from requests import session
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
os.system("clear")

def checkhotmail():
  s = session()
  n_hotmail = 0
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
            \033[1;31m    TOOL LỌC HOTMAIL LIVE/DIE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n""")
  hotmail = open(input(Colorate.Diagonal(Colors.green_to_white, "File Mail: "))).readlines()
  hotmail_die = input(Colorate.Diagonal(Colors.green_to_white, "File Save Mail: "))
  os.system('clear')
  for line_hotmail in hotmail:
    n_hotmail += 1
    HotMail = line_hotmail.strip("\n")
    name_hotmail = HotMail[0:HotMail.index("@")]
    DL = s.get("https://signup.live.com/signup?username="+name_hotmail+"@hotmail.com&lic=1")
    kq = re.search("isAvailable",DL.text)
    if kq == None:
      print ("[" + str(n_hotmail) + "] Live -> " + name_hotmail + "@hotmail.com")
    else:
      print ("[" + str(n_hotmail) + "] Die -> " + name_hotmail + "@hotmail.com")
      open(hotmail_die,"a").write(name_hotmail + "@hotmail.com" + "\n")
  process_menu()
def process_menu():
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
            \033[1;31m    TOOL LỌC HOTMAIL LIVE/DIE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n""")
  os.system('clear')
  checkhotmail()
  quit()
  if choice_user != '1':
    process_menu()
  if choice_user == '1':
    process_menu()
process_menu()