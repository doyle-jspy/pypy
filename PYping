# ICMP Ping python3 구현
# (참고) 파이썬 모의 해킹과 침투테스팅

import os
import platform
import socket

try :
    print("MY IP : " + socket.gethostbyname(socket.getfqdn()))
except :
    pass

targetIP = input("스캔을 위한 호스트 이름을 입력해주세요(***.***.***.0) : ")
net1 = targetIP.split('.') # 나누어 배열에 담음

if(len(net1) != 4):
    print("정확한 IP를 입력해 주세요")
else:
    net2 = '{}.{}.{}.'.format(net1[0],net1[1],net1[2])
    start1 = int(input("start number : "))
    end1 = int(input("end number : "))
    
    if(start1 > end1):
        print("시작 호스트 값이 종료 호스트보다 클 수 없습니다.") # print는 break 포함
    else:
        oper = platform.system()
        print(oper)
        
        if(oper=="Windows"):
            pingCmd = 'ping -n 1'
        if(oper=="Linux"):
            pingCmd = 'ping -c 1'
        else:
            pingCmd = 'ping -n 1'

        for host in range(start1, end1+1):
            ip = net2 + str(host)
            res = os.popen('{} {}'.format(pingCmd, ip))
            # print(res)
            for line in res.readlines():
                print(line)
