# -*- coding:utf-8 -*-
# 数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列。
# 数据帧(DataFrame)的功能特点：
    # 潜在的列是不同的类型
    # 大小可变
    # 标记轴(行和列)
    # 可以对行和列执行算术运算

# pandas.DataFrame
# pandas中的DataFrame可以使用以下构造函数创建 -
# pandas.DataFrame( data, index, columns, dtype, copy)
# 编号	参数	描述
# 1	    data	数据采取各种形式，如:ndarray，series，map，lists，dict，constant和另一个DataFrame。
# 2	    index	对于行标签，要用于结果帧的索引是可选缺省值np.arrange(n)，如果没有传递索引值。
# 3	    columns	对于列标签，可选的默认语法是 - np.arange(n)。 这只有在没有索引传递的情况下才是这样。
# 4	    dtype	每列的数据类型。
# 5	    copy	如果默认值为False，则此命令(或任何它)用于复制数据。

# Pandas数据帧(DataFrame)可以使用各种输入创建，如 -
# 列表
# 字典
# 系列
# Numpy ndarrays
# 另一个数据帧(DataFrame)

import pandas as pd

# 1.创建一个空的DataFrame
df1 = pd.DataFrame()
print(type(df1))

# 2.从列表创建DataFrame
data2 = [1, 2, 3, 4, 5]
df2 = pd.DataFrame(data2)
print(df2)

data2 = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df2 = pd.DataFrame(data2, columns=['Name', 'Age'])
print(df2)

# 3.从ndarrays/Lists的字典来创建DataFrame
# 所有的ndarrays必须具有相同的长度。如果传递了索引(index)，则索引的长度应等于数组的长度。
# 如果没有传递索引，则默认情况下，索引将为range(n)，其中n为数组长度。
data3 = {'name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'age': [28, 34, 29, 42]}
df3 = pd.DataFrame(data3)
print(df3)

# 4.从列表列表创建数据帧DataFrame
data4 = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}]
df4 = pd.DataFrame(data4)
print(df4)

# 5.列选择
data5 = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
         'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df5 = pd.DataFrame(data5)
print(df5['one'])

# 6.列添加
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df6 = pd.DataFrame(d)
df6['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df6)
df6['four'] = df6['one'] + df6['two']
print(df6)

# 7.列删除
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df7 = pd.DataFrame(d)
del(df7['one'])#等同于df7.pop('one')
print(df7)

# 8.行选择，添加和删除
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df8 = pd.DataFrame(d)
print(df8.loc['b'])
# 按整数位置选择
# 可以通过将整数位置传递给iloc()函数来选择行。
print(df8.iloc[0])

# 9.行切片
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df9 = pd.DataFrame(d)
print(df9[2:4])

# 10.附加行
# 使用append()函数将新行添加到DataFrame
df10_1 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df10_2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df10_3 = df10_1.append(df10_2)  # df9_1的值并没有改变
print(df10_1)
print(df10_3)  # 结果如下，可以看出行标签照搬过去了，这样就出现行标签相同的行了
#    a  b
# 0  1  2
# 1  3  4
# 0  5  6
# 1  7  8

# 11.删除行
# 使用索引标签从DataFrame中删除或删除行。 如果标签重复，则会删除多行。
# 如果有注意，在上述示例中，有标签是重复的。这里再多放一个标签，看看有多少行被删除。
df11 = df10_3.drop(0)
print(df11)
