"""
开启socket监听 得到指定消息 执行命令 
"""
import socket
import os

ip = ('127.0.0.1',6666)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ip)
s.listen(5)

while True:
    conn,addr=s.accept()
    msg=conn.recv(1024)
   # print('客户端发来的消息是：',msg)
    if msg == b"shutdown":
        if os.system("shutdown -h 100"):
            conn.send("ok".encode("utf-8"))
        else:
            conn.send("error".encode("utf-8"))
    conn.close()
