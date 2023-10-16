import marshal, os, time

banner=("""
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
            \033[1;31m               TOOL ENCODE MARSHAL
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
""")
def py():
	try:
		os.system('clear')
		print(banner)
		a=input("\033[1;37mFile Cần Enc => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("obf_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mTên Files: \033[1;36mobf_"+a)
		print()
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: Không Tìm Thấy Tệp Tin")
		exit()
	
def py2():
	try:
		os.system('clear')
		print(banner)
		a=raw_input("\033[1;37mFile Cần Enc => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mTên Tệp: \033[1;36mobf_"+a)
		print
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: Không Tìm Thấy Tệp Tin")
		exit()

os.system('clear')
print(banner)
print("\033[1;32m[1] Encode Marshal")
ask=input("\033[1;37m[?] Nhập Số => \033[1;32m")
if ask == '1':
	py()
else:
	print("\n\033[1;31m[!] Invalid!")
