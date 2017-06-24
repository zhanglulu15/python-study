import numpy as np

# sigmoid function
# deriv=ture 是求的是导数
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([  [0,0,1],
                [1,1,1],
                [1,0,1],
                [0,1,1] ])   #输入数据集，形式为矩阵，每 1 行代表 1 个训练样本。

# output dataset
y = np.array([[0,1,1,0]]).T   #输出数据集，形式为矩阵，每 1 行代表 1 个训练样本。

# seed random numbers to make calculation
np.random.seed(1)

# initialize weights randomly with mean 0  以平均值0随机初始化权重
syn0 = 2*np.random.random((3,1)) - 1   #返回随机生成的一个实数,它在[0,1)范围内


# 迭代次数
for iter in range(10000):

    # forward propagation
    # l0也就是输入层,网络第 1 层，即网络输入层。
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))   #网络第 2 层，常称作隐藏层。

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)   #第一层权值，突触 0 ，连接 l0 层与 l1 层。
    #  x.dot(y) 若 x 和 y 为向量，则进行点积操作；若均为矩阵，则进行矩阵相乘操作；若其中之一为矩阵，则进行向量与矩阵相乘操作。

print ("Output After Training:",l1)



