import win32api
import win32gui
import win32con
# import pymouse
import time


def click(x,y, timeout = 0, s = '', **args):
    print('args --> ',x,y)
    print((x,y), type(x))
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    # if args.get('d', None):
    #     timeout = args.get('d', 0)
##    try:
##        win32api.SetCursorPos((x,y))
##        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
##        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
###    except pywintypes.error as e:
###        print ('pywintypes.error')
###        click(x,y,timeout, s)
##    except:
##        print ('mouse未知错误 重试中')
##        print('args --> ',x,y)
##        return
##        click(x,y,timeout, s)

    print (time.strftime('%H:%M %S', time.localtime()), (x, y), s)
    time.sleep(timeout)

def position():
    return win32api.GetCursorPos()
