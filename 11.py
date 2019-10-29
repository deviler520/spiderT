# encoding=utf-8

import urllib.request as request
import bs4
import io
import sys
import pytesseract
from PIL import Image

def main1():
    url = r"http://www.hao6v.com/"

    page = request.urlopen(url).read().decode("gbk")
    page = bs4.BeautifulSoup(page, "html.parser")
    hrefs = page.find("div", class_="col2").find('div', class_="box").find_all("a")
    for href in hrefs:
        print(href["href"])
        print(href.string)


def main2():
    url1 = r"https://api.douban.com/v2/book/2129650"
    f = request.urlopen(url1)
    print("Status", f.status, f.reason)
    ab = ""



    data = f.read()
    for k, v in f.getheaders():
        print("%s : %s" % (k, v))


def main3():
    url = r"http://www.hao6v.com/"
    headers = {
        
    }
    page = request.Request(url, headers)

def main4():
    ss = pytesseract.image_to_string(Image.open(r"C:\Users\gaopeng\Desktop\simple.JPG"))
    print(ss)

def triangles():
    retList = [1]
    while n != 10:
        if n != 0:
            retList = getNextList(retList)
        yield retList

def getNextList(preList):
    if len(preList) == 1:
        return [1,1]
    else:
        nowList = [preList[i] + preList[i+1] for i in range(0, len(preList)-1)]
        nowList.insert(0,preList[0])
        nowList.append(preList[-1])
        return nowList

        

if __name__ == "__main__":
    n = 0              
    results = []        
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break
    print(results)
