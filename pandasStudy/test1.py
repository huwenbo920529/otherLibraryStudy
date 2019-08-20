# -*- coding:utf-8 -*-
# pandas.Series:系列(Series)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组。
# 轴标签统称为索引。
# Pandas系列可以使用以下构造函数创建:
# pandas.DataFrame( data, index, dtype, copy)
# 编号	参数	    描述
# 1	    data	   数据采取各种形式，如：ndarray，list，constants
# 2	    index	   索引值必须是唯一的和散列的，与数据的长度相同。 默认np.arange(n)如果没有索引被传递。
# 3	    dtype	   dtype用于数据类型。如果没有，将推断数据类型
# 4	    copy	   复制数据，默认为false。
# 可以使用各种输入创建一个系列，如：数组、字典、标量值或常数

import pandas as pd
import numpy as np

# 1.创建一个空的系列：
s1 = pd.Series()
print(s1)  # Series([], dtype: float64)

# 2.从ndarray创建一个系列:如果数据是ndarray，则传递的索引必须具有相同的长度。
# 如果没有传递索引值，那么默认的索引将是范围(n)，其中n是数组长度
s2_1 = pd.Series(np.array(['a', 'b', 'c', 'd']))
s2_2 = pd.Series(np.array(['a', 'b', 'c', 'd']), index=[100, 101, 102, 103])
print(s2_1)
print(s2_2)

# 3.从字典创建一个系列
# 字典(dict)可以作为输入传递，如果没有指定索引，则按排序顺序取得字典键以构造索引。
# 如果传递了索引，索引中与标签对应的数据中的值将被拉出
data = {'a': 0., 'b': 1., 'c': 2.}
s3_1 = pd.Series(data)
s3_2 = pd.Series(data, index=['c', 'b', 'e', 'a'])
print(s3_1)
print(s3_2)

# 4.从标量创建一个系列
# 如果数据是标量值，则必须提供索引。将重复该值以匹配索引的长度
s4 = pd.Series(5, index=[0, 1, 2, 3])
print(s4)

# 5.从具有位置的系列中访问数据
s5 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s5[0])
print(s5[:3])
print(s5[-3:])

# 6.使用标签检索数据(索引)
# 一个系列就像一个固定大小的字典，可以通过索引标签获取和设置值。
print(s5['a'])
# 使用索引标签值列表检索多个元素
print(s5[['a', 'c', 'd']])
