# _*_coding:utf-8_*_
# NumPy的主要对象是同种元素的多维数组。
# 这是一个所有的元素都是一种类型、通过一个正整数元组索引的元素表格(通常是元素是数字)。
# 在NumPy中维度(dimensions)叫做轴(axes)，轴的个数叫做秩(rank)。

# NumPy的数组类被称作 ndarray 。通常被称作数组。注意numpy.array和标准Python库类array.array并不相同，
# 后者只处理一维数组和提供少量功能。更多重要ndarray对象属性有：
# ndarray.ndim:数组轴的个数，在python的世界中，轴的个数被称作秩
# ndarray.shape:数组的维度。这是一个指示数组在每个维度上大小的整数元组。例如一个n排m列的矩阵，它的shape属性将是(2,3),这个元组的长度显然是秩，即维度或者ndim属性
# ndarray.size:数组元素的总个数，等于shape属性中元组元素的乘积。
# ndarray.dtype:一个用来描述数组中元素类型的对象，可以通过创造或指定dtype使用标准Python类型。另外NumPy提供它自己的数据类型。
# ndarray.itemsize:数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(=64/8),又如，一个元素类型为complex32的数组item属性为4(=32/8).
# ndarray.data:包含实际数组元素的缓冲区，通常我们不需要使用这个属性，因为我们总是通过索引来使用数组中的元素。

from numpy import *

a = arange(15)
print(a)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(a.shape)  # (15L,)
b = a.reshape(3, 5)
print(b)  # [[ 0  1  2  3  4],[ 5  6  7  8  9],[10 11 12 13 14]]
print(b.shape)  # (3L, 5L)
print(b.ndim)  # 2
print(b.dtype)  # int32
print(b.size)  # 15
print(type(b))  # <type 'numpy.ndarray'>

# 创建数组
# 有好几种创建数组的方法。
# 例如，你可以使用 array 函数从常规的Python列表和元组创造数组。
# 所创建的数组类型由原序列中的元素类型推导而来。
a1 = array([1, 2, 3, 4])
a2 = array((2, 3, 4, 5))
print(a1, a2)
b1 = array([[1.2, 3.0, 5.7], [2.1, 4.2, 6.3]])
b2 = array([(1.5, 2, 3), (4, 5, 6)])
b3 = array(((2., 3.1, 4.2), (3.7, 5.2, 9.2)))
print(b1)
print(b2)
print(b3)

# 函数 zeros创建一个全是0的数组，函数 ones 创建一个全1的数组，
# 函数 empty 创建一个内容随机并且依赖与内存状态的数组。
# 默认创建的数组类型(dtype)都是float64。
c1 = zeros((2, 3))
print(c1, c1.dtype)
c2 = ones((2, 3, 4))
print(c2, c2.dtype)
c3 = empty((2, 3))
print(c3, c3.dtype)

# 为了创建一个数列，NumPy提供一个类似arange的函数返回数组而不是列表:
# 1、range多用作循环，range（0,10）返回一个range对象，如想返回一个list，前面加上list转换；
# 2、arange是numpy模块中的函数，使用前需要先导入此模块，arange(3):返回array类型对象。
# 【注：range()中的步长不能为小数，但是np.arange()中的步长可以为小数】
# 3、xrange()也是用作循环，只是xrang(0,10)不返回list，返回xrange对象。每次调用返回其中的一个值。 
# 返回很大的数的时候或者频繁的需要break时候，xrange性能更好。【注意：python3.x中把xrange()取消了】
a3 = arange(5, 20, 5)
print(a3)  # [ 5 10 15]
a4 = arange(0, 2, 0.3)
print(a4)  # [ 0.   0.3  0.6  0.9  1.2  1.5  1.8]

# 其它函数array, zeros, zeros_like, ones, ones_like,
# empty, empty_like, arange, linspace, rand, randn, fromfunction, fromfile
