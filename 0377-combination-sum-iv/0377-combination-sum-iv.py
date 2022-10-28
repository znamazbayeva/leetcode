class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] + [float(-inf)]*target
        # 1 2 3 4
        # 1      
        # 1 1 -> 2
        # 1 1 (2)[1] 1 (0) -> 3(1)
        # 1 1 1 (3)[1] 1 (0) -> 4(1)
        # 1(0) 2(1) -> 3(1) + 1 = 2
        # 1(0) 2(1) 1(0) -> 4(1) + 1 = 4(2)
        # 1 3 -> 4
        # 2
        # 2 1 -> 3
        # 2 2 -> 4
        # 2 3 -> 5
        # 3 
        # 
        # nums.sort()
        # for i in range(1, target+1):
        #     dp[i] = max([dp[i-c]+1 if i-c == 0 else float(-inf) for c in nums])
        #     print(dp)
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]
