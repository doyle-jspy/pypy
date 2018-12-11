#!/usr/bin/env python3

# cmd : doysterTester.py -h

import sys 
import os 
import re 
import getopt 
import stash 
import time 

print("*******************************************************************")
print("*                                                                 *")
print("* -----------                                                     *")
print("* |   -----    \                                                  *")
print("* |   |     \   |                                                 *")
print("* |   |      |  |                                                 *")
print("* |   |     /   |                                                 *")
print("* |   -----    /                                                  *")
print("* -----------                                                     *")
print("* -------------------                                             *")
print("* Doyster Ver.tester                                              *")
print("* Coded by K.D.Y                                                  *")
print("* agzxcvb@naver.com                                               *")
print("*******************************************************************")

def useapp():
    commt = sys.argv[0]
    comm = os.path.dirname(sys.argv[0])
    
    if os.path.dirname(sys.argv[0]) == os.getcwd(): 
        comm = "./" + comm
    
    print("")

    print("기능")
    print(" 1. parse1 : 크롤러 ver_urllib / http 권장")

    print("")
    print("How to Use: options")
    print("")

    print(" 1-1. Doyster의 크롤러 사용하기")
    print('''
    #> Doyster.py -기능
                  - ex) parse1
    #> Target URL :
                  - ex) http://ex.com
    #> Css Selector :
                  - ex) div#id > div.class''' )

def parse1():
    print("Target URL ex) http://ex.com")
    print("Target URL ERR!) ex.com")
    targetUrl = str(input("Target URL : "))

    import urllib
    import urllib.request
    from bs4 import BeautifulSoup

    resopnse = urllib.request.urlopen(targetUrl)
    print(resopnse)
    soup = BeautifulSoup(resopnse, 'html.parser')
    print("Selector ex 1) span.logo")
    print("Selector ex 2) ul.class > li.class")
    userSelect = str(input("CSS Selector : "))
    results = soup.select(userSelect)
    if(not results):
        print("찾는 CSS Selector가 없습니다.")
    else:
        print("1초 간격으로 수집합니다.")
        print("정보가 과다할 경우 ctrl + c를 눌러 종료 후")
        print("주소 또는 CSS를 확인해주세요")
        time.sleep(3)
        for result in results:
            print(result)
            time.sleep(1)
        print("Parse1을 종료합니다.")
    sys.exit()
    
def start(argv):
    print(argv)
    if '-h' in argv:
        useapp()
    if '-parse1' in argv:
        print("input으로 받을예정")
        parse1()
    else:
        print('option ERR')
        useapp()

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("ERR KeyboardInterrupt")
    except Exception:
        import traceback
        print(traceback.print_exc())
        sys.exit()