from bs4 import BeautifulSoup
import requests


def getthenumber(a):
    a = '"' + a + '"'
    stringcall = "https://www.dice.com/jobs/advancedResult.html?for_one=&for_all=" + a + "&for_exact=&for_none=&for_jt=&for_com=&for_loc=New+York%2C+NY&jtype=Part+Time+OR+Contract+Independent+OR+Contract+W2+OR+C2H+Independent+OR+C2H+W2&sort=relevance&radius=30&jtype=Part+Time+OR+Contract+Independent+OR+Contract+W2+OR+C2H+Independent+OR+C2H+W2&radius=30&jtype=Part+Time+OR+Contract+Independent+OR+Contract+W2+OR+C2H+Independent+OR+C2H+W2"
    result = requests.get(stringcall)
    soup = BeautifulSoup(result.content, "lxml")
    k = soup.get_text()
    ex = open("datas.txt", "w")
    print(k, file=ex)
    d = "wera"
    i = 0
    for l in k.splitlines():
        i += 1
        if i == 8 and "Part-Time OR Contracts" in l:
            num = int(l.split()[0].replace(",", ""))
            return num


a = list()
kw = open("keywords.txt", "r", encoding='utf8')
for line in kw:
    line = line.replace('\n', '')
    WebLine = line.replace(' ', '+')
    k = getthenumber(WebLine)
    print(str(k))
