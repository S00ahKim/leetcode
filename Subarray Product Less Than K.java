/**
 * https://leetcode.com/problems/subarray-product-less-than-k/
 * 처음 풀었을 땐 for loop을 도는 게 너무 많아서 타임아웃이 난 것 같다.
 */

class Solution {
  public int numSubarrayProductLessThanK(int[] nums, int k) {
      int answer = 0;
      if (k < 2) return 0;
      // 조건: 수가 주어진 것처럼 연속적일 것 + 곱이 k보다 작을 것
      for (int windowSize = 1 ; windowSize < nums.length+1 ; windowSize++ ) {
          for (int idx=0 ; idx < nums.length ; idx++) {
              if (idx+windowSize > nums.length) break;
              int[] sub = Arrays.copyOfRange(nums, idx, idx+windowSize);
              if (checkLessThanK(sub, k)) answer++;
              //System.out.println(Arrays.toString(sub) + " " + checkLessThanK(sub, k));
          }
      }
      return answer;
  }
  
  public boolean checkLessThanK(int[] sub, int k) {
      int i = 1;
      boolean answer = true;
      for (int s: sub) {
          i = i * s;
          if (i >= k) {
              answer = false;
              break;
          }
      }
      return answer;
  }
}

// ===========================

class Solution {
  public int numSubarrayProductLessThanK(int[] nums, int k) {
      int count = 0;
      int j = 0;
      int i = 0;
      int product = 1;
 
      while (i < nums.length && j < nums.length) {
          if (product * nums[i] < k) {
              product = product * nums[i];
              System.out.println(i - j + 1);
              count   = count + (i - j + 1);
              i++;
          } else {
              if(nums[j] > 0) product = product / nums[j];
              j++;
          }
      }
  
      return count;
  }
}