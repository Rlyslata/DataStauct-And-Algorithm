from importlib import reload

m = 1
m += 1

print(id(m))


def test():
    global m
    m = 3
    c = 4
    print(id(m))
    print("dir:")
    print(dir(test))
    print("locals:")
    print(locals())
    print("globals:")
    print(globals()['m'])


test()

import Queue

reload(Queue)
