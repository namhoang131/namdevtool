import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Phiên Bản Python Bạn Không Hỗ Trợ!")
# Màu
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
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "#!bin/python3\n#OBFUSCATION BY NAMDEV\n#Date OBF:%s\n" % time.ctime()

def banner(): # Program Banner
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
            \033[1;31m                TOOL ENCODE 16 CHẾ ĐỘ
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n""")
def menu(): # Program Menu
    print(f"{do}[{vang}1{do}] {xduong}Encode Marshal")
    print(f"{do}[{vang}2{do}] {xduong}Encode Zlib")
    print(f"{do}[{vang}3{do}] {xduong}Encode Base16")
    print(f"{do}[{vang}4{do}] {xduong}Encode Base32")
    print(f"{do}[{vang}5{do}] {xduong}Encode Base64")
    print(f"{do}[{vang}6{do}] {xduong}Encode Zlib,Base16")
    print(f"{do}[{vang}7{do}] {xduong}Encode Zlib,Base32")
    print(f"{do}[{vang}8{do}] {xduong}Encode Zlib,Base64")
    print(f"{do}[{vang}9{do}] {xduong}Encode Marshal,Zlib")
    print(f"{do}[{vang}10{do}] {xduong}Encode Marshal,Base16")
    print(f"{do}[{vang}11{do}] {xduong}Encode Marshal,Base32")
    print(f"{do}[{vang}12{do}] {xduong}Encode Marshal,Base64")
    print(f"{do}[{vang}13{do}] {xduong}Encode Marshal,Zlib,B16")
    print(f"{do}[{vang}14{do}] {xduong}Encode Marshal,Zlib,B32")
    print(f"{do}[{vang}15{do}] {xduong}Encode Marshal,Zlib,B64")
    print(f"{do}[{vang}16{do}] {xduong}Encode Thường")
    print(f"{do}[{vang}17{do}] {xduong}Thoát Tool")

class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Kích Thước File : %s\n" % self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % " [-] Nhập Số Mã Hoá : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "namdev = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "namdev = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "namdev = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "namdev = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "namdev = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "namdev = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "namdev = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n Sai Lựa Chọn!")
    
    for x in range(loop):
        try:
            data = "exec((namdev)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % " [-] Chế Độ : "))
        except ValueError:
            sys.exit("\n Sai Lựa Chọn !")
        
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n Cảm Ơn Bạn Đã Dùng Tool")
            os.system('clear') # os.system('cls')
            banner()
        else:
            sys.exit('\n Sai Lựa Chọn !')
        try:
            file = eval(_input % " [-] File Cần Enc : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n Không Tìm Thấy File!")
        
        output = file.lower().replace('.py', '') + '_obf.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n [-] Encode Thành Công: %s" % file)
        print(" [-] Tên Lưu: %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()