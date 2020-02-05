"""
Numpy:
    numpy(numeric python)是Python的开源数字扩展，定义了数值数组和矩阵类型，以及基本运算的语言扩展，可用于矩阵数据、矢量处理等。

pip安装: pip install numpy

numpy使用：
    1.创建数组
        创建数组有4种方式：array,arrange,linspace,logspace
        *** array：
            array将元组或列表作为参数，创建一个一维或多维数组，如array([1,2,3])
        *** arrange:
            arrange与range类似，功能比range更强大，arrange也接收三个参数start、end、step，但arrange的step可以是浮点数
        *** linspace
            linspace接受三个参数，start、end、step，返回首项是start，末项是end，等差是step的等差序列
        *** logspace
            logspace接收三个参数，start、end、step，返回首项是10的start次方，末项是10的end次方，等比是step的等比序列
    2.索引与切片
        与列表元组类似，numpy一维或多维数组也有索引和切片，但比元组和列表的要更灵活

"""
from pandas.tests.io.json.test_ujson import numpy


if __name__ == "__main__":
    array_mine =