# 素性测试
"""
判断数p是否是素数：
    小费马定理表明：
        如果p是素数，则1<=n<p,且pow(n,p-1) % p ==1

    注意：
        1.即使p不是素数，也有可能成立 1<=n<=p,且pow(n,p-1) % p ==1，此时称n为“费马骗子”，相反不成立成为“费马证人”
        2.可以证明对于自然数p，1~p至少有一半n是“费马证人”
        3.在1~P中取k次数（n），用于素性测试，则pow(1/2,k)的概率表明p不是素数。如k=10，p不是素数的概率为0.0009765625
"""
import random
from quickpower import raisePower


def prime_test(number, max_test):
    # 0~max_test-1
    for i in range(max_test):
        # 1~number-1
        if int(raisePower(random.choice(range(1, number)), number - 1)) != 1:
            # if random.choice(range(1, number)) ** (number - 1) % number != 1:
            return False
    return True


if __name__ == "__main__":
    print(prime_test(798798, 10))
