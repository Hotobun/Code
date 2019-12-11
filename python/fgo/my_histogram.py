import my_mouse as m 
import time
from PIL import ImageGrab
import win32api
import os
import pickle
import win32gui
import web_image
import random
import threading

def coord_save(im, now_coord ,target_path, index = ''):
    # now_coord   : 截图的坐标  (左上x, 左上y, 右下x, 右下y)
    # target_path : 保存直方图的路径 文件名.pkl 
    # index       ：同名区分下标 无同名可忽略
    
    save_im_object = (index, now_coord, im.histogram(), im)
    with open(os.path.join("my_images",index + target_path), 'wb') as f:
        pickle.dump(save_im_object, f)
    im.save( os.path.join("my_images/",time.strftime("%m-%d %H_%M ", time.localtime()) + index +  target_path[:-3] + 'jpg'))
    print ('ok')
    im.show()

def makepkl(name, index=''):
    # 获取坐标 并保存
    print("延迟3秒 鼠标放在截图的左上")
    time.sleep(3)
    l = win32api.GetCursorPos()
    print("l = ",l)
    print("延迟3秒 鼠标放在截图的右下")
    time.sleep(3)
    r = win32api.GetCursorPos()
    print("r = ",r)
    coord = (l[0],l[1], r[0],r[1])
    im = ImageGrab.grab(coord)
    im.show()
    if input("确认图片请按回车 取消输入有效值递归"):
        return makepkl(name, index)     
    coord_save(im, coord, name + '.pkl', index)

def contrast(data):
    # data : (index, coord, histogram, im)
    im = ImageGrab.grab(data[1])
    if im == data[3]:
        return True

if __name__ == "__main__":
    pass
    
    