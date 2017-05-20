from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)


# children와 descendants의 차이점은 descendants의 경우에는
# 아래에 있는 child (> child)를 계속 중복해서 가져옴)
# print()
for child in bsObj.find("table", {"id": "giftList"}).descendants:
    print(child)
