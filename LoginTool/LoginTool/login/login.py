#!/usr/bin/env python
#_*_coding:utf-8_*_
import os,sys
import requests
import urllib
import json
import base64

class Admin():
    #程序文件主目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #添加环境变量
    sys.path.append(BASE_DIR)
    #数据库信息
    DATABASE = dict(engineer="file",dbpath=BASE_DIR,tables={"user":"user"})
    __database = "{0}.db".format(os.path.join(DATABASE['dbpath'], DATABASE["tables"]["user"]))

    def __init__(self):
        self.password = ""
        self.username = ""
        self.userinfo = {}
        self.userinfo = self.db_load() 
        self.login()
        
    def load_data_from_db(self,tablename):
        '''
        从指定的数据表中获取所有数据，通过json方式将数据返回
        :param tablename:数据文件名
        :return:返回所有结果
        '''
        try:
            with open(tablename,'r+') as f:
                return json.load(f)
        except Exception as e:
            print(e)
        
    def db_load(self):
        self.dict_user = self.load_data_from_db(self.__database)
        return self.dict_user
    
    def decryption(self,string):
        result = base64.decodestring(string)
        return result.decode('utf-8')
       
    def login(self):           
        header = {
        
                  'Connection': 'Keep-Alive',
                  'Accept-Language': 'zh-CN',
                  'Accept': 'text/html, application/xhtml+xml, */*',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; chromeframe/29.0.1547.57) like Gecko',
                  'Accept-Encoding': 'gzip, deflate',
                  'Host': '10.68.148.38',
                  }
        s = requests.Session()
        s.headers = header
        
        url = 'https://10.68.148.38/dana-na/auth/url_default/login.cgi'
        username = self.userinfo['username']
        tmppassword = self.userinfo['password'].encode('utf-8')
        password = self.decryption(tmppassword)
        postDict = {
                    'tz_offset':'480',
                    'realm':'***-AD',
                    'username':username,
                    'password':password,
                    'btnSubmit':'Sign In',
                    }
        
        postData = urllib.parse.urlencode(postDict).encode()
        result = s.post(url,data=postData,verify=False)
        print('Welcome to Hangzhou Laboratory Login Service.Login status %s' % result.status_code)         

if __name__=="__main__":        
    admin = Admin()

