from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

'''
추가 작업
table의 행 별로 원하는 td 값을 프린트함 (ex. Cost)
https://stackoverflow.com/questions/43096220/how-to-iterate-over-td-tags-using-bs4
'''
rows = iter(bsObj.find("table").find_all("tr"))
next(rows)
for row in rows:
    cells = row.find_all("td")
    print(cells[2].get_text())
