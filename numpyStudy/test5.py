#_*_coding:utf-8_*_
from numpy import *
from numpy.linalg import *
A=arange(12).reshape((3, 4))
print(A)#A是一个数组，区别于矩阵

# 假如我们想要一个数组的第一列和第三列，一种方法是使用列表切片：
print(A[:,[1,3]])
# 稍微复杂点的方法是使用 take() 方法(method):
print(A[:,].take([1,3],axis=1))

# 如果我们想跳过第一行，我们可以这样：
print(A[1:,[1,3]])
#或者使用以下语句
print(A[1:,].take([1,3],axis=1))
#h也可以用以下方法
print(A[ix_((1,2),(1,3))])


# 现在让我们做些更复杂的。比如说我们想要保留第一行大于1的列。
# 一种方法是创建布尔索引
print(A[0,:]>1)#[False False  True  True]
print(A[:,A[0,:]>1])#数组的最后两列


# 但是索引矩阵没这么方便。
M=mat(A.copy())
print(M[0,:]>1) #[[False False  True  True]]注意与上面数组的区别
# 这个过程的问题是用“矩阵切片”来切片产生一个矩阵 ，
# 但是矩阵有个方便的 A 属性，它的值是数组呈现的。所以我们仅仅做以下替代：
print(M[:,M.A[0,:]>1])


# 如果我们想要在矩阵两个方向有条件地切片，我们必须稍微调整策略，代之以：
print(A[A[:,0]>2,A[0,:]>1])  #[ 6 11]
print(M[M.A[:,0]>2,M.A[0,:]>1])#[[ 6 11]]

#以上结果不是我们所期望的结果
# 我们需要使用向量积 ix_ :
print(A[ix_(A[:,0]>2,A[0,:]>1)])
print(M[ix_(M.A[:, 0] > 2, M.A[0, :] > 1)])#这两条语句的结果等价




import numpy
import pylab
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = numpy.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
pylab.hist(v, bins=50, normed=1)       # matplotlib version (plot)
pylab.show()
# Compute the histogram with numpy and then plot it
(n, bins) = numpy.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
pylab.plot(.5*(bins[1:]+bins[:-1]), n)
pylab.show()