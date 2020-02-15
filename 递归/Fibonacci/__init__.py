# 斐波那契数
"""
Fibonacci(0) = 0,Fibonacci(1) = 1
Fibonacci(n) = Fibonacci(n-1)+Fibonacci(n-2)
"""


# 普通递归
def Fibonacci(n):
    if 0 == n:
        return 0
    elif 1 == n:
        return 1
    elif 0 > n:
        raise ValueError("n不能为负")

    return Fibonacci(n - 1) + Fibonacci(n - 2)


# 存储中间值，提高效率,从后往前推
Max = 1
Fibonacci_optimized_arr = [0, 1] + [0] * 999


def Fibonacci_optimized_1(n):
    global Max
    if n > Max:
        Fibonacci_optimized_arr[n] = Fibonacci_optimized_1(n - 1) + Fibonacci_optimized_1(n - 2)
        Max = n
    # n<=max可以在中间值数组中找到
    return Fibonacci_optimized_arr[n]


# 从前往后推
def Fibonacci_optimized_2(n):
    global Max
    if n > Max:
        for i in range(Max + 1, n + 1):
            Fibonacci_optimized_arr[i] = Fibonacci_optimized_2(i - 1) + Fibonacci_optimized_2(i - 2)
        Max = n
    return Fibonacci_optimized_arr[n]


if __name__ == "__main__":
    print(Fibonacci_optimized_1(777))
    print(Fibonacci_optimized_2(777))
    print(Fibonacci(30))
