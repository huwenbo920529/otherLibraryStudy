# -*- coding:utf-8 -*-
# Pandas函数应用
# 要将自己或其他库的函数应用于Pandas对象，应该了解三种重要的方法。以下讨论了这些方法。
# 使用适当的方法取决于函数是否期望在整个DataFrame，行或列或元素上进行操作。
    # 表明智函数应用：pipe()
    # 行或列函数应用：apply()
    # 元素函数应用：applymap()

import pandas as pd
import numpy as np

# 1.表格函数应用
# 可以通过将函数和适当数量的参数作为管道参数来执行自定义操作。 因此，对整个DataFrame执行操作。
# 例如，为DataFrame中的所有元素相加一个值2
def adder(ele1, ele2):
   return ele1 + ele2
df = pd.DataFrame(np.array([i for i in range(6)]).reshape(2, 3), columns=['col1', 'col2', 'col3'])
print(df)
df = df.pipe(adder, 2)
print(df)

# 2.行或列智能函数应用
# 可以使用apply()方法沿DataFrame或Panel的轴应用任意函数，它与描述性统计方法一样，采用可选的轴参数。
# 默认情况下，操作按列执行，将每列列为数组。
df = pd.DataFrame(np.array([i for i in range(6)]).reshape(2, 3), columns=['col1', 'col2', 'col3'])
print(df.apply(np.mean))
print(df.apply(lambda x: x.max()-x.min()))
# 在自定义apply
def myapply(x):
    for i in range(1, len(x)):
        x[i] = x[i] + x[i-1]
    return x[len(x)-1]
print(df.apply(myapply))

# 3.元素智能函数应用
# 并不是所有的函数都可以向量化(也不是返回另一个数组的NumPy数组，也不是任何值)，
# 在DataFrame上的方法applymap()和类似地在Series上的map()接受任何Python函数，并且返回单个值。
df = pd.DataFrame(np.array([i for i in range(6)]).reshape(2, 3), columns=['col1', 'col2', 'col3'])
print(df)
print(df['col1'].map(lambda x: x * 10))# Series上的map()
print(df.applymap(lambda x: x * 10)) #DataFrame上的applymap()