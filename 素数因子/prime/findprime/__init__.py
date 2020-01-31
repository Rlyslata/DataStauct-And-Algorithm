# 寻找素数
"""
埃拉托色尼筛法

给定整数n，寻找2~n的最大素数
1.去除2的倍数
2.去除3的倍数(有些也是2的倍数，已被去除，比如6,12)
.
.
.

3.去除sqrt(n)的倍数

时间复杂度为：O(N*log(logN))
算法适用于小数据，如果number有100位，，吧
"""
from math import sqrt


def findPrime(number) -> list:
    # 合数为true
    is_composite = [True]*(number+1)

    for i in range(2, number + 1):
        is_composite[i] = False

    # 去除2的倍数
    for i in range(4, number + 1, 2):
        is_composite[i] = True

    # 去除大于2的素数的倍数
    stop_at = int(sqrt(number))
    next_prime = 3
    while next_prime <= stop_at:
        # 去除next_prime的倍数
        for k in range(next_prime * 2, number+1, next_prime):
            is_composite[k] = True
        next_prime += 2
        while next_prime <= number and is_composite[next_prime]:
            next_prime += 2

    prime_list = []

    for i in range(2, number+1):
        if not is_composite[i]:
            prime_list.append(i)
    print(prime_list)
    return prime_list


if __name__ == "__main__":
    findPrime(9999)
