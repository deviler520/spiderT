#encoding=utf-8

import urllib.request as urllib2
import io
import sys

def main():
    url = r"http://hiphotos.baidu.com/error.html"
    html = urllib2.urlopen(url).read()
    print(html.decode("gb2312"))



if __name__ == "__main__":
    
    main()