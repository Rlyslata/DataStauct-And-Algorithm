# 计算最小公倍数
"""
先计算 a，b的最大公约数，
a，b的最小公倍数为 lcm(a,b) = a*b/gcd(a,b)
"""
from gcd import gcd


def lcm(a, b):
    Gcd = gcd(a, b)
    return a * b / Gcd


if __name__ == "__main__":
    print(lcm(9994, 9998))
