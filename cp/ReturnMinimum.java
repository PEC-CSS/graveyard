package cp;

public class ReturnMinimum {
    public static void main(String[] args) {
        String s = "01011101";
        int sum = 0;
        sum += s.charAt(0) - '0';
        StringBuilder ans = new StringBuilder();
        for(int i = 1; i < s.length(); i++) {
            int digit = s.charAt(i) - '0';
            if(digit == 0) {
                ans.append("+");
            } else {
                if(sum == 0) {
                    ans.append("+");
                    sum += digit;
                } else {
                    ans.append("-");
                    sum -= digit;
                }
            }
        }
        System.out.println(ans.toString());
    }
}
