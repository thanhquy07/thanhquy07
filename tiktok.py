import requests,os,sys, time
from time import strftime
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
from rich.table import Table as me
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from rich import print as kui
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
import calendar
from time import sleep as jeda
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
import os,sys
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;34m╔═════════════════════════════════════════════════════════════════╗
\033[1;32m║ ████████╗ ███████╚╗       ████████╗ █████╗  █████╗ ██╗          ║
\033[1;35m║ ╚══██╔══╝██║   ██║        ╚══██╔══╝██╔══██╗██╔══██╗██║          ║
\033[1;31m║    ██║   ██║   ██║   █████╗  ██║   ██║  ██║██║  ██║██║          ║
\033[1;33m║    ██║   ██║ ████╚╗  ╚════╝  ██║   ██║  ██║██║  ██║██║          ║
\033[1;34m║    ██║   ╚█████████║         ██║   ╚█████╔╝╚█████╔╝██████╗      ║
\033[1;37m║    ╚═╝    ╚════╗██║          ╚═╝    ╚════╝  ╚════╝ ╚═════╝      ║
\033[1;37m║                ╚══╝                                             ║
\033[1;34m╠═════════════════════════════════════════════════════════════════╣
\033[1;32m║➢ Admin    : Thành Quý Tool                                      ║
\033[1;36m║➢ Youtube  : https://youtube.com/@thanhquytool                   ║
\033[1;31m║➣ Zalo     : 0355879036                                          ║
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
"""
    # Nhập auth
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;97mNHẬP AUTHORIZATION : ")
  token = input("\033[1;31mNHẬP T : ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;97m║ Đăng\033[1;96m Nhập \033[1;95mTài \033[1;94mKhoản \033[1;93mHiện \033[1;92mCó\033[1;91m ( Enter Để Bỏ Qua ,Nhập AUTHORIZATION Tại Đây \033[1;97m║\033[1;91m Để Đổi )  \n\033[1;97m╚⟩⟩⟩ ")

  if select != "":
    author = select
    token = input("\033[1;36mNhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
    quit()

  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;97m•[✩]➭\033[1;36m [{i+1}] \033[1;91m=> \033[1;97mTên Tài Khoản┊\033[1;32m㊪ :\033[1;93m {chontktiktok["data"][i]["nickname"]}  ')
   
dsacc() 
while True:
  try:
    luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩ "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách , Hãy Nhập Lại : "))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;35mSai Định Dạng !!!") 
while True:
  try:
    delay = int(input("\033[1;97m║ Nhập\033[1;91m Delay \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mSai Định Dạng !!!")
while True:
  try: 
    doiacc = int(input("\033[1;97m║ \033[1;99mNhận\033[1;91m Tiền\033[1;96m Thất\033[1;95m Bại\033[1;94m Bao\033[1;93m Nhiu\033[1;92m Lần\033[1;91m Thì\033[1;96m Dừng\033[1;93m \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mNhập Vào 1 Số!!!")    
os.system("clear")    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system("clear")

for x in banner:
  print(x,end = "")
  sleep(0.001)
print("\033[1;31mYouTube : \033[1;33mThành Quý \033[1;33mTool\033[1;32m")
while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;36mCác Acc Tiktok {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy Đê ")
    dsacc()
    while True:
      try:
        luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩  "))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;35mSai Định Dạng !!!")

     
  print(f'\033[1;97mĐang \033[1;96mLấy \033[1;95mNhiệm \033[1;91mVụ\033[1;93m Follow',end="\r")    
  while True:
    try:  
      nhanjob = nhannv(account_id)
      break
    except:
      pass
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mT\033[1;36mh\033[1;35mà\033[1;32mn\033[1;31mh \033[1;34mQ\033[1;33mu\033[1;36mý\033[1;36m🧸 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;34mT\033[1;31mh\033[1;37mà\033[1;36mn\033[1;32mh \033[1;35mQ\033[1;37mu\033[1;33mý\033[1;32m🧸 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
                "\033[1;31mT\033[1;37mh\033[1;36mà\033[1;33mn\033[1;35mh \033[1;32mQ\033[1;34mu\033[1;35mý\033[1;37m🧸 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
                "\033[1;32mT\033[1;33mh\033[1;34mà\033[1;35mn\033[1;36mh \033[1;37mQ\033[1;36mu\033[1;31mý\033[1;34m🧸 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
                "\033[1;37mT\033[1;34mh\033[1;35mà\033[1;36mn\033[1;32mh \033[1;33mQ\033[1;31mu\033[1;37mý\033[1;34m🧸 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
                "\033[1;34mT\033[1;33mh\033[1;37mà\033[1;35mn\033[1;31mh \033[1;36mQ\033[1;36mu\033[1;32mý\033[1;37m🧸 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;36mT\033[1;35mh\033[1;31mà\033[1;34mn\033[1;37mh \033[1;35mQ\033[1;32mu\033[1;36mý\033[1;33m🧸 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
                        
                        
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
    attempts = 0
    max_attempts = 2

    # Vòng lặp thử lại tối đa max_attempts lần
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien["status"] == 200:
                # Nếu hoàn thành thành công, cập nhật thông tin và thoát vòng lặp
                dem += 1
                tien = nhantien["data"]["prices"]
                tong += tien

                # Lấy thời gian hiện tại
                local_time = time.localtime()
                hour = local_time.tm_hour
                minute = local_time.tm_min
                second = local_time.tm_sec

                # Định dạng giờ, phút, giây
                h = f"{hour:02d}"
                m = f"{minute:02d}"
                s = f"{second:02d}"

                # Tạo chuỗi thông báo
                chuoi = (
                    f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                    f"\033[1;31m{nhantien['data']['type']}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                    f"\033[1;32m Ẩn ID\033[1;97m | \033[1;97m \033[1;32m+{tien} \033[1;97m| "
                    f"\033[1;33m{tong}"
                )

                # Xóa dòng trước đó và in thông báo mới
                print(" " * 60, end="\r")  # Xóa dòng cũ
                print(chuoi)    
                checkdoiacc = 0
                break  # Thoát vòng lặp nếu thành công
            else:
                # In toàn bộ response để kiểm tra lý do
                # print(f"Thử lại lần {attempts + 1}.")
                if attempts == 0:
                    for countdown in range(3, -1, -1):
                        print(f"Vui lòng chờ {countdown} giây để hoàn thành job lần thứ 2", end="\r")
                        time.sleep(1)
                    print(" " * 50, end="\r")  # Xóa dòng đếm ngược sau khi hoàn thành

            attempts += 1

        except Exception as e:
            print(f"Đã xảy ra lỗi: {str(e)}. Thử lại lần {attempts + 1}.")
            attempts += 1
            time.sleep(1)  # Thử lại sau 1 giây

    # Nếu hoàn thành thất bại sau 2 lần thử, bỏ qua job và in thông báo
    if attempts == max_attempts:
        print("\033[1;31mBỏ Qua Nhiệm Vụ", end="\r")
        # Xóa dòng thông báo lỗi cũ
        time.sleep(1)

    # Xử lý trường hợp không hoàn thành
    if nhantien["status"] != 200:
        while True:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print(" " * 60, end="\r")  # Xóa dòng thông báo lỗi cũ
                print("\033[1;31mBỏ Qua Nhiệm Vụ", end="\r")
                time.sleep(1)
                checkdoiacc += 1
                break
            except Exception as e:
                print(f"Lỗi khi xử lý thông báo lỗi: {str(e)}")
                time.sleep(1)  # Thử lại sau 1 giây