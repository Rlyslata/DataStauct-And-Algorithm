# 阶乘
def calculate_factorial(n):
    # 递归出口
    if 0 <= n <= 1:
        return 1
    elif n < 0:
        raise ValueError("n 不能为负数")

    return n * calculate_factorial(n - 1)


if __name__ == "__main__":
    print(calculate_factorial(5))
    print(calculate_factorial(-5))
