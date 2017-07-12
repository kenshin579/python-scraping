from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
두개의 단위로 자름 
"""
def getNgrams(input, n):
    input = input.split(' ')
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print("2-grams count is: " + str(len(ngrams)))

"""
문제점: 불필요한 부분이 많음. 

[['\nPython\n\n\n\n\nParadigm\nmulti-paradigm:', 'object-oriented,'], ['object-oriented,', 'imperative,'], ['imperative,', 'functional,'], 
['functional,', 'procedural,'], ['procedural,', 'reflective\n\n\nDesigned\xa0by\nGuido'], ['reflective\n\n\nDesigned\xa0by\nGuido', 'van'], 
['van', 'Rossum\n\n\nDeveloper\nPython'], ['Rossum\n\n\nDeveloper\nPython', 'Software'], ['Software', 'Foundation\n\n\nFirst\xa0appeared\n20\xa0February'],
...

"""