from bs4 import BeautifulSoup
import lxml
import requests
import time

target_url = 'https://www.youtube.com/feed/trending'
response = requests.get(target_url)
soup = BeautifulSoup(response.text, "lxml")
lis = soup.find_all('h3',{'class':True})
time.sleep(3)
lic = []
print("*************************************************************************************************************************************************")
for li in lis :
    lic.append(li.text) 

for result in lic[2:]:
    print(result)


    



