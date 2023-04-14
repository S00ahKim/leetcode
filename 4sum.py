"""
Given an array nums of n integers, 
return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

풀면서 메모
파이썬에서 집합 안에 집합을 넣으려면 set()에 frozenset()을 추가하면 된다.
집합의 요소가 해시 가능 해야 하기 때문인데, 
Python의 모든 불변 내장 객체는 해시 가능하고, frozenset이 불변이기 때문.
마찬가지로 tuple은 불변이므로 set에 추가할 수 있다.
"""

from typing import List

class Solution:
    # 시간초과 ㅠㅠ
    def _fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 정답을 넣을 집합
        answer = []
        test = set()

        # 일단 정렬
        nums.sort()
        print(nums)

        # 답을 [nums[i], nums[j], nums[k], nums[m]] 라고 둘 때
        # 만들 수 있는 모든 조합을 구해보고, 조건에 맞으면 추가한다.
        # 이때 중복 필터링은 집합을 사용했다.
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    for m in range(k+1, len(nums)):
                        # 불가능한 경우는 필터링
                        if i == 0:
                            if target > 0 and nums[i] > 0 and nums[m] > 0:
                                if nums[i] + nums[j] + nums[k] + nums[m] < target:
                                    return []
                            elif target > 0 and nums[-1] < 0:
                                return []
                            # 음수는 양수로 역전될 수 있어서 이렇게 거르면 안됨
                            # elif target < 0 and nums[i] < 0 and nums[m] < 0:
                            #     if nums[i] + nums[j] + nums[k] + nums[m] > target:
                            #         return []
                            elif target < 0 and nums[0] > 0:
                                return []
                        if nums[i] + nums[j] + nums[k] + nums[m] == target:
                            test_before = len(test)
                            test.add(frozenset([nums[i], nums[j], nums[k], nums[m]]))
                            test_after = len(test)
                            if (test_before != test_after): 
                                answer.append([nums[i], nums[j], nums[k], nums[m]])
        return answer
    
    # 답을 찾아봄: https://smlee729.wordpress.com/2018/03/14/algorithm-%EB%AC%B8%EC%A0%9C-4sum/
    # - 우리가 할 수 있는 최선은 O(n^4) 를 O(n^3)로 떨어뜨리는 것
    # - 왜 둘은 고정하고 뒤의 둘은 앞뒤로 움직일까?
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)

        # 문제를 푸는 핵심입니다. 숫자를 오름차순으로 정렬합니다.
        nums.sort()

        # 중복된 tuple들을 없애기 위해서 일단 set으로 결과값들을 담아둡니다.
        result = set()
        for i in range(length-3):
            for j in range(i+1, length-2):
                # 앞의 두 포인터를 고정하고 나서 새로운 target값을 계산합니다.
                new_target = target - nums[i] - nums[j]

                # 나머지 두 포인터는 남은 구간에서 처음과 끝으로 설정하고, 2sum 문제를 풀어줍니다.
                k = j+1
                l = length-1
                while l > k:
                    if new_target == nums[k] + nums[l]:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif new_target > nums[k] + nums[l]:
                        k += 1
                    else:
                        l -= 1
        
        return [list(x) for x in result]

if __name__ == "__main__":
    solution = Solution()
    # print(solution.fourSum([1,0,-1,0,-2,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    # print(solution.fourSum([2,2,2,2,2], 8)) # [[2,2,2,2]]
    print(solution.fourSum([-2,-3,0,-4,5,-5,-1], -12)) # [[-5,-4,-3,0],[-5,-4,-2,-1]]