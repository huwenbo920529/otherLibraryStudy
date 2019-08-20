# -*- coding:utf-8 -*-
# Pandas描述性统计
# 编号	函数	描述
# 1	    count()	非空观测数量
# 2	    sum()	所有值之和
# 3	    mean()	所有值的平均值
# 4	    median()	所有值的中位数
# 5	    mode()	值的模值
# 6	    std()	值的标准偏差
# 7	    min()	所有值中的最小值
# 8	    max()	所有值中的最大值
# 9	    abs()	绝对值
# 10	prod()	数组元素的乘积
# 11	cumsum()	累计总和
# 12	cumprod()	累计乘积
# 注 - 由于DataFrame是异构数据结构。通用操作不适用于所有函数。
# 类似于：sum()，cumsum()函数能与数字和字符(或)字符串数据元素一起工作，不会产生任何错误。
# 字符聚合从来都比较少被使用，虽然这些函数不会引发任何异常。
# 由于这样的操作无法执行，因此，当DataFrame包含字符或字符串数据时，像abs()，cumprod()这样的函数会抛出异常。

import pandas as pd
import numpy as np

data = {'Name': pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack','Lee','David','Gasper','Betina','Andres']),
        'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
        'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
df = pd.DataFrame(data)
print(df)

# 1.汇总数据
# describe()函数是用来计算有关DataFrame列的统计信息的摘要。
print('describe():\n', df.describe())

# 2.sum()方法
# 返回所请求轴的值的总和。 默认情况下，轴为索引(axis=0)。
print('sum():\n', df.sum())

# 3.mean()示例
# 返回平均值
print('mean():\n', df.mean())

# 4.std()示例
# 返回数字列的Bressel标准偏差。
print('std():\n', df.std())

# 5.median()示例
print('median():\n', df.median())

# 6.mode()示例
print('mode():\n', df.mode())

# 7.max()示例
print('max():\n', df.max())

# 8.min()示例
print('min():\n', df.min())

# 9.abs()示例
data1 = {'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
        'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
df1 = pd.DataFrame(data1)
print('abs():\n', df1.abs())

# 10.prod()示例
# 数组元素的乘积
data2 = {'Item1': pd.Series([20, 20, 22]),
         'Item2': pd.Series([4.23, 3.24, 3.98])}
df2 = pd.DataFrame(data2)
print('prod():\n', df2.prod())

# 11.cumsum()示例
# 累计求和
print('cumsum():\n', df2.cumsum())
#    Item1  Item2
# 0   20.0   4.23
# 1   40.0   7.47
# 2   62.0  11.45

# 12.cumprod()示例
# 累计乘积
print('cumprod():\n', df2.cumprod())

# 13.累计求最大或最小
print('cummax():\n', df2.cummax())
print('cummin():\n', df2.cummin())

# 14.count()用法
# 非空观测数量
print('count():\n', df2.count())