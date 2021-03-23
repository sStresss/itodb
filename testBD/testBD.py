
import pymysql
import GlobalValues

print(GlobalValues.SqlHostname, GlobalValues.SqlPort, GlobalValues.SqlUserName, GlobalValues.SqlPwd, GlobalValues.SqlDBName)

sql_con = pymysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='sergey',
                                  passwd='sinapS281082', db='itodb')

print(GlobalValues.SqlHostname, GlobalValues.SqlPort, GlobalValues.SqlUserName, GlobalValues.SqlPwd, GlobalValues.SqlDBName)

print(sql_con.open)

sql_con.close()