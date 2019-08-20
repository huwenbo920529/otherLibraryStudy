# -*- coding:utf-8 -*-
# Pandas面板（Panel）
# 面板(Panel)是3D容器的数据。面板数据一词来源于计量经济学，部分源于名称：Pandas - pan(el)-da(ta)-s。
# 3轴(axis)这个名称旨在给出描述涉及面板数据的操作的一些语义。它们是 -
# items - axis 0，每个项目对应于内部包含的数据帧(DataFrame)。
# major_axis - axis 1，它是每个数据帧(DataFrame)的索引(行)。
# minor_axis - axis 2，它是每个数据帧(DataFrame)的列。
# pandas.Panel()
# 可以使用以下构造函数创建面板 -
# pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
# Python
# 构造函数的参数如下 -
# 参数	    描述
# data	    数据采取各种形式，如：ndarray，series，map，lists，dict，constant和另一个数据帧(DataFrame)
# items	    axis=0
# major_axis	axis=1
# minor_axis	axis=2
# dtype	    每列的数据类型
# copy	    复制数据，默认 - false
# 创建面板
# 可以使用多种方式创建面板 -
# 从ndarrays创建
# 从DataFrames的dict创建

import pandas as pd
import numpy as np

# 1.创建一个空面板
p1 = pd.Panel()
print(p1)

# 2.从3Dndarray创建
data = np.random.rand(2, 4, 5)
p2 = pd.Panel(data)
print(p2)

# 3.从DataFrame对象的dict创建面板
data = {'Item1': pd.DataFrame(np.random.randn(4, 3)),
        'Item2': pd.DataFrame(np.random.randn(4, 2))}
p3 = pd.Panel(data)
print(p3)

# 4.从面板中选择数据
# 要从面板中选择数据，可以使用以下方式 -
# Items
# Major_axis
# Minor_axis
data = {'Item1': pd.DataFrame(np.array([i for i in range(12)]).reshape(4, 3)),
        'Item2': pd.DataFrame(np.array([i for i in range(8)]).reshape(4, 2))}
p = pd.Panel(data)
print(p['Item1'])
print(p['Item2'])
print(p.major_xs(0))  # 每个Item的第1行
print(p.minor_xs(0))  # 每个Item的第1列
