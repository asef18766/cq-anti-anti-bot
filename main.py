from win import win_init, get_proc_hwnd
from screenshot import scrrenshot
from anti_anti_bot import cmp_screenshot
from shutil import copyfile
from datetime import datetime
from time import sleep
import json
import logging
from utils import get_current_date_str, print_traceback
import requests

user_data = json.loads(open("setting.json", "r", encoding="utf-8").read())
LB_KEY = user_data["user_token"]
TAR_PROC = user_data["target_proc"]
LINEBOT_URL = user_data["line_bot_url"]

logging.basicConfig(handlers=[logging.FileHandler("log/"+get_current_date_str()+".log", 'w', 'utf-8')], 
                    level=logging.DEBUG)

def upload_line(file:str):
    requests.post(LINEBOT_URL,
        files={
            "screenshot":open(file, 'rb')
        },
        data={
            "user_token":LB_KEY
        }
    )

def backup_samples():
    print("generate backup samples ...")
    copyfile("test.png", f"pic_set/{get_current_date_str()}.png")
    upload_line("test.png")

def main():
    win_init()
    nox_hwnd = get_proc_hwnd(TAR_PROC)
    while True:
        try:
            logging.info(f"taking screen shot at {get_current_date_str()}")
            scrrenshot(nox_hwnd, "test.png")
            cmp_screenshot("test.png", backup_samples)
            # cmp_screenshot("pic_set/anti-bot.png", backup_samples)
            sleep(60)
        except Exception as e:
            print_traceback(e)
if __name__ == "__main__":
    main()