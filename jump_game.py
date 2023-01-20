"""
You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 뒤에서부터 여기까지 왔을 때 다음으로 갈 수 있거나 끝까지 갈 수 있는가를 본다.
        if len(nums) == 1 : return True
        nums.reverse()
        next = 1
        end = 1
        can = False
        for idx in range(len(nums)):
            if idx == 0 : continue
            if nums[idx] >= next:
                next = 1
                can = True
                continue # 둘중에 하나만 만족해도 됨
            else:
                next += 1
                can = False
            if nums[idx] >= end:
                can = True
            else:
                end += 1
                can = False
        return can
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2,3,1,1,4])) # true
    print(solution.canJump([3,2,1,0,4])) # false
    print(solution.canJump([1,2,0,1])) # true
