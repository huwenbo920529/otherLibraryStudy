# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# 1.通过传递值列表来创建一个系列，让Pandas创建一个默认的整数索引
print('Seris:\n')
s = pd.Series([1, 2, 3, np.NaN, 5])
print(s, type(s))

# 2.使用datetime索引,创建一个DataFrame
print('date_range:\n')
dates = pd.date_range(start='20170101', periods=4, freq='D')
print(dates)

# 3.使用numpy数组h和前面的dates，及标记来创建DataFrame
print('DataFrame:\n')
df = pd.DataFrame(np.random.randn(4, 5), index=dates, columns=list('ABCDE'))
print(df)

# 4.通过传递可以转换为类似系列的对象的字典来创建DataFrame
print('DataFrame2:\n')
df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20180206'),
    'C': np.array([3]*4, dtype='int32'),
    'D': pd.Series(1, index=list(range(4)), dtype='float32'),
    'E': pd.Categorical(["test", "train", "test", "predict"]),
    'F': 'foo'
})
print(df2)

# 5.查看数据
# 查看框架的顶部和底部的数据行
print(df.head(n=3)) #默认n=5
print(df.tail(n=3)) #默认n=5
# 显示索引，列和底层numpy数据
print('df.index:\n', df.index)
print('df.columns:\n', df.columns)
print('df.values:\n', df.values)
# 描述显示数据的快速统计摘要
print('df.describe():\n', df.describe())

# 6.数据转置
print('df.T:\n', df.T)

# 7.排序
# 通过轴排序
print('轴排序:\n', df.sort_index(axis=1, ascending=False))# 横轴降序
# 通过值排序
print('值排序:\n', df.sort_values(by='B', ascending=False)) #'B'列的值降序

# 8.选择区块
# 获取
print('df.A:\n', df.A)#相当于df['A']
# 选择通过[]操作符，选择切片行
print('df[0:3]:\n', df[0:3])
print('指定选择日期:\n', df['20170101':'20170103'])

# 9.按标签选择
# 使用标签获取横截面
print('loc1:\n', df.loc[dates[0]])
# 通过标签选择多轴
print('loc2:\n', df.loc[:, ['A', 'D']])
# 显示标签切片，包括两个端点
print('loc3:\n', df.loc['20170101':'20170103', ['A', 'E']])
# 获得标量值
print('loc4:\n', df.loc['20170103', 'A'])
# 快速访问标量(等同于先前的方法)
print('at:\n', df.at[dates[0], 'A'])

# 10.通过位置选择
print('iloc1:\n', df.iloc[3]) #第四行的值
# 通过整数切片，类似于numpy/python
print('iloc2:\n', df.iloc[1:3, 2:4])
# 通过整数位置的列表，类似于numpy/python样式
print('iloc3:\n', df.iloc[[0, 2, 3], [1, 3, 4]])
# 明确切片
print('iloc4:\n', df.iloc[1,1])
# 要快速访问标量(等同于先前的方法)
print('iat:\n', df.iat[1, 1])

# 11.布尔索引
# 使用单列的值来选择数据
print('df[df.A>0]:\n', df[df.A > 0])
# 从满足布尔条件的DataFrame中选择值
print('df[df>0]:\n', df[df > 0])
# 使用isin()方法进行过滤
print('isin()方法:\n', df2[df2['E'].isin(['test', 'predict'])])