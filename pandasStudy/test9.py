# -*- coding:utf-8 -*-
# Pandas排序
# Pandas有两种排序方式，它们分别是 -
# 按标签
# 按实际值

import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
print(unsorted_df)

# 按行标签排序
# 使用sort_index()方法，通过传递axis参数和排序顺序，可以对DataFrame进行排序。
# 默认情况下，按照升序对行标签进行排序。
sorted_df = unsorted_df.sort_index()
print(sorted_df)

# 按列标签排列
# 通过传递axis参数值为0或1，可以对列标签进行排序。 默认情况下，axis = 0，逐行排列
sorted_df = unsorted_df.sort_index(axis=1)
print(sorted_df)

# 按值排序
# 像索引排序一样，sort_values()是按值排序的方法。它接受一个by参数，它将使用要与其排序值的DataFrame的列名称
sorted_df = unsorted_df.sort_values(by='col1')
print(sorted_df)

sorted_df = unsorted_df.sort_values(by=['col1', 'col2'])
print(sorted_df)

# 排序算法
# sort_values()提供了从mergeesort，heapsort和quicksort中选择算法的一个配置。Mergesort是唯一稳定的算法。
orted_df = unsorted_df.sort_values(by='col1', kind='mergesort')
print(sorted_df)
