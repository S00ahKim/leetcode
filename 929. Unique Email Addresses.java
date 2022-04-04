import java.util.HashSet;

/**
 * https://leetcode.com/problems/unique-email-addresses/
 * 
 * 처음에 "%s@%s".format() 처럼 문법을 틀리게 써서 의도대로 되지 않음.
 * 테스트로 돌려보는 거 보고 + 뒤에 . 이 있으면 포함시켜야 한다고 뇌피셜로 생각했음.
 * => 귀납적으로 생각하지 말자. 처음에 잘 이해했는데 너무 돌아갔다.
 * 
 * split을 할 때 + 처럼 메타 문자를 쓸 때에는 \\를 붙여 주어야 함.
 * 
 */

class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> set = new HashSet<String>();
        for (String email : emails) {
            String[] emailInfo = email.split("@");
            String id = emailInfo[0].split("\\+")[0].replace(".", "");
            set.add(String.format("%s@%s", id, emailInfo[1]));
        }
        return set.size();
    }
}