"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_cnt_dict = {}
        for n in nums:
            if n in nums_cnt_dict.keys():
                nums_cnt_dict[n] += 1
            else:
                nums_cnt_dict[n] = 1
        top_k = sorted(nums_cnt_dict.values(), reverse=True)[:k]
        return [k for k, v in nums_cnt_dict.items() if v in top_k]

if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2)) #[1,2]