from typing import List


# 需要额外的空间
def quick_sort(arr: List):
    if len(arr) < 1:
        return arr
    mid_value = arr[len(arr) // 2]
    left = [i for i in arr if i < mid_value]
    middle = [x for x in arr if x == mid_value]  # 等于基准值
    right = [i for i in arr if i > mid_value]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    b = quick_sort([1, 33, 2, 3, 4, 10, 9, 24, 2])
    print(b)
