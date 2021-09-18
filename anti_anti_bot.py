import cv2
import numpy
from datetime import datetime
import pprint
LOG_LOC  = "log"
temp_pic = cv2.imread("pic_set/temp.png")

def cmp_screenshot(src:str, fun_hook):
    src_pic = cv2.imread(src)
    w, h = temp_pic.shape[:-1]

    res = cv2.matchTemplate(src_pic, temp_pic, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = numpy.where(res >= threshold)

    ptc = 0

    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(src_pic, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        ptc += 1

    if ptc != 0:
        cv2.imwrite(f'{LOG_LOC}/result-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png', src_pic)
        if fun_hook:
            fun_hook()
    