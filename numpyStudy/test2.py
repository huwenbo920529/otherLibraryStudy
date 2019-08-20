#_*_coding:utf-8_*_
# 形状操作
# 更改数组的形状
# 一个数组的形状由它每个轴上的元素个数给出：
from numpy import *
import math
a= floor(10*random.random((3,4)))# int（）函数直接截去小数部分# floor（） 得到最接近原数但是小于原数的部分# round()得到最接近原数的整数（返回为浮点类型）
print a
print a.shape

#一个数组的形状可以被多种命令修改
print a.ravel()#a本身不变，只是将a中的元素展平输出成一维

a.shape=(6,2)
a.transpose()#transpose的操作依赖于shape参数
print a


# reshape 函数改变参数形状并返回它，而 resize 函数改变数组自身
a=array([1,2,3,4,5,6,7,8])
a.reshape((2,4))
print a#a没有被改变
a.resize((2,4))
print a#a被改变了


# 组合(stack)不同的数组
# 几种方法可以沿不同轴将数组堆叠在一起：
a=floor(10*random.random((2,3)))
b=floor(10*random.random((2,3)))
print a
print b
print vstack((a,b))
print hstack((a,b))


#函数 row_stack 以行将一维数组合成二维数组，它等同与 vstack 对一维数组。
print row_stack((a,b))
#函数 column_stack 以列将一维数组合成二维数组，它等同与 hstack 对一维数组。
print column_stack((a,b))

a1=array([1,2,3])
a2=array([4,5,6])
print a1,a2
print row_stack((a1,a2))
print column_stack((a1,a2))

# 对那些维度比二维更高的数组， hstack 沿着第二个轴组合， vstack 沿着第一个轴组合,
# concatenate 允许可选参数给出组合时沿着的轴。



# np.newaxis分别是在行或列上增加维度，原来是（6，）的数组，
# 在行上增加维度变成（1,6）的二维数组，
# 在列上增加维度变为(6,1)的二维数组
a=array([1,2,3])
b=a[newaxis,:]
c=a[:,newaxis]
print a,a.shape#[1 2 3]  (3L,)
print b,b.shape#[[1 2 3]]  (1L,3L)
print c,c.shape#[[1] [2] [3]]  (3L,1L)


# 在复杂情况下， r_[] 和 c_[] 对创建沿着一个方向组合的数很有用，
# 它们允许范围符号(“:”):
# 当使用数组作为参数时， r_ 和 c_ 的默认行为和 vstack 和 hstack 很像，
# 但是允许可选的参数给出组合所沿着的轴的代号。
a=r_[1:7,0,4]
print a #[1 2 3 4 5 6 0 4]


# 将一个数组分割(split)成几个小数组
# 使用 hsplit 你能将数组沿着它的水平轴分割，或者指定返回相同形状数组的个数，
# 或者指定在哪些列后发生分割:
# vsplit 沿着纵向的轴分割， array split 允许指定沿哪个轴分割。
a=floor(10*random.random((3,6)))
print a #[[ 0.  4.  1.  5.  1.  6.]  [ 3.  1.  8.  2.  9.  2.]  [ 1.  4.  0.  7.  3.  7.]]
print hsplit(a,3)#[array([[ 0.,  4.],[ 3.,  1.],[ 1.,  4.]]), array([[ 1.,  5.],[ 8.,  2.],[ 0.,  7.]]), array([[ 1.,  6.],[ 9.,  2.],[ 3.,  7.]])]
print hsplit(a,(3,4))#[array([[ 0.,  4.,  1.],[ 3.,  1.,  8.],[ 1.,  4.,  0.]]), array([[ 5.],[ 2.],[ 7.]]), array([[ 1.,  6.],[ 9.,  2.],[ 3.,  7.]])]
print vsplit(a,1)#[array([[ 0.,  4.,  1.,  5.,  1.,  6.], [ 3.,  1.,  8.,  2.,  9.,  2.],[ 1.,  4.,  0.,  7.,  3.,  7.]])]
print vsplit(a,(2,3))
print split(a,(2,3),axis=0)#等价于 vsplit(a,(2,3))
print split(a,(3,4),axis=1)#等价于 hsplit(a,(3,4))


