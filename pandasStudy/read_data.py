# -*- coding:utf-8 -*-
import pandas as pd
import pymysql

con = pymysql.connect(host='xxx',
                      port=3306,
                      user='xxx',
                      passwd='xxx',
                      db='xxx',
                      use_unicode=True,
                      charset="utf8")
sql = """select company_name
    from t_customer
    where company_name!='' """
ret = pd.read_sql(sql, con)
print(type(ret))
print(ret.head(5))
