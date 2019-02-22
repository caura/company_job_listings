from bs4 import BeautifulSoup
import requests


def number(b):
    s = 0
    for type in typel:
        site = "https://www.ziprecruiter.com/candidate/search?search=" + b + "&location=New+York%2C+NY&days=&radius=25&refine_by_salary=&refine_by_tags=employment_type%3A" + type + "&refine_by_title=&refine_by_org_name="
        n = getthenumber(site)
        s += n
    return s


def getthenumber(a):
    result = requests.get(a)
    soup = BeautifulSoup(result.content, "lxml")
    k = soup.get_text()
    i = 0
    for l in k.splitlines():
        i = i + 1
        if i == 15 and '+' in l:
            d = l
            num = int(d[0:d.index('+')].replace(',', ''))
            return num
        elif i == 15:
            return 0


a = list()
typel = list()
types = open("types.txt", "r", encoding='utf8')
for type in types:
    typel.append(type.replace("\n", ''))
kw = open("keywords.txt", "r", encoding='utf8')
ex = open("ZipInfo.txt", "w")
for line in kw:
    line = line.replace('\n', '')
    WebLine = line.replace(' ', '+')
    k = number(WebLine)
    print(str(k))
