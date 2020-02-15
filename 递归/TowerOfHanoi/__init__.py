# 汉诺塔
first_peg = [1, 2, 3, 4, 5]
second_peg = []
third_peg = []


def TowerOfHanoi(from_peg, to_peg, other_peg, plate_num):
    # 递归地将from_peg上的n-1个盘子放到other_peg
    # plate_num始终记录的是
    if plate_num > 1:
        TowerOfHanoi(from_peg, other_peg, to_peg, plate_num - 1)
    # 将from_peg上的最后一个盘子移动到to_peg上
    try:
        to_peg.append(from_peg.pop())
    except IndexError:
        print("from_peg = {}    to_peg = {}    other_peg = {}".format(from_peg, to_peg, third_peg))
    # 将n-1个盘子从other_peg上移回到from_peg上
    if plate_num > 1:
        TowerOfHanoi(other_peg, to_peg, from_peg, plate_num - 1)


if __name__ == "__main__":
    TowerOfHanoi(from_peg=first_peg, to_peg=second_peg, other_peg=third_peg, plate_num=5)
    print(first_peg)
    print(second_peg)
    print(third_peg)
