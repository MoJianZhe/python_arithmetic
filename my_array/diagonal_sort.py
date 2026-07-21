# 1329. 将矩阵按对角线排序
from typing import List
def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    dic = {}
    col_size = len(mat[0])
    row_size = len(mat)
    for i in range(row_size):
        for j in range(col_size):
            key = j-i
            if key not in dic:
                dic[key] = []
            dic[key].append(mat[i][j])
    for key in dic.keys():
        arr = dic[key]
        dic[key]=sorted(arr,reverse=True)
    for i in range(row_size):
        for j in range(col_size):
            # pop 是取最后一个元素，所以上面要反序
            a = dic[j-i].pop()
            mat[i][j]= a
    return mat

# solution by labula
def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])

    # 存储所有对角线的元素列表
    diagonals = {}

    for i in range(m):
        for j in range(n):
            # 横纵坐标之差可以作为一条对角线的 ID
            diagonalID = i - j
            if diagonalID not in diagonals:
                diagonals[diagonalID] = []
            diagonals[diagonalID].append(mat[i][j])

    # 从数组末尾删除元素效率较高，所以我们把 ArrayList 倒序排序
    for diagonal in diagonals.values():
        diagonal.sort(reverse=True)

    # 把排序结果回填二维矩阵
    for i in range(m):
        for j in range(n):
            diagonal = diagonals[i - j]
            mat[i][j] = diagonal.pop()

    return mat