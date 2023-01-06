"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 두개의 글자만 비교해서 최대 prefix를 찾고 다음 것도 맞는지 계속 확인해 나감
        lcp = ""
        if len(strs) == 1:
            return strs[0]
        else:
            first = strs[0]
            second = strs[1]
            enough = False
            shorter_one = first if len(first) < len(second) else second
            first = first[:len(shorter_one)]
            second = second[:len(shorter_one)]
            while not enough:
              for idx in range(len(shorter_one)):
                  if first[idx] == second[idx]:
                    lcp += first[idx]
                  else:
                    enough = True
              enough = True
            for left in strs[1:]:
              enough = False
              while not enough:
                if left.startswith(lcp):
                  break
                lcp = lcp[:-1]

        return lcp


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))