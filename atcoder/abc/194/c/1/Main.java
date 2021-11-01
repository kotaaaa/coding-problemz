import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        long cnt = 0;
        int a = 2;
        int b = 2;
        while(a <= n) {
            b = 2;
            while (Math.pow(a,b) <= n) {
                cnt++;
                b++;
            }
            a++;
        }
        System.out.println("a "+a+" b "+b);

        System.out.println(n-cnt);

    }
}