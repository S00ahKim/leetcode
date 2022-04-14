/*
https://leetcode.com/problems/valid-sudoku/

(1) 행 확인 > 열 확인 > 서브박스 확인 을 매번 루프로 돌리고 중복체크를 이상하게 해서 시간 리밋이 걸렸다.
(2) 한 번만 모든 요소를 보면서 필요한 거 확인 + 이전에 검증된 부분은 패스하고 그 다음만 보기

cf. "String", 'c'
cf2. Set 자료구조는 char같은 primitive로는 선언할 수 없음
*/

class Solution {
  public boolean isValidSudoku(char[][] board) {
      // 지금 순서의 수가 그 행에서, 열에서, 박스에서 유일한지를 검사
      boolean isValid = true;
      loop:
      for (int i = 0; i < 9 ; i++){
          for (int j = 0 ; j < 9 ; j++) {
              char thisTurn = board[i][j];
              if (thisTurn == '.') {
                  continue;
              }
              
              // 행 검사
              Set<Character> row = new HashSet<Character>();
              int rowNum = 0;
              for (int z = j ; z < 9 ; z++) {
                  if (board[i][z] != '.') {
                      row.add(board[i][z]);
                      rowNum++;
                  }
              }
              if (rowNum != row.size()) {
                  isValid = false;
                  break loop;
              }
              
              // 열 검사
              Set<Character> col = new HashSet<Character>();
              int colNum = 0;
              for (int z = i ; z < 9 ; z++) {
                  if (board[z][j] != '.') {
                      col.add(board[z][j]);
                      colNum++;
                  }
              }
              if (colNum != col.size()) {
                  isValid = false;
                  break loop;
              }
              
              // 박스 검사
              Set<Character> box = new HashSet<Character>();
              int boxNum = 0;
              for (int startRowIdx = (i/3)*3; startRowIdx < ((i/3)*3)+3 ; startRowIdx++) {
                  for (int startColIdx = (j/3)*3; startColIdx < ((j/3)*3)+3 ; startColIdx++) {
                      if (board[startRowIdx][startColIdx] != '.') {
                          box.add(board[startRowIdx][startColIdx]);
                          boxNum++;
                      }
                  }
              }
              if (boxNum != box.size()) {
                  isValid = false;
                  break loop;
              }
          }
      }
      return isValid;
  }
}