# 5. 最长回文子串
def longestPalindrome(self, s: str) -> str:
    max_str = ""
    for i in range(len(s)):
        re1 = self.max_long_palindrome(s, i, i)
        re2 = self.max_long_palindrome(s, i, i + 1)
        max_str = re1 if len(re1) > len(max_str) else max_str
        max_str = re2 if len(re2) > len(max_str) else max_str
    return max_str


# 寻找在s中，以 s[l],s[r]为中心,向两边扩散的最大的回文串
def max_long_palindrome(self, s, l, r) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    # 左闭右开
    return s[l + 1 : r]


# solution by labula
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.palindrome(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    # 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
    def palindrome(self, s: str, l: int, r: int) -> str:
        # 防止索引越界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 向两边展开
            l -= 1
            r += 1
        # 此时 s[l+1..r-1] 就是最长回文串
        return s[l + 1 : r]
