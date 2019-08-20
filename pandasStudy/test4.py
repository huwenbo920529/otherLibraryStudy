# -*- coding:utf-8 -*-
# Pandas基本功能

# 一、系列基本功能
# 编号	属性或方法	描述
# 1	    axes	    返回行轴标签列表。
# 2	    dtype	    返回对象的数据类型(dtype)。
# 3	    empty	    如果系列为空，则返回True。
# 4	    ndim	    返回底层数据的维数，默认定义：1。
# 5	    size	    返回基础数据中的元素数。
# 6	    values	    将系列作为ndarray返回。
# 7	    head()	    返回前n行。
# 8	    tail()	    返回最后n行。

import pandas as pd
import numpy as np
s = pd.Series(np.random.rand(4))
print(s)
print('axes:', s.axes)
print('dtype:', s.dtype)
print('empty:', s.empty)
print('ndim:', s.ndim)
print('size:', s.size)
print('values:', s.values)
print('head(2):\n', s.head(2))
print('tail(2):\n', s.tail(2))

# 二、DataFrame基本功能
# 编号	属性或方法	描述
# 1	    T	        转置行和列。
# 2	    axes	    返回一个列，行轴标签和列轴标签作为唯一的成员。
# 3	    dtypes	    返回此对象中的数据类型(dtypes)。
# 4	    empty	    如果NDFrame完全为空[无项目]，则返回为True; 如果任何轴的长度为0。
# 5	    ndim	    轴/数组维度大小。
# 6	    shape	    返回表示DataFrame的维度的元组。
# 7	    size	    NDFrame中的元素数。
# 8	    values	    NDFrame的Numpy表示。
# 9	    head()	    返回开头前n行。
# 10	tail()	    返回最后n行。

data = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack']),
        'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
        'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
df = pd.DataFrame(data)
print(df)
print('T:\n', df.T)
print('axes:\n', df.axes)
print('dtype:\n', df.astype)
print('empty:', df.empty)
print('ndim:', df.ndim)
print('shape:', df.shape)
print('size:', df.size)
print('values:\n', df.values)
print('head(2):\n', s.head(2))
print('tail(2):\n', s.tail(2))
