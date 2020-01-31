# 寻找素数因子
"""
寻找一个数的素因子的最显而易见的办法是：尝试将这个数用比其小大于等于2的整数试除，将能整除的数（因子）保存起来，
再尝试将这个数除以保存的因子的得到的数，尝试其他的因子

"""
from math import sqrt


def splitPrime(number) -> list:
    # 素数因子
    factor = []
    i = 3
    # 最大可能因子

    # 提取出偶数
    while number > 1 and number % 2 == 0:
        factor.append(2)
        number //= 2

    # 寻找奇因子
    max_factor = int(sqrt(number))
    while i <= max_factor:
        while number % i == 0:
            factor.append(i)
            number //= i
        max_factor = int(sqrt(number))
        i += 2
    factor.append(number)
    return factor
    pass


if __name__ == "__main__":
    ret = splitPrime(999979799744544)
    print(ret)
    print("去重：")
    print(set(ret))
    ac = 1
    for i in range(0, len(ret)):
        ac *= ret[i]
    print(ac)
