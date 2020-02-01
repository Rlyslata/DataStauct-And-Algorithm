import gc

"""
稀疏数组应用场景：
    当数组size很大而空间利用率很低时，应使用稀疏数组来存储
    
    下面的实现的稀疏数组0行0列都没用来存储数据，留做存储row_size等其他数据
    
    一个稀疏数组由多个行链表组成，一个行链表由多个节点构成
    
    :author: Rlyslata
    :date: 2020/2/1
"""


# 节点类
class ArrayEntry:
    def __init__(self, columnNumber=0, nextEntry=None, entry=0):
        # 所处的列数
        self.columnNumber = columnNumber
        # 下一个节点
        self.nextEntry = nextEntry
        # 数据域
        self.entry = entry


# 行链表类
class ArrayRow:
    def __init__(self, rowNumber=0, rowSentinel=ArrayEntry(), nextRow=None):
        # 稀疏数组所处的行
        self.rowNumber = rowNumber
        # 下一行
        self.nextRow = nextRow
        # 当前行的哨兵、头指针
        self.rowSentinel = rowSentinel

        self.columnSize = 0


# 稀疏数组类
class SparseArray:
    def __init__(self, sentinel=ArrayRow(), rowSize=0, columnSize=0):
        # sentinel row的头指针
        self.sentinel = sentinel
        # 稀疏数组的行
        self.rowSize = rowSize
        # 稀疏数组的列
        self.columnSize = columnSize

    # 寻找rowNum前一行，返回rowNum前一行
    def findRowBefore(self, rowNum) -> ArrayRow:
        array_row = self.sentinel
        while array_row.nextRow and array_row.nextRow.rowNumber < rowNum:
            array_row = array_row.nextRow
        return array_row

    # 寻找row的columnNum列的前一列
    def findColumnBefore(self, row, columnNum) -> ArrayEntry or str:
        if row is None:
            return "row 不能为空"
        row_sentinel = row.rowSentinel
        while row_sentinel.nextEntry and row_sentinel.nextEntry.columnNumber < columnNum:
            row_sentinel = row_sentinel.nextEntry
        return row_sentinel

    # 获取（rowNum，columnNum）值
    def getEntry(self, rowNum, columnNum) -> int or str:
        row = self.findRowBefore(rowNum)
        if row.nextRow is None or row.nextRow.rowNumber > rowNum:
            return "没找到行" + str(rowNum)
        row_sentinel = self.findColumnBefore(row, columnNum)
        if row_sentinel.nextEntry is None or row_sentinel.nextEntry.columnNumber > columnNum:
            return "没找到列" + str(columnNum)
        return row_sentinel.nextEntry.entry

    # 设置entry，若未找到行，则新建行，未找到列则，新建列
    def setEntry(self, rowNum, columnNum, entry) -> bool:
        # 找到行
        row = self.findRowBefore(rowNum)
        if row.nextRow is None or row.nextRow.rowNumber > rowNum:
            new_row = ArrayRow(row.rowNumber + 1)
            new_row.nextRow = row.nextRow
            row.nextRow = new_row
            row = row.nextRow

        # 找到列
        row_sentinel = self.findColumnBefore(row, columnNum)
        if type(row_sentinel) == str:
            return False
        elif row_sentinel.nextEntry is None or row_sentinel.nextEntry.columnNumber > columnNum:
            new_column = ArrayEntry(columnNumber=row_sentinel.columnNumber + 1, entry=entry)
            new_column.nextEntry = row_sentinel.nextEntry
            row_sentinel.nextEntry = new_column
        else:
            row_sentinel.nextEntry.entry = entry
        return True

    def deleteEntry(self, rowNum, columnNum):
        # 找到行
        row = self.findRowBefore(rowNum)
        if row.nextRow is None or row.nextRow.rowNumber > rowNum:
            return False

        # 找到列
        row_sentinel = self.findColumnBefore(row.nextRow, columnNum)
        if type(row_sentinel) == str:
            return False
        elif row_sentinel.nextEntry is None or row_sentinel.nextEntry.columnNumber > columnNum:
            return False
        else:
            delete = row_sentinel.nextEntry
            after_delete = row_sentinel.nextEntry.nextEntry
            row_sentinel.nextEntry = after_delete
            del delete
            gc.collect()
            return True


if __name__ == "__main__":
    sparse = SparseArray()
    row1 = sparse.sentinel.nextRow = ArrayRow(rowNumber=1)
    row1.rowSentinel.nextEntry = ArrayEntry(columnNumber=1, entry=11)
    print(sparse.findRowBefore(1).nextRow.rowSentinel.nextEntry.entry)
    print(sparse.findColumnBefore(row1, 1).nextEntry.entry)
    print(sparse.setEntry(2, 2, 22))
    print(sparse.getEntry(2, 2))

    print(sparse.deleteEntry(2, 2))
    print(sparse.deleteEntry(2, 3))
    print(sparse.getEntry(2, 2))
