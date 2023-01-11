"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # 이전 단계에서 1계단 또는 2계단 오르는 방법 = 지금 단계에 오르는 방법
        need_one_step = 2
        need_two_step = 1
        this_turn = 0
        if n < 3:
          return n
        for i in range(3, n+1):
          this_turn = need_one_step + need_two_step
          need_two_step = need_one_step
          need_one_step = this_turn
        return this_turn


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2)) #2
    print(solution.climbStairs(3)) #3
    print(solution.climbStairs(4)) #5
    print(solution.climbStairs(5)) #9