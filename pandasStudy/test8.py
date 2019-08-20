# -*- coding:utf-8 -*-
# Pandas迭代
# Pandas对象之间的基本迭代的行为取决于类型。当迭代一个系列时，它被视为数组式，基本迭代产生这些值。
# 其他数据结构，如：DataFrame和Panel，遵循类似惯例迭代对象的键。
# 简而言之，基本迭代(对于i在对象中)产生 -
    # Series - 值
    # DataFrame - 列标签
    # Pannel - 项目标签

# 注意 - 不要尝试在迭代时修改任何对象。
# 迭代是用于读取，迭代器返回原始对象(视图)的副本，因此更改将不会反映在原始对象上。

import pandas as pd
import numpy as np

# 迭代DataFrame
# 迭代DataFrame提供列名
N = 20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N-1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })
for col in df:
   print(col)



# 要遍历数据帧(DataFrame)中的行，可以使用以下函数 -
    # iteritems() - 迭代(key，value)对
    # iterrows() - 将行迭代为(索引，系列)对
    # itertuples() - 以namedtuples的形式迭代行
df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])
for (key, value) in df.iteritems():
    print(type(key), type(value), len(key), len(value))
    print(key,':\n',value)#key是列名，value是DataFrame类型

# iterrows()示例
# iterrows()返回迭代器，产生每个索引值以及包含每行数据的序列。
for row_index,row in df.iterrows():
    print(type(row_index), type(row))
    print(row_index, row)

# itertuples()方法将为DataFrame中的每一行返回一个产生一个命名元组的迭代器。
# 元组的第一个元素将是行的相应索引值，而剩余的值是行值
for row in df.itertuples():
    print(type(row))
    print (row)