def f(m_):
    print("id(m) = " + str(id(m_)))
    m = m_ + 1
    print("id(m) = " + str(id(m)))


def f2(a_: list):
    a_[1] = 10


var1 = 100
if __name__ == "__main__":
    m = 0
    print("id(m) = " + str(id(m)))
    print(m)
    f(m)
    print(m)

    a = [1, 2, 3]
    print(a)
    f2(a)
    print(a)


def f3():
    a = 0

    def inner_func():
        nonlocal a
        a = a + 1
        print("a = " + str(a))
        var1 = 10
        print("var1=" + str(var1))
        # global var1
        print("var1=" + str(var1))
    inner_func()


f3()
