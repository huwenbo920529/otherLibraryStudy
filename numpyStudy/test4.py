#_*_coding:utf-8_*_
# 线性代数
# 简单数组运算
# 参考numpy文件夹中的linalg.py获得更多信息
# numpy.linalg中的逆矩阵函数inv函数、行列式det函数、求解线性方程组的solve函数、内积dot函数、
# 特征分解eigvals函数、eig函数、奇异值分解svd函数、广义逆矩阵的pinv函数
from numpy import *
from numpy.linalg import *
a=array([[1.0,2.0],[3.0,4.0]])
print a
print a.transpose()
print "a的逆：",inv(a)#a的逆矩阵
print "a的行列式：",det(a)
print "a的奇异值分解：",svd(a)
print "a的特征值：",eigvals(a)
print "a的特征向量与对应的特征值：",eig(a)

u=eye(2)#2行2列单位矩阵
print u
print trace(u)#矩阵的迹，主对角线元素之和

j = array([[0.0, -1.0], [1.0, 0.0]])
print dot(j,j)

y=array([[5],[7]])
print solve(a,y)#求解线性方程ax=y


# 矩阵类
# 这是一个关于矩阵类的简短介绍。
A=matrix('1.0 2.0;3.0 4.0')
X=matrix('5.0 7.0')
print A
print A.T#返回A的转置矩阵,A本身不变
Y=X.T
print A*Y#矩阵乘法

print A.I#返回矩阵A的逆
print solve(A,Y)


# 索引：比较矩阵和二维数组
# 注意NumPy中数组和矩阵有些重要的区别。NumPy提供了两个基本的对象：
# 一个N维数组对象和一个通用函数对象。其它对象都是建构在它们之上 的。
# 特别的，矩阵是继承自NumPy数组对象的二维数组对象。
# 对数组和矩阵，索引都必须包含合适的一个或多个这些组合：整数标量、省略号 (ellipses)、整数列表;布尔值，整数或布尔值构成的元组，和一个一维整数或布尔值数组。
# 矩阵可以被用作矩阵的索引，但是通常需要数组、列表或者 其它形式来完成这个任务。

# 像平常在Python中一样，索引是从0开始的。传统上我们用矩形的行和列表示一个二维数组或矩阵，
# 其中沿着0轴的方向被穿过的称作行，沿着1轴的方向被穿过的是列。
A=arange(12)
A.shape=(3,4)
M=mat(A.copy())#mat函数创建矩阵时，若输入已经为matrix或ndarray对象，则不会为它们创建副本。因此，调用mat函数和调用matrix(data, copy=False)等价。在创建矩阵的专用字符串中，矩阵的行与行之间用分号隔开，行内的元素之间用空格隔开。
print A
print M

# 现在，让我们简单的切几片。基本的切片使用切片对象或整数。例如， A[:] 和 M[:] 的求值将表现得和Python索引很相似。
# 然而要注意很重要的一点就是NumPy切片数组 不创建数据的副本;切片提供统一数据的视图。
print A[:,1],A[:,1].shape  #[1 5 9] (3L,)
print M[:,1],M[:,1].shape  #[1 5 9] (3L,1L)
# #注意最后两个结果的不同。对二维数组使用一个冒号产生一个一维数组，
# 然而矩阵产生了一个二维矩阵。