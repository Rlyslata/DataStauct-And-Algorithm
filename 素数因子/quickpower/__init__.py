# 快速求幂
"""
原理：
    1、A**(2*M) == A**M**2
    2、A**（2+M) == A**2 * A**M

计算A的p次幂
    Float RaisePower(Float :A,Integer:P):
        <使用第一个法则快速计算A**1，A**2,A**4,A**8,以此类推,知道A**N,N+1>P>
        <利用这些A的幂，使用第二个法则计算A**p>
        return A**p

一般地，将p表示为二进制形式，即P=2**a+2**b+2**c...+2**n，故A**P=A**(2**a) * A**(2**b) * A**(2**c) ...* A**(2**n)
"""


def raisePower(number, p) -> float:
    power = 1
    while p > 0:
        # p & 1 等价于p%2==1
        if p & 1:
            power *= number  # 用于计算最后的A**1或这说是A**(2**0)
        # 右移
        p >>= 1
        number *= number  # 计算 A**2,由A**2 * A**2 得到A**4,....得到A**N；例如A**7，因7b=111=4+2+1，故算法执行过程为，计算A**2,A**4,A**1
    return power


if __name__ == "__main__":
    print(raisePower(2, 8))
