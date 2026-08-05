# 1011.在D天内送达包裹的能力

from typing import List


class ShipWithinDays:
    # 1 <= days <= weights.length <= 5 * 10^4
    # 1 <= weights[i] <= 500
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 
        left = 1
        # 最大承载就是 weights[i] 的最大值 500 * 长度
        right = 500*len(weights)+1 # 加1是因为左闭右开
        while left < right:
            mid = left + (right - left)//2 
            mid_days = self.find_day_by_result(weights,mid)
            if mid_days == days:
                right = mid
            elif mid_days < days:
                right = mid - 1 # 应该更新未 mid , [left,mid-1) mid-1就会被排除掉了。
            elif mid_days > days:
                left = mid + 1
        return left
        

    def find_day_by_result2(self, weights:List[int],result)->int:
        item = 0
        days = 1
        for i in range(len(weights)):
            if weights[i] > result:
                # 说明小了，返回最大值
                return 50001
            if (item + weights[i])>result:
                days +=1
                #  item 不能直接给weights[i] , 给weights[i] 后，没有判断days 是否需要+1
                item = weights[i]             
            else :
                item = item + weights[i]
        return days

    def find_day_by_result(self, weights:List[int],result)->int:
        item = 0
        days = 1
        for i in range(len(weights)):
            if weights[i] > result:
                # 说明小了，返回最大值
                return 50001
            if (item + weights[i])>result:
                days +=1
                # days + 1后，item 从0开始计数
                item = 0
            item = item + weights[i]
        return days


    # solution by labula       
    def shipWithinDays(self,weights: List[int], days: int) -> int:
        left = 0
        # 注意，right 是开区间，所以额外加一
        right = 1
        for w in weights:
            left = max(left, w)
            right += w
        
        while left < right:
            mid = left + (right - left) // 2
            if f(weights, mid) == days:
                # 搜索左侧边界，则需要收缩右侧边界
                right = mid
            elif f(weights, mid) < days:
                # 需要让 f(x) 的返回值大一些
                right = mid
            elif f(weights, mid) > days:
                # 需要让 f(x) 的返回值小一些
                left = mid + 1
        
        return left


    def find_day_by_result_bylabula(self,weights: List[int], x: int) -> int:
        days = 0
        # 尽可能多的装货
        i = 0
        while i < len(weights):
            cap = x
            while i < len(weights):
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1
            days += 1
        return days
