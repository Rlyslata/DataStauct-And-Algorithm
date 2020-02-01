import time

from pymysql import Date


class TriangleArray:
    def __init__(self):
        self.data = []
        self.size = 0

    def get(self, row, column):
        index = int((row ** 2 + row) / 2 + column)
        if index <= self.size - 1:
            return self.data[index]
        else:
            return None

    def append_(self, value):
        self.data.append(value)
        self.size += 1

    def set(self, row, column, value):
        index = int((row ** 2 + row) / 2 + column)
        if index <= self.size - 1:
            self.data[index] = value
            return True
        else:
            return False


if __name__ == "__main__":
    tri = TriangleArray()
    tri.append_(1)
    tri.append_("rlyslata")
    tri.append_("CSDN")
    tri.append_("新肺炎冠状病毒")
    tri.append_(str(time.localtime()))

    print(tri.get(0, 0))
    print(tri.get(1, 0))
    print(tri.get(1, 1))
    print(tri.get(2, 0))
    print(tri.get(2, 1))
