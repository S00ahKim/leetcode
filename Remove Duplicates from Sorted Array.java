/**
 * https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
 * 
 * 뒤로 보낸 중복값은 무슨 값이든 상관없다고 했는데 결과 예시 보고 중복값을 남기지 말아야겠거니 하고 또 뇌피셜로 생각했음.
 * 그래서 어떻게 중복값을 수정할까를 너무 오래 고민했던 것 같다.
 * 다시 찬찬히 읽어보니 그런 조건은 없었다.
 * 그리고 순회를 처음부터 돌지 않고 두번째 요소부터 보는 게 훨씬 쉬운 접근이었다.
 */

class Solution {
  public int removeDuplicates(int[] nums) {
      if (nums.length == 1) {
          return 1;
      }
      int lastNum = nums[0];
      int validateIndex = 1;
      
      for (int i = 1; i < nums.length; i++) {
          if (nums[i] == lastNum) {
              nums[i] = 101;
          } else {
              lastNum = nums[i];
              nums[validateIndex] = nums[i];
              validateIndex++;
          }
      }
      return validateIndex;
  }
}