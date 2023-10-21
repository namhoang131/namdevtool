from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
from time import sleep,strftime
try:from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
except:os.system('pip install pystyle'); from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
black='\033[1;90m'
pink='\033[1;97m'
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;96m'
yellow='\033[1;93m'
pinkx='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
den='[1;90m'
luc='[1;32m'
trang='[1;37m'
red='[1;31m'
vang='[1;33m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
purple='\e[35m'
hong='[1;95m'
hquantool=pink+'['+blue+'NamDev'+pink+']'
hquantool_no_pro=luc+'[NamDev]'+end
hln=pink+"["+blue+"NamDev"+pink+"]"
sadboiz=pink+"["+blue+"NamDev"+pink+"]"
thanh_xau=trang+'~'+red+'['+vang+'⟨⟩'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'✓'+red+'] '+trang+'➩ '+luc
def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1',53))
        return True
    except OSError:
        pass
    return False
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
banners=f"""            
            ╭─⋞─────────────────────────────────────────────────────╮
            ███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
            ████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
            ██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
            ██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
            ██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
            ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
             Youtube : \033[1;37mhttps://youtube.com/@NamTool1
             Nhóm Zalo : \033[1;37mhttps://zalo.me/g/kfmgqm225
             Facebook   : \033[1;37mhttps://facebook.com/nam.nhn131 
            ╰─────────────────────────────────────────────────────⋟─╯ 
                          TOOL TRAO ĐỔI SUB V2
            ╰─────────────────────────────────────────────────────⋟─╯"""     

def lehoangphuc(so):
	a='[1;95m────'*so
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		sleep(0.003)
	print()
def banner():
	print('[0m',end='')
	os.system("clear")
	a=Colorate.Horizontal(Colors.yellow_to_red,banners)
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
	print()
banner()
	
while(True):
        token_tds=input(f'{thanh_xau}{luc}Nhập Token TDS: {vang}')
        
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds))
        if 'error' in ttacc.text:print(red+ttacc.json()['error'].upper())
        if 'success' in ttacc.text:
                user=ttacc.json()['data']['user']
                xu=ttacc.json()['data']['xu']
                xu_die=ttacc.json()['data']['xudie']
                lehoangphuc(14)
                print(pink+''+blue+'\033[1;92mTên Tài Khoản TDS : '+trang+user.upper()+vang+'')
                print(pink+''+blue+'\033[1;92mSố Xu Hiện Có: '+trang+xu.upper()+vang+'')
                print(pink+''+blue+'\033[1;92mTổng Xu Die: '+trang+xu_die.upper()+vang+'')
                sleep(1)
                lehoangphuc(14)
                break
