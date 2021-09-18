from win import win_init, get_proc_hwnd
from screenshot import scrrenshot
from anti_anti_bot import cmp_screenshot
from shutil import copyfile
from datetime import datetime
from time import sleep
import sys
import traceback
import logging
import json

user_data = json.loads(open("setting.json", "r", encoding="utf-8").read())
LB_KEY = user_data["user_token"]
TAR_PROC = user_data["target_proc"]


def get_time_str()->str:
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
logging.basicConfig(handlers=[logging.FileHandler("log/"+get_time_str()+".log", 'w', 'utf-8')], 
                    level=logging.DEBUG)

def backup_samples():
    print("generate backup samples ...")
    copyfile("test.png", f"pic_set/{get_time_str()}.png")

def main():
    win_init()
    nox_hwnd = get_proc_hwnd(TAR_PROC)
    while True:
        try:
            logging.info(f"taking screen shot at {get_time_str()}")
            scrrenshot(nox_hwnd, "test.png")
            cmp_screenshot("test.png", backup_samples)
            # cmp_screenshot("pic_set/anti-bot.png", backup_samples)
            sleep(60)
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            logging.error(errMsg)
    
if __name__ == "__main__":
    main()