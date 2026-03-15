import gevent
from gevent import monkey
# 修改阻塞行为
monkey.patch_socket()
from socket import socket

# 创建套接字
def Server():
    server = socket()
    server.bind(('0.0.0.0',8888))
    server.listen(10)
    print('正在等待客户端连接... ...')

    while True:
        # 阻塞等待中... ...
        client,addr = server.accept()
        print(addr,'连接过来了')
        # 处理客户端请求
        # handle(client)
        # 协程,接收多个客户端连接,实现并发
        gevent.spawn(handle,client)


def handle(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(data.decode())

        client.send('服务端收到消息!'.encode())


if __name__ == '__main__':
    Server()































