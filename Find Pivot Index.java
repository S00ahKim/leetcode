/**
 * https://leetcode.com/problems/find-pivot-index/
 * 앞에서부터 피봇일 경우 오른쪽 합, 뒤에서부터 피봇일 경우 왼쪽 합을 구해서 배열에 넣고
 * 피봇 인덱스가 같은데 양쪽 합이 같은 경우를 찾아서 리턴 & 없으면 -1 리턴
 */

class Solution {
  public int pivotIndex(int[] nums) {
      int[] front = new int[nums.length];
      int[] back = new int[nums.length];
      
      int fnum = 0;
      for (int i = 0; i<nums.length ; i++) {
          if (i==0) {
              front[0] = 0;
          } else {
              fnum += nums[i-1];
              front[i] = fnum;
          }
      }
      
      int bnum = 0;
      for (int i = nums.length-1 ; i>-1 ; i--) {
          if (i==nums.length-1) {
              back[0] = 0;
          } else {
              bnum += nums[i+1];
              back[i] = bnum;
          }
      }
      
      for (int i = 0; i<nums.length ; i++) {
          if (front[i] == back[i]) {
              return i;
          }
      }
      return -1;
  }
}