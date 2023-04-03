"""
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

= 다 다른 요소를 더해서 0이 되는 경우 찾기
"""
from typing import List

class Solution:
    def _threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        # (1) 0이 세 개인 경우 & (2) 중복인 값이 있는 경우 & (3) 모두 다른 값인 경우
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
        # (1)        
        if 0 in dict.keys() and dict[0] >= 3:
            answer.append([0,0,0])
            dict[0] = 1
        keys = list(dict.keys())
        for i in range(len(keys)):
            key = keys[i]
            # (2)
            if key != 0 and dict[key] >= 2 and -(2*key) in dict.keys():
                answer.append([key, key, -(2*key)])
            # (3) 두 값이 골라지면 남은 하나의 값은 정해진다.
            for j in range(i+1, len(keys)):
                x = keys[i]
                y = keys[j]
                if -(x+y) in keys[j+1:]:
                    answer.append([x, y, -(x + y)])
        return answer

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 정답을 넣을 배열
        answer = []

        # 일단 정렬
        nums.sort()

        # 불가능한 경우 리턴
        if nums[0] > 0 :
            return []
        if nums[0] == 0 and nums[2] != 0 :
            return []
        if nums[-1] < 0 :
            return []
        
        for i in range(0, len(nums)):
            # 중복값에 대해서는 이미 확인했으므로 넘어감
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # 양수부터는 더이상 합산 0을 만들 수 없으므로 넘어감
            if nums[i] > 0:
                break

            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    low = nums[j]
                    high = nums[k]
                    while nums[j] == low and j < k:
                        j += 1
                    while nums[k] == high and j < k:
                        k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return answer

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
    print(solution.threeSum([0,0,0])) #[[0,0,0]]
    print(solution.threeSum([0,1,1])) #[]
    print(solution.threeSum([-1,0,1,0])) #[[-1,0,1]]
    print(solution.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])) #[[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]