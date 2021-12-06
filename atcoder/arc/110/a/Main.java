import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long L = 2;

        for (int i = 3; i <= N; i++){
            L = L / gcd(L, i) * i;
        }
        System.out.println(L + 1);
    }

    public static long gcd(long a, long b){
        if (a == 0) return b;
        if (b == 0) return a;

        long tmp = 0;
        if (a > b){
            tmp = a;
            a = b;
            b = tmp;
        }
        return gcd(a, b % a);
    }
}