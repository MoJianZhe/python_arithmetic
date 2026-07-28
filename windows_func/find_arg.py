# 438.找到字符串中所有字母异位词


class Solution:

    def findAnagrams(self, s: str, t: str) -> list[int]:
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0
        valid = 0
        # 记录结果
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while right - left >= len(t):
                # 当窗口符合条件时，把起始索引加入 res
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res

    # 自己写的
    def findAnagrams2(self, s: str, t: str) -> list[int]:
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0
        valid = 0
        # 记录结果
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩 ，大于的时候再收缩也可以，和 long_continue_one.py 保持一致。
            while right - left > len(t):
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
            # 当窗口符合条件时，把起始索引加入 res
            if valid == len(need):
                res.append(left)
        return res
