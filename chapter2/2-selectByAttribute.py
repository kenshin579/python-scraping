from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

# find the number of times "the prince" was surrounded by tags
nameList = bsObj.findAll(text="the prince")  # ["the prince", ....]
print(len(nameList))

# find all tags with the word "text" in the class attr and "title" in the id attr.
allText = bsObj.findAll(id="title", class_="green")
print("id and green:", allText)

# "or" filter 역할
allText = bsObj.findAll({"h1", "h2", "h3"}) # 모든 h1~h3 를 검색함
print("or:", allText)

# keyword argument examples ("and" filter 역할을 함)
allText = bsObj.findAll(id="text")
allText2 = bsObj.findAll("", {"id": "text"}) # 위와 같음
print("1.", allText[0].get_text())
print("1.", allText2[0].get_text())

# allText = bsObj.findAll(class="green") # Python keyword class 이름으로 검색안됨
allText = bsObj.findAll(class_="green")
allText2 = bsObj.findAll("", {"class": "green"}) # 위와 같음
print("2.", allText[0].get_text())
print("2.", allText2[0].get_text())
