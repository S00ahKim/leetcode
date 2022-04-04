/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

정수 배열 nums와 정수 target이 주어진다.
더해서 taget이 되는 두 수의 인덱스를 반환하라.
같은 수를 두 번 쓸 수는 없지만, 모든 input 케이스에서 단 하나의 해답만 나오게 된다.
정답은 어떤 순서로 리턴해도 상관없다.
*/

class Solution {
  public int[] twoSum(int[] nums, int target) {
      int[] answer = new int[2]; // 배열 크기 할당
      loop: // 이중 loop를 한 번에 종료시킬 수 있는 방법
      for (int i=0; i<nums.length; i++) { // not length()
          for (int j=i+1; j<nums.length; j++) {
              if (nums[i]+nums[j] == target) {
                  answer[0] = i;
                  answer[1] = j;
                  break loop;
              }
          }
      }
      return answer;
  }
}