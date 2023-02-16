"""
Given n pairs of parentheses, 
write a function to generate 
all combinations of well-formed parentheses.
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: return ["()"]
        prev_answer = set()
        turn = 1
        prev_parenthesis = [["(", ")"]]
        while turn < n:
            prev_answer = set()
            for pp in prev_parenthesis:
                for idx in range(len(pp)+1):
                    pp.insert(idx, "()")
                    prev_answer.add("".join(s for s in pp))
                    del pp[idx]
            prev_parenthesis = list(list(p) for p in list(prev_answer))
            turn += 1
        return list(prev_answer)

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3)) #["((()))","(()())","(())()","()(())","()()()"]