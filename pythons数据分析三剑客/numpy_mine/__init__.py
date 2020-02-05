"""
Numpy:
    numpy(numeric python)是Python的开源数字扩展，定义了数值数组和矩阵类型，以及基本运算的语言扩展，可用于矩阵数据、矢量处理等。

pip安装: pip install numpy

numpy使用：
    1.创建数组
        创建数组有4种方式：array,arange,linspace,logspace
        *** array：
            array将元组或列表作为参数，创建一个一维或多维数组，如array([1,2,3])
        *** arange:
            arange与range类似，功能比range更强大，arange也接收三个参数start、end、step，但arange的step可以是浮点数
        *** linspace
            linspace三个主要参数，start、stop、num，返回首项是start，末项是stop，共num项的等差序列
        *** logspace
            logspace三个主要参数，start、stop、num，返回首项是10的start次方，末项是10的stop次方，共num项的等比序列
    2.索引与切片
        与列表元组类似，numpy一维或多维数组也有索引和切片，但比元组和列表的要更灵活

    3.矩阵

    4.numpy.ndarray类型属性及注意事项
        属性：
            *** ndim    数组的维度
            *** shape   数组的各维度，类型是元组
            *** size    数组元素个数，各维度乘积
            *** dtype   数据元素类型
            *** itemsize    数据元素字节数
            *** data    数据存放地址
        注意事项：
            *** 以二维数组为例，当数组每行列数不同时（各行不定长），dim = 1,shape = (行数,)被视为一维数组。
                此时使用切片[0,0:2]时会有indexError异常,并且无法获取size属性。
            *** ndarray会自动转换类型，如[1,2,3]的dtype = int32，而[1,2,3.0]的dtype = float64，[1,2,"3"] 的dtype = <U11，
                至于转换原因，那肯定是为了不丢失有效数据位
            *** transpose(*axes):
                原码注释：
                    axes : None, tuple of ints, or `n` ints

                    * None or no argument: reverses the order of the axes.

                    * tuple of ints: `i` in the `j`-th place in the tuple means `a`'s
                    `i`-th axis becomes `a.transpose()`'s `j`-th axis.

                    * `n` ints: same as an n-tuple of the same ints (this form is
                    ntended simply as a "convenience" alternative to the tuple form)
                意思是：
                    **  不给出axes默认反转整个shape元组，也就是说a*b*c*d....*n的多维矩阵会被转置为n*...*d*c*b*a的矩阵
                        以二维矩阵为例3*4的矩阵会被转置为4*3的矩阵，对应transpose(1,0)或者transpose()
                    **  给出axes,axes是个元组，如axes = （1,2,0）这个意思是将shape[0]放置到shape[2]后面，如shape为（1,2,3）就会变成
                    （2,3,1），也即1*2*3原矩阵会变成2*3*1矩阵
"""
import numpy as np

if __name__ == "__main__":
    # 1.创建数组
    array_mine = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [7, 8, 9, 10]])
    arange_mine = np.arange(1, 3, 0.2)
    linspace_mine = np.linspace(1, 10, 10)
    logspace_mine = np.logspace(0, 6, 7)

    print("array_mine = \n" + str(array_mine) + "\ntype = " + str(type(array_mine)))
    print("arange_mine = " + str(arange_mine) + "          type = " + str(type(arange_mine)))
    print("linspace_mine = " + str(linspace_mine) + "          type = " + str(type(linspace_mine)))
    print("logspace_mine = " + str(logspace_mine) + "          type = " + str(type(logspace_mine)))

    print("\n\n")
    # 2.索引和切片 以array_mine为例

    # 选取全部元素 array_mine[:] == array_mine
    print("选取全部元素 array_mine[:] = {}".format(array_mine[:]))

    # 选取第0行
    print("选取第0行 array_mine[0] = {}".format(array_mine[0]))

    # 选取0~2行，不包括第2行
    print("选取0~2行，不包括第2行 array_mine[0:2] = {}".format(array_mine[0:2]))

    # 选取第0行下标0~2，不包括2
    print("选取第0行下标0~2，不包括2 = {}".format(array_mine[0, 0:2]))

    # 选取第1行第1列
    print("选取第1行第1列  = {} ".format(array_mine[1, 1]))

    # 按条件截取
    print("选中array_mine中所有大于5的元素 = {}".format(array_mine[array_mine > 5]))
    # 甚至可以给大于5的元素赋值，如    array_mine[array_mine>5] = 0
    print("比较array_mine中每一个值 a>5 = \n{}".format(array_mine > 5))

    # 矩阵运算
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [7, 8, 9, 10]])
    # 加减乘除模幂,与寻常运算并无差别，加减乘除模都是项对项，与数学的矩阵相乘不同，
    # 类型转换需得注意，比如只要有一个运算结果为float，那么真个矩阵全部元素都会变成float
    print("array_mine*array = \n{}".format(array_mine * array))
    print("array**2 = \n{}".format(array ** 2))

    # 矩阵点乘，即线代中的矩阵相乘,将array重塑为4*3的矩阵以满足矩阵相乘
    print("矩阵点乘:\n{}".format(array_mine.dot(array.reshape(4, 3))))

    # 矩阵转置
    print("矩阵转置:\n{}".format(array_mine.transpose()))

    # 求逆矩阵
    print("求逆矩阵:\n{}".format(np.linalg.inv(np.array([[1, 2], [3, 4]]))))
