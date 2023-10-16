import requests, os, sys, threading, ctypes,time
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
red='\u001b[31;1m'
yellow='\u001b[33;1m'
trang='\u001b[37;1m'
green='\u001b[32;1m'
os.system('')
def clear():
 if os.name=='nt':os.system('cls')
 else:os.system('clear')
clear()
def banner():
 banner = f"""
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
            \033[1;31m                TOOL LỌC GMAIL LIVE/DIE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
banner()
class Vailon: 
    def __init__(self):
        self.hits, self.checkertotal, self.bad = 0, 0, 0
    def check(self,mail):
        email=mail.split("@")[0]
        headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': 'SOCS=CAISHAgCEhJnd3NfMjAyMjA5MjYtMF9SQzIaAnZpIAEaBgiA49iZBg; SEARCH_SAMESITE=CgQIiJcB; OTZ=6808754_28_28__28_; SID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xP1dOtBDROhKjz5SFZ2HPEAg.; __Secure-1PSID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xP6i9SRLJ2CfBQdtzAtQwGKw.; __Secure-3PSID=Rgjt_cNy7lrlpaysYS_SblWtFHK8poW1mo6VJYa0OSV4R0xPLecZ92MaIfSrGuMqMt58pA.; LSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrS_GBxgp-6OrljgSEuhCTmpw.; __Host-1PLSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrSh_tFjkFrpPLp8IwjEa20Fg.; __Host-3PLSID=o.chat.google.com|o.mail.google.com|s.VN|s.youtube:Rgjt_QKOq4VvjZ-zeMOEMrnS2bJuYXMykeZ03pk5VTiBmCrSwGQJGzGnctiYneQHj99LgQ.; HSID=AIUuPaTXOPxOkhMLf; SSID=Athev6z3ak8lEpjuF; APISID=8DlG_TO9ysaCYWTf/Ae-1aPHfAEn7sgv55; SAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; __Secure-1PAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; __Secure-3PAPISID=GedaQ3G9H4uxE2bs/A3OQFQ_hkv_E85cJ4; ACCOUNT_CHOOSER=AFx_qI5txOCPu91XTnxPNWCseBPchHwgbehh8VuGmeFk2zRINY0V738h-KLeP5Yo3lfvSiV5l-VtwLRgN5Op0w_XVG6YwqIPMLN-BEa6XvrEhrKkXR8gCYkKgdnPUidsjcpCI1GdsBAPbKTlcobj0M0qfH_I3VOANYPGKYf9_AEOU1nH7JXGgaLrtLC4auEVbAiLDXrOhUipqvcGttb7vTflj9NtvK68Ml-Sd47VtuV0Cil4fCv-0sA; AEC=AakniGP-meb0VviSuwR7IJjoArTEwhSbhpotg-le9KKmLAAOgktBblZi5w; NID=511=kPtbzrhed3UY0hf0TMdxpUWo0GtPwy36ZNTlZddiOq1gkQDBPCxh7VKs010hIkHQpo479bpBczkzqMG0H8A3MCw_zrQDLsz5slA7JO2Y12uOh0tEK2j7pLWpZQdtOSTmRo6rJQTeGz2OSKI3RCaBU-6hbKcj81RZ8Xq-ClVxC17Bza4kPouFYs0LsHEVHYIajoqlz4HtzfYHkqE6g_lbfFb16dB9SKlFE6CX7r1FymiUUwCXWLMPgBS-cBXiSBNwAc-T1qXI_iCfIToCMr-y-zxIi-w95fgeDB75V-MKPUHizSyKd2_yLMuYmA; 1P_JAR=2022-12-13-10; __Host-GAPS=1:RVsbsQmEhDoLUWva9ubWUjp1xqfen5umeSWt_tt3GEE_egqADJrD_E1hzlaB8ntwZbhkS4j5ZmamHWgB9u04UNJLaYQrXGExdkm6LHNWFo_WdZYEreZQ033j2EQggNdO6OLUV6X_rW5G0dpBsHryFVH_XhOTnQ:cbjgPCdoVlKJTgeQ; SIDCC=AIKkIs2HVbit189PhWNwtaOVx1w7KkuPvA9zMl9pwOAA9qBwPFutPfoy6NDWQj-BSmFhRXIGbg; __Secure-1PSIDCC=AIKkIs0b8W5dBEgFOgDFbtzs8eMcRhIppWPIfWr6OotDZ-9FNMngm-BupwRxFRzrjM4DOj4Et-0; __Secure-3PSIDCC=AIKkIs3y6FQcDoVUOoLByb8UDCXpUUC6LI0tiGBtnQpSskEzWcnMNNMf_O63FzSBDCAK-7qjc68',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=91132a1d-0fb7-47b1-88c6-efe6f2983fda,sync_account_id=111888066456390590950,signin_mode=all_accounts,signout_mode=show_confirmation',
    'x-client-data': 'CIu2yQEIpLbJAQjEtskBCKmdygEIq5PLAQiSocsBCIr5zAEI3fnMAQjA+swBCPD/zAEIh4HNAQiygs0BCL2DzQE=',
    'x-same-domain': '1',
}
        params = {
            'hl': 'vi',
            '_reqid': '62102',
            'rt': 'j',
        }
        data = f'flowEntry=SignUp&flowName=GlifWebSignIn&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&f.req=%5B%22AEThLlxW8eNh7I717NFQgEJhhfS0ySiuzQJxzYc_22vnt8YllYT8g4EGkHpf0ZJJcp5mjKoldzI8VzX0YNVGVulzcGeFeE2YYYMB_mflSMSYLBtYiWGUjBI1_eprTOfxvzkTDmdpPPRrqAmlnOwR9QdBX2NGxninYT4OUJcGgTDvvLqtN6fo8SCMm90cQvkWVQN5kNVb_wCzHyrHOjIhSQVUB73B8RI9hw%22%2C%22%22%2C%22%22%2C%22{email.replace("@gmail.com","")}%22%2Ctrue%2C%22S1140864020%3A1670945489551602%22%2C1%5D&at=AFoagUW6UNV8lKuxebNs0SsIepiy670yiw%3A1670945489567&azt=AFoagUVtLLqRGj7U4bGqhDm30sJVEd1I5w%3A1670945489567&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%2291132a1d-0fb7-47b1-88c6-efe6f2983fda%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%5D&gmscoreversion=undefined&'
        response = requests.post('https://accounts.google.com/_/signup/webusernameavailability',params=params,headers=headers,data=data).text
        res = response.replace(")]}'","").split('[[["gf.wuar",')[1].split(',[],')[0].split(']]]')[0].split(',[')[0].split(']]]')[0]
        if ('1') in res:
          self.checkertotal += 1
          print(f'{trang}[+] {self.checkertotal}/{len(self.file)} | {green}{email}@gmail.com ==> Die')
          open(self.ds,"a+").write(mail+"\n")

        elif ('2') in res:
          self.checkertotal += 1
          print(f'{trang}[-] {self.checkertotal}/{len(self.file)} | {red}{email}@gmail.com ==> Live')


        elif ('3') in res:
          self.checkertotal += 1
          print(f'{trang}[-] {self.checkertotal}/{len(self.file)} | {yellow}{email}@gmail.com ==> Erro')

        else:
          self.checkertotal += 1
          print(f'{trang}[-] {self.checkertotal}/{len(self.file)} | {red}{email}@gmail.com ==> None')
    def do_long(self,thread_step,thread_count):
        for i in range(thread_step, len(self.file), thread_count):
                self.check(self.file[i])
    def main(self):
        self.name=input(Colorate.Diagonal(Colors.green_to_white, "\n[>^<] => List Mail: "))
        self.ds=input(Colorate.Diagonal(Colors.green_to_white, "[>^<] => Save Mail Die: "))
        self.thread_count=int(input(Colorate.Diagonal(Colors.green_to_white, "[>^<] => Thead: ")))
        self.mo=open(self.name,"r")
        self.file=self.mo.read().split("n")
        for i in range(self.thread_count):
                new_thread=threading.Thread(target=self.do_long, args=(i,self.thread_count)).start()
if __name__ == '__main__':
    run = Vailon()
    run.main()
