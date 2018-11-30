# 네이버 환율 스크래핑
# 5초 간격 
# Json 파일 생성

import threading
from bs4 import BeautifulSoup
import urllib.request
import json
import time

def dataSet(fileName):
    url = "https://finance.naver.com/marketindex/"
    response = urllib.request.urlopen(url)

    soup = BeautifulSoup(response, "html.parser")
    results = soup.select("span.value")
    
    jsonData = {
        "달러" : results[0].text,
        '엔' : results[1].text,
        "유로" : results[0].text
    }
    
    with open('words'+fileName+'.json','w',encoding="utf-8") as f:
        json.dump(jsonData, f, ensure_ascii=False, indent="\t")

def startTimer():
    now = time.localtime()
    fileName = "%04d-%02d-%02d-%02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    timer = threading.Timer(5, startTimer)
    timer.start()
    dataSet(fileName)

startTimer()
