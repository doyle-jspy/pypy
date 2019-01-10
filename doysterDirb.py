# dirb python으로 구상
# 방식 : 브루트포스 공격과 유사하게 사전에 준비한 자료를 무차별 대입하며, 하위 도메인을 찾는다.
# 제작중인 doyster CLI에 추가할 때 수정할 예정 -> argparse 로 변경 중

import urllib.request
startUrl = 'http://targetURL||IP'
testDir = [1,2,3,4,5]
# 1,2,3,4,5로 표현했지만, 마지막에 자료를 추가할 예정

def dirb(data):
	for data in testDir:
		res = urllib.request.urlopen(startUrl+'/'+data)
    # 또는 curl 사용 예정
		if res == 404 || 401:
			continu
		if res == 200:
			print(data)
			break
      
dirb(testDir)
