from pystyle import Write,Colors
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\e[35m"
hong = "\033[1;95m"
thanh_xau= trang + "~" + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + "~" + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
import requests ,json 
from time import sleep 
from datetime import datetime 
import os 
from sys import platform 
from threading import Thread 
def banner():
        os.system("cls" if os.name == "nt" else "clear")
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
            \033[1;31m    TOOL TƯƠNG TÁC CHÉO TIKTOK
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n""")

hello ='mb'if platform [0 :3 ]=='lin'else 'pc'
def nam (ciao ,bo ,hi ):
	ngay =datetime .now ().strftime ("%H:%M:%S")
	print (f'{red}[{vang}{ciao}{red}] {red}| {lam}{ngay} {red}| {vang}{bo} {red}| {trang}{hi} {red}|')
class o (object ):
	def __init__ (xuat ,trong ):
		xuat .token =trong 
	def login (ts ):
		try :
			loi =requests .post ('https://tuongtaccheo.com/logintoken.php',headers ={'Content-type':'application/x-www-form-urlencoded',},data ={'access_token':ts .token })
			nguyen =loi .json ()['data']['user']
			hoang =loi .json ()['data']['sodu']
			ts .cookie ='PHPSESSID='+(loi .cookies )['PHPSESSID']
			return nguyen ,hoang 
		except :
			try :print (red +loi .json ()['mess'])
			except :print (red +' Kiểm Tra Kết Nối Mạng')
			return False 
	def coin (b ):
		try :
			nhn ={'user-agent':'Mozilla/5.0 (Linux; Android 13; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','cookie':b .cookie }
			non =requests .post ('https://tuongtaccheo.com/home.php',headers =nhn ).text 
			a =non .split ('"soduchinh">')[1 ].split ('<')[0 ]
			return a 
		except :
			return False 
	def getnv (nv ,nv2 ):
		try :
			c ={'Content-type':'application/x-www-form-urlencoded','accept':'application/json, text/javascript, */*; q=0.01','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':nv .cookie ,'referer':'https://tuongtaccheo.com/kiemtien/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 13; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest'}
			x =requests .post (f'https://tuongtaccheo.com/tiktok/kiemtien/{nv2}',headers =c ).json ()
			return x 
		except :
			return False 
	def nhantien (y ,z ,hup ):
		try :
			da ='id='+z 
			hell =str (len (da ))
			heaven ={'accept':'*/*','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-length':hell ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8','cookie':y .cookie ,'referer':'https://tuongtaccheo.com/kiemtien/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 13; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest'}
			next =requests .post (f'https://tuongtaccheo.com/tiktok/kiemtien/{hup}',headers =heaven ,data =da )
			if 'mess'in next .text :
				porn =next .json ()['sodu']
				global chat 
				chat +=porn 
				mo =500 if hup =='nhantien.php'else 1300 
				chao =porn //mo 
				namtool (14 )
				print (f'{luc}Nhận Thành Công {chao} Nhiệm Vụ {red}| {lam}+{porn} {red}| {vang}{chat}')
				namtool (14 )
				if dong ==0 :return False 
			elif '"error2":'in mem .text :
				print (red ,mem .json ()['error2'])
				namtool (14 )
				return False 
			elif '"error":'in mem .text :
				print (red ,mem .json ()['error'])
				namtool (14 )
			else :
				print (red +'Nhận Xu Thất Bại Vui, Lòng Thử Lại ')
				namtool (14 )
		except :
			return False 
	def run (cuong ,kim ):
		try :
			thao ={'Content-type':'application/x-www-form-urlencoded','accept':'application/json, text/javascript, */*; q=0.01','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','referer':'https://tuongtaccheo.com/cauhinh/tiktok.php','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 13; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest','cookie':cuong .cookie }
			vu =requests .post ('https://tuongtaccheo.com/cauhinh/datnick.php',headers =thao ,data ={'iddat[]':kim ,'loai':'tt'}).json ()
			return vu 
		except :
			return False 
	def acc_cau_hinh (dit ):
		try :
			ngan =requests .get ('https://tuongtaccheo.com/cauhinh/tiktok.php',headers ={'user-agent':'Mozilla/5.0 (Linux; Android 13; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','cookie':dit .cookie }).text 
			anh =ngan .split ('Nick đang dùng:')[1 ].split ('/> ')[1 ].split ('<')[0 ]
			return anh 
		except :
			return False 
def em (vn ):
  try :
    for het in range (vn ,-1 ,-1 ):
       print (f'{vang}[{trang}Nam~Tool{vang}]['+vang +str (het )+lam +' Giây]           ',end ='\r')
       sleep (1 )
  except :
     sleep (vn )
     print (vn ,end ='\r')
def namtool (viet ):
	for xong in range (viet ):
		print (red +'────',end ='')
	print ('')
def hcm (hoangsa ,truongsa ):
	if truongsa =='mb':
		os .system (f'xdg-open {hoangsa}')
	else :
		os .system (f'cmd /c start {hoangsa}')
def xin (mat ):
	try :
		day =requests .get (f'https://now.tiktok.com/@{mat}',headers ={'user-agent':'Mozilla/5.0 (Linux; Android 13; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'}).text 
		hut =day .split ('{"id":"')[1 ].split ('"')[0 ]
		lo =day .split ('"nickname":"')[1 ].split ('"')[0 ]
		return hut ,lo 
	except :
		return False 
def sua ():
	fuck=0
	can =0 
	sa =0 
	bonam =0 
	go =''
	global chat 
	banner ()
	while True :
		if os .path .exists ('configttc.txt'):
			with open ('configttc.txt','r')as bi :
				xa =bi .read ()
			ten =o (xa )
			tk =ten .login ()
			if tk !=False :
				print (f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Giữ Lại Tài Khoản {vang}'+tk [0 ])
				print (f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Nhập Access_Token TTC Mới')
				ra =input (f'{thanh_xau}{trang}Nhập {red}==>: {vang}')
				if ra =='2':
					os .remove ('configttc.txt')
				elif ra =='1':
					pass 
				else :
					print (red +'Lựa chọn không xác định !!!');namtool (14 )
					continue 
			else :
				os .remove ('configttc.txt')
		if not os .path .exists ('configttc.txt'):
			xa =input (f'{thanh_xau}{trang}Nhập Access_Token TTC: {vang}')
			with open ('configttc.txt','w')as no :
				no .write (xa )
		with open ('configttc.txt','r')as no :
			xa =no .read ()
		ten =o (xa )
		tk =ten .login ()
		if tk !=False :
			chat =tk [1 ]
			id =tk [0 ]
			print (lam +' Đăng Nhập Thành Công ')
			break 
		else :
			os .remove ('configttc.txt')
			continue 
	banner ()
	print (f'{thanh_xau}{trang}Tên Tài Khoản: {vang}{id}')
	print (f'{thanh_xau}{trang}Xu Hiện Tại: {vang}{chat}')
	namtool (14 )
	while True :
		bonam =0 
		print (f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Chạy Nhiệm Vụ Tim')
		print (f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Để Chạy Nhiệm Vụ Follow')
		print (f'{thanh_xau}{trang}Nhập {red}[{vang}3{red}] {trang}Để Chạy Nhiệm Vụ Follow Tiktok Now')
		print (f'{thanh_xau}{trang}Nhập {red}[{vang}4{red}] {trang}Để Chạy Nhiệm Vụ Follow Tiktok Qua Video')
		non =input (f'{thanh_xau}{trang}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
		chich =int (input (f'{thanh_xau}{trang}Nhập Delay:{vang} '))
		namtool (14 )
		while True :
			if bonam ==2 :break 
			bonam =0 
			tren =int (input (f'{thanh_xau}{trang}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
			if tren <8 :
				print (f'{red}Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue 
			that =ten .acc_cau_hinh ()
			if that !=False :
				print (f'{thanh_xau}{trang}Enter Để Dùng Cấu Hình Đã Lưu: {vang}{that}')
			id =input (f'{thanh_xau}{trang}Nhập User Name Cần Cấu Hình:{vang} ')
			if that !=False and id =='':
				namtool (14 )
				print (f'{lam}User {vang}{that} {lam}Đã Được Cấu Hình Trước Đó')
			else :
				bye =xin (id )
				if bye ==False :print (red +'Sai User Name Tik Tok.');continue 
				chay =ten .run (bye [0 ])
				print (chay )
				if chay ==1 :namtool (14 );print (f'{trang}Đang Cấu Hình ID: {vang}{bye[0]} {red}| {trang}User: {vang}{id} {red}| {trang}Tên: {trang}{bye[1]} ');namtool (14 )
				else :print (f'{red}Cấu Hình Thất Bại User: {vang}{id}');continue 
			while True :
				if bonam ==1 or bonam ==2 :break 
				if '1'in non :
					mau =ten .getnv ('getpost.php')
					if mau ==False :print (red +'Không Get Được Nhiệm Vụ Tim !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (mau )==0 :print (red +'Hết Nhiệm Vụ Tim ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{trang}Tìm Thấy{vang}',len (mau ),f'{trang}Nhiệm Vụ Tim',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for vai in mau :
							vao =vai ['link'];bye =vai ['idpost']
							Thread (target =hcm ,args =(vao ,hello )).start ()
							go =go +str (bye )+',';fuck +=1 ;nam (fuck ,'TIM',bye );em (chich )
							if fuck %tren ==0 :
								sleep (1 )
								mup =ten .nhantien (go ,'nhantien.php')
								go =''
								if mup ==False :
									print (red +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
									print (f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
									ra =input (f'{thanh_xau}{trang}Nhập {red}==>: {vang}')
									namtool (14 )
									if ra =='1':bonam =2 ;break 
									elif ra =='2':bonam =1 ;break 
				if bonam ==1 or bonam ==2 :break 
				if '2'in non :
					bu =ten .getnv ('subcheo/getpost.php')
					if bu ==False :print (red +'Không Get Được Nhiệm Vụ Follow !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (bu )==0 :print (red +'Hết Nhiệm Vụ Follow ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{trang}Tìm Thấy{vang}',len (bu ),f'{trang}Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for vai in bu :
							vao =vai ['link'];bye =vai ['idpost']
							Thread (target =hcm ,args =(f'https://www.tiktok.com/@{vao}',hello )).start ()
							go =go +str (bye )+',';fuck +=1 ;nam (fuck ,'FOLLOW',bye );em (chich )
							if fuck %tren ==0 :
								sleep (1 )
								tien =ten .nhantien (go ,'subcheo/nhantien.php')
								go =''
								if tien ==False :
									print (red +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
									print (f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
									ra =input (f'{thanh_xau}{trang}Nhập {red}==>: {vang}')
									namtool (14 )
									if ra =='1':bonam =2 ;break 
									elif ra =='2':bonam =1 ;break 
				if bonam ==1 or bonam ==2 :break 
				if '3'in non :
					mau =ten .getnv ('subcheo/getpost.php')
					if mau ==False :print (red +'Không Get Được Nhiệm Vụ Follow !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (mau )==0 :print (red +'Hết Nhiệm Vụ Follow ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{trang}Tìm Thấy{vang}',len (mau ),f'{trang}Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for vai in mau :
							vao =vai ['link'];bye =vai ['idpost']
							Thread (target =hcm ,args =(f'https://now.tiktok.com/@{vao}',hello )).start ()
							go =go +str (bye )+',';fuck +=1 ;nam (fuck ,'FOLLOW_TIKTOK_NOW',bye );em (chich )
							if fuck %tren ==0 :
								sleep (1 )
								mup =ten .nhantien (go ,'subcheo/nhantien.php')
								go =''
								if mup ==False :
									print (red +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
									print (f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
									ra =input (f'{thanh_xau}{trang}Nhập {trang}===>: {vang}')
									namtool (14 )
									if ra =='1':bonam =2 ;break 
									elif ra =='2':bonam =1 ;break 
				if bonam ==1 or bonam ==2 :break 
				if '4'in non :
					mau =ten .getnv ('subcheo/getpost2.php')
					if mau ==False :print (red +'Không Get Được Nhiệm Vụ Follow !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (mau )==0 :print (red +'Hết Nhiệm Vụ Follow ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{trang}Tìm Thấy{vang}',len (mau ),f'{trang}Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for vai in mau :
							vao =vai ['link'];bye =vai ['idpost']
							Thread (target =hcm ,args =(f'{vao}',hello )).start ()
							go =go +str (bye )+',';fuck +=1 ;nam (fuck ,'FOLLOW',bye );em (chich )
							if fuck %tren ==0 :
								sleep (1 )
								mup =ten .nhantien (go ,'subcheo/nhantien.php')
								go =''
								if mup ==False :
									print (red +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}1{red}] {trang}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{trang}Nhập {red}[{vang}2{red}] {trang}Thay Acc Tiktok ')
									print (f'{thanh_xau}{trang}Nhấn {red}[{vang}Enter{red}] {trang}Để Tiếp Tục')
									ra =input (f'{thanh_xau}{trang}Nhập {do}==>: {vang}')
									namtool (14 )
									if ra =='1':bonam =2 ;break 
									elif ra =='2':bonam =1 ;break 
sua ()