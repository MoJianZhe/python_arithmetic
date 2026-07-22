# 76.最小覆盖子串
def minWindow(self, s: str, t: str) -> str:
    # 窗口中字符的数量
    window = {}
    # 需要查询的字符串列表，key 字符，value = 数量
    need = {}
    # 是否到达条件
    valid = 0
    # 窗口区间, [left,right)
    left, right = 0
    index = 0
    length = float("inf")
    for i in t:
        need[i] = need.get(i, 0) + 1
    while right < len(s):
        a = s[right]
        window[a] = window.get(a, 0) + 1
        if a in need:
            if window[a] == need[a]:
                valid += 1
        right += 1
        # 已经满足条件，开始收缩窗口
        while valid == len(need):
            if (right - left) < length:
                length = right - left
                index = left
            # 移除 left
            b = s[left]
            left += 1
            if b in need:
                if window[b] == need[b]:
                    valid -= 1
                window[b] = window[b] - 1
    if length == float("inf"):
        return ""
    else:
        return s[index : index + length]



# solubion by labula
def minWindow(self, s: str, t: str) -> str:
    need, window = {}, {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    left = 0
    right = 0
    valid = 0
    # 记录最小覆盖子串的起始索引及长度
    start = 0
    length = float('inf')
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 扩大窗口
        right += 1
        # 进行窗口内数据的一系列更新
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # 在这里更新最小覆盖子串
            if right - left < length:
                start = left
                length = right - left
            # d 是将移出窗口的字符
            d = s[left]
            # 缩小窗口
            left += 1
            # 进行窗口内数据的一系列更新
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    # 返回最小覆盖子串
    return "" if length == float('inf') else s[start: start + length]