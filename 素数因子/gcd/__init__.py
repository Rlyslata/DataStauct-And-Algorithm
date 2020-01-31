# 计算最大公约数
"""
gcd(a,b) = = gca(b,a mod b)
a = b*m+n
a= b,b=n
"""


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
        print([a, b])
    return a


if __name__ == "__main__":
    print(gcd(9994, 9998))
