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
/**
 * 기본적으로 서브 어레이가 "연속적"이어야 하기 때문에
 * 다음 순서에서 추가될 때 k보다 커지면 나중을 기약할 것도 없이 앞에서부터 빼야 한다.
 * 그래서 i가 앞으로 전진하는 인덱스고, j는 빠지는 인덱스를 둔다.
 * 그러면 i가 앞으로 나갈 때마다 생성 가능한 서브어레이 숫자는 1, 3, 6, 10, ...개가 되는데
 * 유일해야 하므로 이전에 나온 걸 빼면 1, 2, 3, 4, ...씩 추가된다. 이는 i-j+1에 해당한다.
 */

class Solution {
  public int numSubarrayProductLessThanK(int[] nums, int k) {
      int count = 0;
      int j = 0;
      int i = 0;
      int product = 1;
 
      while (i < nums.length && j < nums.length) {
          if (product * nums[i] < k) {
              product = product * nums[i];
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