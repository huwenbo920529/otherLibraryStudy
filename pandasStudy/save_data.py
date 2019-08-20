# coding:utf-8
import pandas as pd
# data = [['hu', 26, 'wuhan', 'android'], ['hu', 26, 'wuhan', 'android']]
# columns = ['Name', 'Age', 'city', 'device']
# df = pd.DataFrame(data, columns=['Name', 'Age', 'city', 'device'])


columns = ['Loan Number', 'Customer Name', 'SSN', 'Email', 'Home phone', 'Cell phone', 'Work phone',
           'Date and Time Stamp', 'customer_id']
df = pd.read_excel('pending customers.xls', skiprows=[0], sheet_name='Sheet2', header=0)  # 第0行的数据作为列名
customer_id_list = [11261, 11262, 11271, 11273, 9398, 11276, 11279, 11280, 11281, 11284,
                    11287, 11291, 11292, 11297, 11299, 11300, 11301, 11302, 11303]
# print(type(df.iloc[2:-1, :]))
df['customer_id'] = customer_id_list
df.to_csv('test.csv', columns=columns, index=False, header=True, mode='w')
