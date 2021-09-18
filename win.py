import win32gui, ctypes
import logging
def enum_cb(hwnd, results):
    results.append((hwnd, win32gui.GetWindowText(hwnd)))

def win_init():
    # this takes care of the DPI settings (https://stackoverflow.com/questions/51786794/using-imagegrab-with-bbox-from-pywin32s-getwindowrect)
    ctypes.windll.user32.SetProcessDPIAware()
    

def get_proc_hwnd(proc_name:str):
    winlist = []
    win32gui.EnumWindows(enum_cb, winlist)
    
    main = [(hwnd, title) for hwnd, title in winlist if proc_name in title][0]
    try:
        main_hwnd = main[0]
        logging.info(f"targeting process {main[1]} with handle {main[0]}")
        return main_hwnd
    except:
        raise ValueError("can not found target process")