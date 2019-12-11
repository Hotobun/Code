import my_mouse as m 
import time
from PIL import ImageGrab
import os
import pickle
import win32api
import win32con
import web_image
import my_histogram as h

# 是否关机
shutdown = 1

def get_imtuple(name):
    # 获取直方图数据
    datapath = os.path.join(os.getcwd(),'my_images')
    if name+'.pkl' not in os.listdir(datapath):
        print(datapath,"没有文件", name+'.pkl')
        h.makepkl(name)
    with open(os.path.join(datapath, name+'.pkl'), 'rb') as f:
        data = pickle.load(f)
    # print(type(data))
    # print(data)
    return data

def click(x,y,timeout = 0):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(timeout)

def main():
    callten = get_imtuple('meatball')
    over    = get_imtuple('meatballover')
    while True:
        # 点击召唤十次
        # 循环点召唤
        # 判断溢出结束
        im = ImageGrab.grab(callten[1])
        if im.histogram() == callten[2]:  # 到这里就是友情点召唤界面
            click(1089, 688, 2 )  # 召唤 
            click(1089, 688, 3 )  # 确定
        elif im.histogram() == over[2]:   # 溢出了
            return 
        click(1056, 770, 2)          # 再次召唤
        

if __name__ == "__main__":
    time.sleep(3)
    main()
    if shutdown:
        os.system("shutdown -s -t 10")
