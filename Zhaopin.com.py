#coding:utf-8

from bs4 import BeautifulSoup
from urllib import request as urllib2
import json

urlReferer = "https://sou.zhaopin.com/?p=%(page)s&jl=%(location)s&sf=0&st=0&kw=python&kt=3"
url = "https://fe-api.zhaopin.com/c/i/sou?start=%(st)s&pageSize=90&cityId=%(location)s&salary=0,0\
&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3"

listJobInfo = []


RET_ERROR = -1
RET_OK = 0


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
    if js != None and len(js["data"]['results'])!= 0:
        #data is here
        relults = js["data"]['results']
        for result in relults:
            jobInfo = GetJobInfo(result)
            listJobInfo.append(jobInfo)
        return RET_OK       
    else:
        return RET_ERROR


def GetJobInfo(result):
    jobName = result["jobName"]
    jobType = result["jobType"]["items"][0]["name"]
    jobUrl = result["positionURL"]
    salary = result["salary"]
    city = result["city"]["display"]
    company = result["company"]["name"]
    companyUrl = result["company"]["url"]
    welfare = ",".join(str(s) for s in result["welfare"])

    dicRet = {
        "jobName":jobName,
        "jobType":jobType,
        "jobUrl":jobUrl,
        "salary":salary,
        "city":city,
        "company":company,
        "companyUrl":companyUrl,
        "welfare":welfare
        }

    return dicRet

if "__main__" == __name__:

    for i in range(1,3):
        urlChinaReferer = urlReferer %{"page":i, "location":489}
        urlChina = url %{"st":(i-1)*90, "location":489}

        content = GetPageInfo(urlChina, urlChinaReferer)
        if(AnalysisPageInfo(content) == RET_ERROR):
            break

        
                
    print("OK")

    
