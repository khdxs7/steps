#!/usr/bin/python3
from scapy.all import *
import socket
import time

# syn扫描
def syn_scan(target_ip, start, end):
    print("\n\033[1;31m开始扫描......\033[0m")
    print("-" * 50)

    # 定义端口计数变量
    c_open = 0
    c_closed = 0
    c_filtered = 0

    # 端口循环扫描
    for port in range(start, end + 1):

        # sr1 向目标发送一个SYN分组（packet）
        a = sr1(IP(dst=target_ip) / TCP(dport=port), timeout=1, verbose=0)

        # 如果没有返回，则表示被过滤
        if a == None:
            print("[*]" + " " + str(port) + " 过滤 ")
            c_filtered += 1
            
        # 接收返回的数据包验证flags 的值 即ACK+SYN回包的16进制数据转为10进制 0X12
        # 转成int 来判断是否回包是ACK+SYN的值18是表示端口开放
        elif int(a[TCP].flags) == 18:

            print("\033[1;32m[*]" + " " + str(port) + " 开放 \033[0m")
            c_open += 1

        # 如果返回值为Syn+Rst,则十六进制为0x14,十进制为20。说明该端口关闭
        elif int(a[TCP].flags) == 20:
            print("\033[1;37m[*]" + " " + str(port) + " 关闭 \033[0m")
            c_closed += 1

    print("-" * 50)
    print("\033[1;31m[*] 扫描完成！\033[0m\n")
    print("[*] 共扫描 %s 个端口，其中" % (c_open + c_closed + c_filtered))
    print("[*] %s 个端口开放" % c_open)
    print("[*] %s 个端口关闭" % c_closed)
    print("[*] %s 个端口被过滤" % c_filtered)


# 检查输入是IP地址还是是网址，以及校验IP合法性
def checkip(hostip):

    pat = re.compile(r"([0-9]{1,3})\.")
    r = re.findall(pat, hostip + ".")
    if len(r) == 4 and len([x for x in r if int(x) >= 0 and int(x) <= 255]) == 4:
        return hostip
    else:
        domain_ip = socket.getaddrinfo(hostip, None)[0][4][0]
        return domain_ip


def run():
    print("\n" + " " * 20 + "\033[1;34mSYN端口扫描器\033[0m \n")

    host_ip = input("请输入网址或者ip地址：")
    if checkip(host_ip) != None:
        target_ip = checkip(host_ip)
        inputs = input("端口范围（eg：50-80）： ")
        ports = inputs.split("-")
        start = int(ports[0])
        end = int(ports[1])

        syn_scan(target_ip, start, end)
        time.sleep(0.01)


if __name__ == "__main__":
    run()
