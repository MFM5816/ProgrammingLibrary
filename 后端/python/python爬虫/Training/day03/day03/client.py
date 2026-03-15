from socket import socket

client = socket()
# 连接服务器
client.connect(('127.0.0.1',8888))

while True:
    # 发消息
    content = input('你想说:')
    client.send(content.encode())
    # 收消息
    data = client.recv(1024)
    print(data.decode())