import win32api
import win32gui
import win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def re():
    click(1338, 451) # 刷新
    time.sleep(2)
    click(1111, 694) # 确定
    time.sleep(3)
    click(961, 694) # 关闭
    time.sleep(2)

def main():
    for i in range(9):
        re()
        for j in range(432):
            click(793, 581)
            time.sleep(0.1)
            print(j)
        time.sleep(2)
        

if __name__ == "__main__":
    print("3秒后开始点")
    time.sleep(3)
    main()
