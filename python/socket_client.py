"""
发送指定消息 服务器执行命令
"""
import socket

ip = ("127.0.0.1",6666)
s = socket.socket()
s.connect(ip)
s.send("shutdown".encode("utf-8"))
r = s.recv(1024)
print(r.decode('utf-8'))
s.close()
