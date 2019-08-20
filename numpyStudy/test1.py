# _*_coding:utf-8_*_


from numpy import *
# 打印数组
# 当你打印一个数组，NumPy以类似嵌套列表的形式显示它，但是呈以下布局：
# 最后的轴从左到右打印
# 次后的轴从顶向下打印
# 剩下的轴从顶向下打印，每个切片通过一个空行与下一个隔开
# 一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表。
print arange(12).reshape((3,4))
print arange(24).reshape((2,3,4))
# print arange(10000)#如果一个数组用来打印太大了，NumPy自动省略中间部分而只打印角落


# 基本运算
# 数组的算术运算是按元素的。新的数组被创建并且被结果填充。
a1=arange(4)
a2=array([20,30,40,50])
a3=a2-a1
print "{}-{}={}".format(a2,a1,a3)


# 不像许多矩阵语言，NumPy中的乘法运算符 * 指示按元素计算，
# 矩阵乘法可以使用 dot 函数或创建矩阵对象实现
A=array([[1,1],[0,1]])
B=array([[2,0],[3,4]])
print A*B#[[2 0],[0 4]],只是对应元素相乘
print dot(A,B)#[[5 4],[3 4]]，真正意义上的矩阵的乘法


# 有些操作符像 += 和 *= 被用来更改已存在数组而不创建一个新的数组。
import math
a=ones((2,3),dtype=int)
b=random.random((2,3))
print a
print b
a*=3
b+=a
print a
print b


# 当运算的是不同类型的数组时，结果数组和更普遍和精确的已知(这种行为叫做upcast)。
a=ones(3,dtype=int32)
b=linspace(0,pi,3)#b.dtype=float64
c=a+b
print c
print "c.sum()=",c.sum()
print "c.min()=",c.min()
print "c.max()=",c.max()


# 指定 axis 参数你可以把运算应用到数组指定的轴上：
b=arange(12).reshape((3,-1))
print b.sum(axis=0)
print b.sum(axis=1)
print b.min(axis=0)
print b.min(axis=1)
print b.cumsum(axis=1)


# 通用函数(ufunc)
# NumPy提供常见的数学函数如 sin , cos 和 exp 。在NumPy中，这些叫作“通用函数”(ufunc)。
# 在NumPy里这些函数作用按数组的元素运算，产生一个数组作为输出。
B=arange(3)
C=array([2.,-1,4])
print B
print exp(B)
print sqrt(B)
print add(B,C)

#更多函数all, alltrue, any, apply along axis, argmax, argmin, argsort,
# verage,bincount, ceil, clip, conj, conjugate, corrcoef, cov, cross,
# cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum,
# mean, median, min, minimum, nonzero, outer, prod, re, round, sometrue,
#  sort, std, sum, trace, transpose, var, vdot, vectorize, where



# 索引，切片和迭代
# 一维数组可以被索引、切片和迭代，就像列表和其它Python序列
a=arange(10)**3
print a
print a[2],a[3:8]

a[:6:2]=-1000#equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
print a#从0到6号位置，每隔2个位置值改为-1000
print a[: :-1] # reversed a,只是将数组a逆序输出，数组a本身不变
for i in a:
    print i,


# 多维 数组可以每个轴有一个索引。这些索引由一个逗号分割的元组给出。
def f(x,y):
    return 10*x+y
b=fromfunction(f,(5,4),dtype=int)
print b
print b[0:5,1] #  each row in the second column of b
print b[1:3, :] # each column in the second and third row of b

#当少于轴数的索引被提供时，缺失的索引被认为是整个切片。
print b[-1]  #equivalent to the last row
print b[-1, :] # 与上面的语句等价


# b[i] 中括号中的表达式被当作 i 和一系列 : ，来代表剩下的轴。NumPy也允许你使用“点”像 b[i,...] 。
# 点 (…)代表许多产生一个完整的索引元组必要的分号。如果x是秩为5的数组(即它有5个轴)，那么:
# x[1,2,…] 等同于 x[1,2,:,:,:],
# x[…,3] 等同于 x[:,:,:,:,3]
# x[4,…,5,:] 等同 x[4,:,:,5,:].
c=arange(24).reshape(2,3,4)
print c
print c[0:1,0:2,0:3]
print c[0:1,:,0:3]


# 迭代 多维数组是就第一个轴而言的
a=arange(12).reshape(3,4)
for row in a:
    print row,#[0 1 2 3] [4 5 6 7] [ 8  9 10 11]
print "\n"
b=arange(8).reshape(2,2,2)
print b         #[[[0 1][2 3]] [[4 5][6 7]]]
for row in b:
    print row,#[[0 1] [2 3]]     [[4 5] [6 7]]


# 然而，如果一个人想对每个数组中元素进行运算，
# 我们可以使用flat属性，该属性是数组元素的一个迭代器:
for element in b.flat:
    print element,#0 1 2 3 4 5 6 7

# 更多[], …, newaxis, ndenumerate, indices, index exp