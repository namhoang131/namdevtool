#Code By Nguyễn Hoàng Nam
import requests
import re
import threading
import random
import json
import os
import time
import sys
from colorama import Fore, Style, init

# -----[MÀU VÀ BIẾN]-----#
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
kt_code = "</>"
dem = 0
print(f"Tiến hành kiểm tra toàn vẹn của file....")
def download_resource(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Tải về thành công: {file_path}")
    else:
        print(f"Lỗi khi tải về tài nguyên từ: {url}")

# Đường dẫn đến thư mục chứa các tệp tải về
resource_dir = "namdev"

# Kiểm tra và tải về file "config.json"
config_url = "https://namtool131.000webhostapp.com/emoji.json"
config_file_path = os.path.join(resource_dir, "emoji.json")
if not os.path.exists(config_file_path):
    os.makedirs(resource_dir, exist_ok=True)
    download_resource(config_url, config_file_path)
else:
    print(f"File đã tồn tại: {config_file_path}")
# -----[BẮT ĐẦU]-----#
init(convert=True)
os.system("cls")
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
            \033[1;31m              TOOL SPAM COMMENT FACEBOOK
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯""")
cookies = input("\033[1;97mVui Lòng Nhập Cookie Facebook: ")


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
            \033[1;31m                TOOL SPAM COMMENT FACEBOOK
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n"""



    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        time.sleep(0.0000100)


os.system("clear")
os.system("cls")
banner()

count = 0
count_lock = threading.Lock()


def increment_count():
    global count
    with count_lock:
        count += 1


class FB:
    def __init__(self, cookies):
        self.headers = {
            "cookie": cookies,
            "Host": "d.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "connection": "keep-alive",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua": '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
        }

    def comment(self, reply_id, id_post, c_user, comment):
        session = requests.Session()

        response = session.get("https://d.facebook.com/", headers=self.headers)
        data = response.text

        fb_dtsg = re.search(
            r'<input type="hidden" name="fb_dtsg" value="([^"]+)"', data
        ).group(1)
        jazoest = re.search(
            r'<input type="hidden" name="jazoest" value="([^"]+)"', data
        ).group(1)

        comment_data = {
            "fb_dtsg": fb_dtsg,
            "jazoest": jazoest,
            "comment_text": comment,
        }
        comment_headers = {
            **self.headers,
            "user-agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/117.0.0.0",
        }
        response = session.post(
            f"https://d.facebook.com/a/comment.php?parent_comment_id={reply_id}&fs=0&comment_logging&ft_ent_identifier={id_post}&av={c_user}",
            data=comment_data,
            headers=comment_headers,
        )

        if response.status_code == 200:
            increment_count()
            return {"status": True, "data": "Comment Thành Công!"}
        else:
            return {"status": False, "data": "Comment Thất Bại!"}


def comment_on_post(cookies, reply_id, post_id, c_user, comment):
    increment_count()
    while True:
        action = FB(cookies)
        result = action.comment(reply_id, post_id, c_user, comment)
        with count_lock:
            current_count = count
            print(
                f"{Fore.GREEN}[ Nam~Dev ]{Style.RESET_ALL}: {current_count} | {result['data']} | {comment}"
            )

num_threads = int(input("\033[1;97mNhập Số Luồng Muốn Chạy: "))
linkReply = input("\033[1;97mVui Lòng Nhập Link Cần Spam: ")
postID = linkReply.split("ft_ent_identifier=")[1].split("&")[0]
parentCommentID = linkReply.split("ctoken=")[1].split("&")[0].split("_")[1]
cookie_pairs = cookies.split(";")
for pair in cookie_pairs:
    key, value = pair.strip().split("=")
    if key == "c_user":
        c_user_value = value
        break
print(
    "\033[1;96m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
)
comment_text = ["Đừng Nhìn Cmt_", "NGƯỜI SPAM ĐẸP TRAI SỐ 1 THẾ GIỚI"]
with open(f"namdev/emoji.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
threads = []
for i in range(num_threads):
    thread = threading.Thread(
        target=comment_on_post,
        args=(
            cookies,
            parentCommentID,
            postID,
            c_user_value,
            random.choice(comment_text) + " " + random.choice(data),
        ),
    )
    threads.append(thread)
    thread.start()
