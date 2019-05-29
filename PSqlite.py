#coding:utf8

import sqlite3

class PSqlite3:

    def __init__(self, dbPath):
        self.conn = sqlite3.connect(dbPath)

    def Close(self):
        conn.close()
        
    def CreateTable(self):
        createTableSql = "create table JobInfo ("\
        +"jobName varchar(50),"\
        +"jobType varchar(50),"\
        +"jobUrl varchar(50),"\
        +"salary varchar(50),"\
        +"city varchar(50),"\
        +"company varchar(50),"\
        +"companyUrl varchar(50),"\
        +"welfare varchar(50))"
                        
        cursor = self.conn.cursor()
        cursor.execute(createTableSql)
        cursor.close()
        self.conn.commit()
        
    def InsertData(self, dicList):
        insterSql = "insert into JobInfo"\
        +" (jobName, jobType, jobUrl, salary, city, company, companyUrl, welfare)"\
        +" values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        cursor = self.conn.cursor()
        for dic in dicList:
            instertStr = insterSql %(
                dic["jobName"],
                dic["jobType"],
                dic["jobUrl"],
                dic["salary"],
                dic["city"],
                dic["company"],
                dic["companyUrl"],
                dic["welfare"],
            )
            cursor.execute(instertStr)
        cursor.close()
        self.conn.commit()

    def QueryData(self):
        selectSql = "select * from JobInfo"
        cursor = self.conn.cursor()
        cursor.execute(selectSql)
        ret = cursor.fetchall()
        cursor.close()

        return ret


if __name__ == "__main__":
    import sys
    import os
    
    dbPath = os.path.join(sys.path[0], "test.db")
    if os.path.exists(dbPath):
        os.remove(dbPath)
        
    sqlObj = PSqlite3(dbPath)
    sqlObj.CreateTable()

    dicList = [
        {
        "jobName":"1",
        "jobType":"2",
        "jobUrl":"3",
        "salary":"4",
        "city":"5",
        "company":"6",
        "companyUrl":"7",
        "welfare":"8"},
        {
        "jobName":"11",
        "jobType":"22",
        "jobUrl":"33",
        "salary":"44",
        "city":"55",
        "company":"66",
        "companyUrl":"77",
        "welfare":"88"}]
    sqlObj.InsertData(dicList)

    ret = sqlObj.QueryData()
    assert ret[1][0] == "11"

    

