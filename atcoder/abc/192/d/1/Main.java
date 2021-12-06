import java.util.*;

public class Main {
    public static void main(String[] args) {

//        System.out.println("100000000000000000000000000000000000000000000000000000000000".length());
//        System.exit(0);

        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        long m = sc.nextLong();
//        m = sc.nextLong();

        int d = 0;
        for (int i = 0; i < s.length(); i++) {
            d = Math.max(d, (s.charAt(i) - 48));
        }

        d++;

        long ans = 0;
        while (true) {

            long each = 0;
            for (int i = 0; i < s.length(); i++) {
                System.out.println("((int) s.charAt(i) - 48) "+((int) s.charAt(i) - 48) );
                each += ((int) s.charAt(i) - 48) * Math.pow(d, s.length()-1 - i);
                System.out.println("a "+((int) s.charAt(i) - 48)+" Math.pow(d, s.length()-1 - i) "+Math.pow(d, s.length()-1 - i)+" d "+d+" i "+i);
                System.out.println("each "+each);
            }
            if (each > m) {
                break;
            }
            ans++;
            d++;
//            if (ans == 3){
//                break;
//            }
        }

        System.out.println(ans);

    }
}