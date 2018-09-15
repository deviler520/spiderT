#encoding=utf-8

import urllib.request as request
import bs4
import io
import sys

def main1():
    url = r"http://www.hao6v.com/"
     
    page = request.urlopen(url).read().decode("gb2312")
    page = bs4.BeautifulSoup(page,"html.parser")
    hrefs = page.find("div", class_ = "col2").find('div', class_= "box").find_all("a")
    for href in hrefs:
        print(href["href"])
        print(href.string)
    
    
    



if __name__ == "__main__":
    '''
    get http://www.hao6v.com/
    
    '''
    main1()