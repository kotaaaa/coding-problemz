import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

//        boolean hard = true;
//        System.out.println("s "+s);
//        System.out.println("s.length "+s.length());
//        System.out.println(s.charAt(9));
        for (int i = 1; i <= s.length(); i++) {
            if (i % 2 == 1) { // 奇数
                if (Character.isUpperCase(s.charAt(i-1))) {
//                    hard = false;
                    System.out.println("No");
                    System.exit(0);
                }
            } else {
                if (!Character.isUpperCase(s.charAt(i-1))) {
//                    hard = false;
                    System.out.println("No");
                    System.exit(0);
                }
            }
        }
        System.out.println("Yes");
    }
}