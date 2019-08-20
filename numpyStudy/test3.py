#_*_coding:utf-8_*_

# 复制和视图
# 当运算和处理数组时，它们的数据有时被拷贝到新的数组有时不是。这通常是新手的困惑之源。这有三种情况:
# 完全不拷贝
# 简单的赋值不拷贝数组对象或它们的数据。
from numpy import *
a=arange(12)
b=a
print b is a #True
b.shape=(3,4)
print b
print a.shape#(3L, 4L)

# 视图(view)和浅复制
# 不同的数组对象分享同一个数据。视图方法创造一个新的数组对象指向同一数据。
c=a.view()
print c is a#False
print c.flags.owndata#False
c.shape=(2,6)
print c
print a.shape#(3L, 4L)
c[0,4]=100#c的第一行带5个元素修改为100
print a#a中元素的值发生变化
print c


# 切片数组返回它的一个视图
s=a[:,1:3]
print s
s[:]=10
print s
print a


# 深复制
# 这个复制方法完全复制数组和它的数据。
d=a.copy()
print d is a#False
print d.base is a#False
d[0,0]=999
print d
print a#a的元素不会因为d的改变而改变





# 函数和方法(method)总览
# 这是个NumPy函数和方法分类排列目录。这些名字链接到 NumPy示例 ,你可以看到这些函数起作用。[^5]

# 创建数组
# arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r , zeros, zeros_like
# 转化
# astype, atleast 1d, atleast 2d, atleast 3d, mat
# 操作
# array split, column stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
# 询问
# all, any, nonzero, where
# 排序
# argmax, argmin, argsort, max, min, ptp, searchsorted, sort
# 运算
# choose, compress, cumprod, cumsum, inner, fill, imag, prod, put, putmask, real, sum
# 基本统计
# cov, mean, std, var
# 基本线性代数
# cross, dot, outer, svd, vdot