#coding:utf-8

from bs4 import BeautifulSoup
from urllib import request as urllib2
import json

urlReferer = "https://sou.zhaopin.com/?p=%(page)s&jl=%(location)s&sf=0&st=0&kw=python&kt=3"
url = "https://fe-api.zhaopin.com/c/i/sou?start=990&pageSize=90&cityId=%(location)s&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3"
def GetPageInfo(url, urlReferer):
    
    content = ""
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'fe-api.zhaopin.com',
        'Origin': 'https://sou.zhaopin.com',
        'Referer': urlReferer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    if response.status == 200:
        content = response.read().decode('utf-8')

    return content



def AnalysisPageInfo(content):
    
    js = json.loads(content)
    if js != None:
        print(js["data"]['results'][0])
        
    



    

if "__main__" == __name__:

    for i in range(1,2):
        urlChinaReferer = urlReferer %{"page":i, "location":489}
        urlChina = url %{"location":489}
        content = GetPageInfo(url, urlChinaReferer)
        AnalysisPageInfo(content)



    
