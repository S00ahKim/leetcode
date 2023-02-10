"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems connected 
and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1) 모두 양수이므로 하나라도 더 하면 이득이라서 처음부터 건너건너 vs 두번째부터 건너건너 두개만 보면 됨
        #    ㄴ 실패 케이스: [2,1,1,2]
        # if len(nums) == 1: return nums[0]
        # from_first = sum(nums[0::2])
        # from_second = sum(nums[1::2])
        # return from_first if from_first > from_second else from_second

        # 2) 순서대로 n번째 집을 턴 만큼의 max값을 찾아본다
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return nums[0] if nums[0] > nums[1] else nums[1]

        max_arr = [nums[0], nums[0] if nums[0] > nums[1] else nums[1]]
        idx = 2
        prev_1 = max_arr[idx-1] # 하나 전
        prev_2 = max_arr[idx-2] # 둘 전
        for num in nums[2:]:
            max_arr.append(prev_2 + num if prev_2 + num > prev_1 else prev_1)
            idx += 1
            prev_1 = max_arr[idx-1]
            prev_2 = max_arr[idx-2]
        return max_arr[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1,2,3,1])) #4
    print(solution.rob([2,7,9,3,1])) #12
    print(solution.rob([2,1,1,2])) #4
    print(solution.rob([2,3,7,2,5,10])) #19
