/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 * 
 * 시도 1: 앞에서 최소를 찾고 뒤에서 최대를 찾아서 최대차이를 얻음 => [3,2,6,5,0,3] 이런 경우를 잡아내지 못함.
 * 시도 2: 답은 맞게 나오는 것 같은데, 이중 for문 때문에 타임 리밋이 걸림.
 * 시도 3: 이중포문 회피 - 최소, 최대를 잡고 돌리기 
 */

// 시도 1
class Solution {
  public int maxProfit(int[] prices) {
      if (prices.length == 1) {
          return 0;
      }
      // 맨 뒤 요소를 제외하고 앞 배열에서 최소값을 찾는다.
      int[] findMinimum = Arrays.copyOfRange(prices, 0, prices.length-1);
      int idx = 0;
      int val = findMinimum[0];
      for (int i=1; i<findMinimum.length ; i++) {
          if (val > findMinimum[i]) {
              val = findMinimum[i];
              idx = i;
          }
      }
      // 최소값을 찾고 최소값의 idx 뒤부터 최대값을 찾는다.
      int[] findMaximum = Arrays.copyOfRange(prices, idx, prices.length);
      int idx_2 = idx;
      int val_2 = prices[idx_2];
      for (int i=1; i<findMaximum.length ; i++) {
          if (val_2 < findMaximum[i]) {
              val_2 = findMaximum[i];
              idx_2 = i;
          }
      }
      // 만약 앞에서 찾은 최소값이 뒤의 최대값보다 클 경우 0을 리턴한다. 아닐 경우 최대이익을 리턴한다.
      if (val>val_2) {
          return 0;
      } else {
          return val_2 - val;
      }
  }
}

// 시도 2
class Solution {
  public int maxProfit(int[] prices) {
      // 앞-뒤
      int[] diff = new int[prices.length];
      for (int i=0; i<prices.length; i++) {
          int val = prices[i];
          int diffNum = -1;
          for (int j=i+1; j<prices.length; j++) { // 처음에 j=1로 고정했었다 ;;
              int val_2 = prices[j];
              if (diffNum < (val_2 - val)) {
                  diffNum = val_2 - val;
              }
          }
          diff[i] = diffNum;
      }
      // 모두 음수면 0, 양수면 최대값을 리턴한다
      int maximum = diff[0];
      for (int i=1; i<diff.length ; i++) {
        if (maximum < diff[i]) {
            maximum = diff[i];
        }
      }
      if (maximum < 0) {
          return 0;
      } else {
          return maximum;
      }
  }
}

// 시도 3
class Solution {
  public int maxProfit(int[] prices) {
      int minimum = prices[0]; // minimum은 변경될 수 있다.
      int maxProfit = 0; // minimum이 변경되더라도 변경된 minimum의 maxProfit을 이전과 비교하기 위함
      
      for (int i=0; i<prices.length; i++){
          int price = prices[i];
          if (price < minimum) {
              minimum = price;
          }
          int currentProfit = price-minimum;
          if (maxProfit < currentProfit) {
              maxProfit = currentProfit;
          }
      }
      return maxProfit;
  }
}