while(True):
        while(True):
                while(True):
                        ck_fb=input(f'{thanh_xau}{trang}Nhập Cookie FACEBOOK: {vang}')
                        os.system("clear")
                        banner()
                        if ck_fb=='':break
                        u_check='https://mbasic.facebook.com/profile.php'
                        h={'cookie':ck_fb}
                        check=requests.get(url=u_check,headers=h).text
                        try:
                                name=check.split('<title>')[1].split('</title>')[0]
                                id_fb=ck_fb.split('c_user=')[1].split(';')[0]
                                lehoangphuc(14)
                                print(pink+''+blue+'\033[1;97mTên Tài Khoản Facebook : '+vang+name.upper()+vang+'')
                                print(pink+''+blue+'\033[1;97mTên Tài Khoản TDS : '+vang+user.upper()+vang+'')
                                print(pink+''+blue+'\033[1;97mSố Xu Hiện Có: '+vang+xu.upper()+vang+'')
                                print(pink+''+blue+'\033[1;97mTổng Xu Die: '+vang+xu_die.upper()+vang+'')
                                
                                sleep(2)
                                break
                        except:
                                print(f'{thanh_xau}{lam} COOKIE FACEBOOK  {redz}{name} BỊ DIE OR  VĂNG{end}')
                if ck_fb=='':
                        print(blue+'CẢM BẠN ĐÃ SỬ DỤNG TOOL CỦA',sadboiz+' !')
                        quit()
                        
                u_run='https://traodoisub.com/api/?fields=run&id='+id_fb+'&access_token='+token_tds
                print(pink+''+blue+'\033[1;97mĐang Cấu Hình Tên Tài Khoản Facebook : '+vang+name.upper()+vang+'')
                run=requests.get(url=u_run)
                if 'success' in run.text:
                        print(vang,'['+run.json()['data']['msg'].upper()+']')
                        lehoangphuc(14)
                        sleep(0.5)
                        break
                else:
                        print(red+run.json()['error'].upper())
                        
        stop=int(input(f'{thanh_xau}{trang}NHẬP SỐ NHIỆM VỤ : {vang}'))
        delay=int(input(f'{thanh_xau}{trang}NHẬP DELAY : {vang}'))
        s=0
       
        while(True):
                print(f'{thanh_xau}{luc}Đợi Giây Lát',end="\r")
                while(True):
                        try:
                                list_nv=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+token_tds)
                                if 'id' in list_nv.text:break
                        except:
                                print(hquantool_no_pro+pink+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+pink+']','               ',end='\r')
                for x in range(0,len(list_nv.json())):
                        try:
                                id_post=list_nv.json()[x]['id']
                                type_post=list_nv.json()[x]['type']
                                if str(type_post)=='LIKE':
                                        type_rect='LIKE'
                                        v=1
                                if str(type_post)=='LOVE':
                                        type_rect='LOVE '
                                        v=2
                                if str(type_post)=='CARE':
                                        type_rect='CARE '
                                        v=3
                                if str(type_post)=='HAHA':
                                        type_rect='HAHA '
                                        v=4
                                if str(type_post)=='WOW':
                                        type_rect='WOW  '
                                        v=5
                                if str(type_post)=='SAD':
                                        type_rect='SAD  '
                                        v=6
                                if str(type_post)=='ANGRY':
                                        type_rect='ANGRY'
                                        v=7
                                host='https://mbasic.facebook.com'
                                u=host+'/reactions/picker/?is_permalink=1&ft_id='+id_post
                                h={'cookie':ck_fb}
                                check=requests.get(url=u,headers=h).text
                                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        break
                                if 'Phẫn nộ' in check:
                                        cx=BeautifulSoup(check,'html.parser')
                                        type_cx=cx.find_all('a')
                                        u_cx=host+str(type_cx[v]['href'])
                                        rect=requests.get(url=u_cx,headers=h).text
                                        #print(rect)
                                        #1like_2tym_3thuongthuong_4haha
                                        #5wow_6sad_7phanno
                                nhan_tien=requests.get('https://traodoisub.com/api/coin/?type='+type_post+'&id='+id_post+'&access_token='+token_tds)
                                if 'success' in nhan_tien.text:
                                        s=s+1
                                        xu=str(nhan_tien.json()['data']['xu'])
                                        msg=str(nhan_tien.json()['data']['msg']).upper()
                                        time=datetime.now().strftime("%H:%M:%S")
                                        print(hquantool_no_pro+luc+'['+blue+str(s)+luc+']['+time+']['+luc+type_rect+vang+']['+luc+msg+vang+']['+luc+xu+vang+']','     ')
                                        if s==stop:break
                                        for a in range(delay,0,-1):
                                                print(hquantool,'['+luc+str(a)+vang+']','     ',end='\r')
                                                sleep(0.7)
                        except:
                                print(hquantool_no_pro+pink+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+pink+']','               ',end='\r')
                if s==stop:break
                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        print(hquantool_no_pro+pink+'['+red+'COOKIE FACEBOOK DIE OR BỊ BLOCK'+pink+']','                    ')
                                        break
        print(hquantool+pink+'[DỪNG TOOL ẤN'+blue+' ENTER !!!'+pink+']')
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds)).json()
        if s==stop:print(f'{thanh_xau}{luc}ĐÃ CHẠY XONG {stop} NHIỆM VỤ TỔNG XU CỦA BẠN LÀ {xu}')