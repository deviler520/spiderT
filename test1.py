# coding:utf-8

from bs4 import BeautifulSoup
from urllib import request as urllib2


if "__main__" == __name__:
    url = "https://reeoo.com"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request, timeout = 2)
    
    content = response.read()
    #print(content)
    soup = BeautifulSoup(content,"html.parser")
    tag = soup.head
    children = tag.contents
    print(children)