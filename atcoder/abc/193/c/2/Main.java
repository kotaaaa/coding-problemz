import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
//        long cnt = 0;
//        int a = 2;
        long b = 2;
        HashSet<Long> set = new HashSet<Long>();
        for (long a = 2; a <= Math.sqrt(n); a++) {
            b = 2;
            while (Math.pow(a,b) <= n) {
                set.add((long) Math.pow(a,b));
                b++;
//                cnt++;

            }
        }
        System.out.println(n-set.size());
    }
}