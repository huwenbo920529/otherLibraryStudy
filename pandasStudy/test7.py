# -*- coding:utf-8 -*-
# Pandas重建索引
# 重新索引会更改DataFrame的行标签和列标签。重新索引意味着符合数据以匹配特定轴上的一组给定的标签。
# 可以通过索引来实现多个操作 -
    # 重新排序现有数据以匹配一组新的标签。
    # 在没有标签数据的标签位置插入缺失值(NA)标记。
import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame({
   'A': pd.date_range(start='2017-01-01', periods=N, freq='D'),
   'x': np.linspace(0, stop=N-1, num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print(df_reindexed)

# 2.重建索引与其他对象对齐
df1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])
df1 = df1.reindex_like(df2)
print(df1)

# 3.填充时重新加注
# reindex()采用可选参数方法，它是一个填充方法，其值如下：
    # pad/ffill - 向前填充值
    # bfill/backfill - 向后填充值
    # nearest - 从最近的索引值填充
df1 = pd.DataFrame(np.array([i for i in range(12)]).reshape(4, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.array([i for i in range(5, 11)]).reshape(2, 3), columns=['col1', 'col2', 'col3'])
df3 = df2.reindex_like(df1, method='ffill')
df4 = df2.reindex_like(df1, method='bfill')
df5 = df2.reindex_like(df1, method='nearest')
print(df3)
print(df4)
print(df5)

# 4.重建索引时的填充限制
# 限制参数在重建索引时提供对填充的额外控制。限制指定连续匹配的最大计数。
print(df2.reindex_like(df1))
print(df2.reindex_like(df1, method='ffill', limit=1))

# 5.重命名
# rename()方法允许基于一些映射(字典或者系列)或任意函数来重新标记一个轴
df1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
print(df1)
print(df1.rename(columns={'col1': 'c1', 'col2': 'c2'}, index={0: 'apple', 1: 'banana', 2: 'durian'}))
# rename()方法提供了一个inplace命名参数，默认为False并复制底层数据。 指定传递inplace = True则表示将数据重命名。