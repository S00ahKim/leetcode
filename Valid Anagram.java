/**
 * https://leetcode.com/problems/valid-anagram/
 * 
 * 처음에는 굳이 자료구조를 두개 만들고 딥카피를 하고 개수를 비교하고 이랬는데
 * 생각해보니 굳이 저걸 노가다(...)하면서 타이핑하지 않아도 배열 선언을 하면 되고
 * String으로 변환하는 과정도 불필요하게 느껴졌다.
 * 그리고 다른 사람들 풀이도 살펴보다가 수를 비교하는 게 아니라 더하고 빼면 배열을 하나만 쓰면 된다는 걸 깨달음
 * 여러모로 낭비를 최소화하는 생각을 해야겠다 생각함.
 */

class Solution {
  public boolean isAnagram(String s, String t) {
      boolean answer = true;
      
      HashMap<String,Integer> dictionaryForS = new HashMap<String,Integer>(){{
          put("a",0);
          put("b",0);
          put("c",0);
          put("d",0);
          put("e",0);
          put("f",0);
          put("g",0);
          put("h",0);
          put("i",0);
          put("j",0);
          put("k",0);
          put("l",0);
          put("m",0);
          put("n",0);
          put("o",0);
          put("p",0);
          put("q",0);
          put("r",0);
          put("s",0);
          put("t",0);
          put("u",0);
          put("v",0);
          put("w",0);
          put("x",0);
          put("y",0);
          put("z",0);
      }};
      HashMap<String, Integer> dictionaryForT = new HashMap<String, Integer>();
      dictionaryForT.putAll(dictionaryForS);
      
      for (int i = 0; i < s.length() ; i++) {
          dictionaryForS.put(Character.toString(s.charAt(i)), dictionaryForS.get(Character.toString(s.charAt(i))) + 1);
      }
      
      for (int i = 0; i < t.length() ; i++) {
          dictionaryForT.put(Character.toString(t.charAt(i)), dictionaryForT.get(Character.toString(t.charAt(i))) + 1);
      }
      
      for (String k : dictionaryForS.keySet()) {
          if (dictionaryForS.get(k) != dictionaryForT.get(k)) {
              answer = false;
              break;
          }
          System.out.println("[Key]:" + dictionaryForS.get(k) + " [Value]:" + dictionaryForT.get(k));
      }
      return answer;
  }
}

class Solution {
  public boolean isAnagram(String s, String t) {
      int[] stores = new int[26];

      for (char c : s.toCharArray()) {
          stores[c - 'a']++;
      }

      for (char c : t.toCharArray()) {
          stores[c - 'a']--;
      }

      for (int e : stores) {
          if (e != 0) return false;
      }

      return true;
  }
}