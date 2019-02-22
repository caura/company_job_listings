from bs4 import BeautifulSoup
import requests


def getthenumber(a):
    stringcall = "https://www.dice.com/jobs/q-"+a+"-jtype-Part%20Time+OR+Contracts-l-New_York%2C_NY-radius-30-jobs"
    result = requests.get(stringcall)
    soup = BeautifulSoup(result.content, "lxml")
    k = soup.get_text()
    ex = open("temp.txt", "w")
    print(k, file = ex)
    for l in k.splitlines():
        if "Jobs Found" in l:
            d = l
            num = int(d[d.index('(')+1:d.index('J') - 1].replace(',', ''))
            return num


a = list()
kw = open("keywords.txt", "r", encoding='utf8')
for line in kw:
    line = line.replace('\n', '')
    WebLine = line.replace(' ', '+')
    k = getthenumber(WebLine)
    print(str(k))


