from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print("xml_content", xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "lxml")
textStrings = wordObj.findAll('w:t')  # todo: empty set임. 왜?
for textElem in textStrings:
    print(textElem.text)

for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find('w:pstyle')
        if style is not None and style['w:va'] == 'Title':
            print('<h1>')
            closeTag = '</h1>'
    except AttributeError:
        # No tags to print
        pass
    print(textElem.text)
    print(closeTag)
