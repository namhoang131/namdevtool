from faker import Faker
import random
import string
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
def generate_email(domain, num_emails, filename, country):
    if country.lower() == 'us':
        fake = Faker('en_US')
    elif country.lower() == 'india':
        fake = Faker('hi_IN')
    elif country.lower() == 'vn':
        fake = Faker('vi_VN')
    elif country.lower() == 'canada':
        fake = Faker('en_CA')
    elif country.lower() == 'singapore':
        fake = Faker('en_SG')
    elif country.lower() == 'sez':
        fake = Faker('fr_FR')
    else:
        print("\033[1;37m" + "Quốc gia không được hỗ trợ. Vui lòng chọn 'US', 'India', 'VN', 'Canada', 'Singapore' hoặc 'Sez'." + "\033[1;33m")
        return

    # Danh sách tên Việt Nam
    vietnamese_names = "Nguyen,Tran,Le,Pham,Ho,Huynh,Hoang,Phan,Vu,Vo,Dang,Bui,Do,Hua,Ly,Cao,Dinh,Doan,Dao,Duc,Duong,Giang,Ha,Han,Khuat,Khuong,La,Lam,Luc,Mai,Mac,Nghe,Nghiem,Ngo,Ngo,Nguyen,Pho,Quach,Quang,Quan,Quy,Ta,Thai,Thach,Than,Thang,Thao,Thi,Thich,Thinh,Thoi,Tieu,To,Trang,Trinh,Trinh,Truong,Tu,Ung,Vien,Vuong,Vuu,Yen,Van,Thi,Dinh..."

    # Chuyển đổi danh sách tên thành một danh sách
    vietnamese_names = vietnamese_names.split(',')

    # Hỏi người dùng có muốn thêm số vào tên không
    use_numbers = input("\033[1;37m" + "Bạn có muốn thêm số vào tên không? (y/n): " + "\033[1;33m")
    use_numbers = True if use_numbers.lower() == 'y' else False

    # Hỏi người dùng muốn thêm ký tự gì vào tên
    char_to_add = input("\033[1;37m" + "Bạn muốn thêm ký tự gì vào sau tên? (Nhập 'không' nếu bạn không muốn thêm ký tự): " + "\033[1;33m")

    with open(filename, 'w') as f:
        for _ in range(num_emails):
            if country.lower() == 'vn':
                # Chọn một tên ngẫu nhiên từ danh sách tên Việt Nam
                name = random.choice(vietnamese_names).lower()
            else:
                # Chọn một tên ngẫu nhiên từ danh sách tên Mỹ/Canada/Ấn Độ/Singapore/Sez
                name = fake.first_name().lower()

            # Thêm số vào tên nếu người dùng chọn
            if use_numbers:
                name += str(random.randint(0, 99))

            # Thêm ký tự vào tên nếu người dùng chọn
            if char_to_add.lower() != 'không':
                name += char_to_add

            email = name + '@' + domain
            print("\033[1;36m" + "Nam~Tool | " + email + " |" + "\033[0m")
            f.write(email + '\n')

if __name__ == "__main__":
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
            \033[1;31m                TOOL GEN MAIL V3
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯""")
    domain = input("\033[1;37m" + "Nhập tên miền của email (ví dụ: yahoo.com): " + "\033[1;33m")
    num_emails = int(input("\033[1;37m" + "Nhập số lượng email bạn muốn tạo: " + "\033[1;33m"))
    filename = input("\033[1;37m" + "Nhập tên file txt để lưu email: " + "\033[1;33m")
    country = input("\033[1;37m" + "Chọn quốc gia để tạo tên (US, India, VN, Canada, Singapore, Sez): " + "\033[1;33m")
    generate_email(domain, num_emails, filename, country)