#!/usr/bin/env python
#_*_coding:utf-8_*_

#初始化用户数据表 user_list.db

import os
import json
import  sys
import base64

def encrypt(string):
    s1 = base64.encodestring(bytes(string,encoding='utf-8'))
    return s1.decode('utf-8')
    
def init_db_user():
    _db_file = os.path.join(DATABASE['dbpath'],"user.db")            
    username = input('please input username:')
    password = input('please input password:')
    temp = [username,'@nsn-intra']
    tmpusername = ''.join(temp)
    
    with open(_db_file,"w+") as fp:
        for k,v in _user_list.items():

            _user_list['username'] = tmpusername
            #对密码进行加密
            encrypassword = encrypt(password)
            #修改明文密码            
            _user_list['password']=encrypassword
            
        fp.write(json.dumps(_user_list))     
           
def init_database(): 
    tables = list(DATABASE['tables'].values())#数据表名称列表
    database = DATABASE['dbpath'] #数据表存放路径
 
    for _table in tables:
        #如果表不存在
        if not os.path.exists(os.path.join(database,"{0}.db".format(_table))):
            print("Table {0}.db create successfull".format(_table))
            
        if hasattr(sys.modules[__name__],"init_db_{0}".format(_table)):
            init_func = getattr(sys.modules[__name__],"init_db_{0}".format(_table))
            init_func()

        else:
            print("init table {0} failed, no function init_db_{0} found".format(_table))

if __name__ == "__main__":
    #程序文件主目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #添加环境变量
    sys.path.append(BASE_DIR)
    #数据库信息
    DATABASE = dict(engineer="file",dbpath=BASE_DIR,tables={"user":"user"})
    #用户列表初始化    
    _user_list = {"username":'',"password":''}
    
    init_database()
    print('init_db success')
