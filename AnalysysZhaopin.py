#coding:utf-8


import sys
import os
import itertools
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy
import PSqlite



def AnlysysDB(dbPath):
    #get info from db
    dbInstance = PSqlite.PSqlite3(dbPath)
    jobInfo = dbInstance.QueryData()
    Draw(jobInfo)


def Draw(jobInfo):
    #count by city
    groupByCityJopInfo = itertools.groupby(jobInfo, key = GetCity)
    jobInfo.sort(key = GetCity)
    drawData = [(key, len(list(group))) for key, group in groupByCityJopInfo]
    drawData.sort(key = lambda x:x[1])
    drawData = [value for value in drawData if value[1] > 10]
    print(drawData)
    DrawBarPic(drawData)

def DrawBarPic(drawData):
    names = [str(value[0]) for value in drawData]
    values = [(value[1]) for value in drawData]
    plt.rcParams['font.sans-serif']=['SimHei']
    
    plt.xlabel("City")
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.yticks(numpy.arange(0,300,20))
    
    x = range(0, len(names))
    y = values
    for a,b in zip(x,y):
        plt.text(a, b+0.05, b, ha='center', va= 'bottom')
    
    plt.bar(names, values, label="Python")
    
    plt.show()
    
def GetCity(jobInfo):
    idx = jobInfo[4].find("-")
    if idx == -1:
        return jobInfo[4]
    else:
        return jobInfo[4][:idx]

                                         

if "__main__" == __name__:
    if len(sys.argv) == 1:
        dpPath = dbPath = os.path.join(sys.path[0], "Testpython.db")
        AnlysysDB(dpPath)
    else:    
        dpPath = sys.argv[1]
        AnlysysDB(dpPath)
        
