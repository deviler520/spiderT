# encoding=utf-8

import urllib.request as request
import bs4
import io
import sys


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
    data = f.read()
    for k, v in f.getheaders():
        print("%s : %s" % (k, v))


def main3():
    url = r"http://www.hao6v.com/"
    headers = {
        
    }
    page = request.Request(url, headers)

if __name__ == "__main__":
    '''
    get http://www.hao6v.com/
    
    '''
    main1()
    #main2()