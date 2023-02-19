"""
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, 
compute how much water it can trap after raining.
"""
from typing import List

class Solution:
    # 시간 초과 ㅠㅠ
    def _trap(self, height: List[int]) -> int:
        water = [0 for _ in range(len(height))]
        for idx in range(len(height)):
            if idx == 0 or idx == len(height)-1: #처음이나 끝에는 물이 찰 수 없다
                water[idx] = 0
            else:
                # 지금 칸의 물의 높이 = min(현재 위치 전의 최대 바 높이,현재 위치 뒤의 최대 바 높이)-현재 바 높이
                # 단, 이전-이후 최대값보다 현재 위치가 더 높으면 현재 위치를 기준으로 봄
                prev_tallest = max(height[:idx]) if max(height[:idx]) > height[idx] else height[idx]
                next_tallest = max(height[idx+1:]) if max(height[idx+1:]) > height[idx] else height[idx]
                water[idx] = min(prev_tallest,next_tallest)-height[idx]
        return sum(water)

    def trap(self, height: List[int]) -> int:
        water = [0 for _ in range(len(height))]
        prev_tallest_idx = 0
        prev_tallest = height[prev_tallest_idx]
        next_tallest_idx = height.index(max(height))
        next_tallest = height[next_tallest_idx]
        for idx in range(len(height)):
            if idx == 0 or idx == len(height)-1: #처음이나 끝에는 물이 찰 수 없다
                water[idx] = 0
            else:
                # 지금 칸의 물의 높이 = min(현재 위치 전의 최대 바 높이,현재 위치 뒤의 최대 바 높이)-현재 바 높이
                # 단, 이전-이후 최대값보다 현재 위치가 더 높으면 현재 위치를 기준으로 봄
                if prev_tallest < height[idx]:
                    prev_tallest_idx = idx
                    prev_tallest = height[prev_tallest_idx]
                if idx > next_tallest_idx:
                    next_tallest_idx = idx + height[idx:].index(max(height[idx:]))
                    next_tallest = height[next_tallest_idx]
                water[idx] = min(prev_tallest,next_tallest)-height[idx]
        return sum(water)

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
    print(solution.trap([4,2,0,3,2,5])) #9