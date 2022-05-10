/**
 * https://leetcode.com/problems/pascals-triangle-ii/
 * 처음에는 방정식을 찾아볼까 했었는데, rowIndex가 33 이하면
 * 그냥 답을 만들어가는 게 나을 것 같아서 정직하게 구현했다.
 * answer.add() 처럼 list에 add하는 건 리턴값이 boolean으로,
 * answer에 재할당하면 타입에러가 나니까 주의하자...
 */

class Solution {
  public List<Integer> getRow(int rowIndex) {
      List<Integer> answer = new ArrayList<Integer>();
      for (int row=0; row < rowIndex+1 ; row++) {
          if (row < 2) {
              answer.add(1);
          } else {
              List<Integer> tmp = new ArrayList<Integer>();
              tmp.add(1);
              for (int i=0; i < answer.size()-1 ; i++) {
                  tmp.add(answer.get(i) + answer.get(i+1));
              }
              tmp.add(1);
              answer = tmp;
          }
      }
      return answer;
  }
}