/**
 * https://leetcode.com/problems/is-subsequence/
 * 
 * sIdx와 tIdx라는 변수로 두 문자열에 대한 인덱스를 보면서 subsequece인지 확인
 * 
 * 예외 케이스에 대한 처리를 추가했다.
 * A: s의 길이가 아예 없으면 무조건 true 반환
 * B: t 순회가 다 끝나기 전에 이미 subsequence인 것이 밝혀진 경우 순회 멈춤
 */

class Solution {
  public boolean isSubsequence(String s, String t) {
      if (s.length() == 0) { // A
          return true;
      }
      
      int sIdx = 0;
      for (int tIdx=0; tIdx < t.length() ; tIdx++) {
          if (s.charAt(sIdx) == t.charAt(tIdx)) {
              sIdx++;
          }
          if (sIdx == s.length()) { // B
              break;
          }
      }
      if (sIdx == s.length()) {
          return true;
      } else {
          return false;
      }
  }
}