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