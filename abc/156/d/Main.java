import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        long mod = 1000000007;

        long ans = 0;
        ans = ((long) Math.pow(2,N) - 1 - ncr(N,a) - ncr(N,b)) % mod;
        System.out.println(ans);

    }
    public static long ncr (int n, int r){
        return (long) factrial(n)/(factrial(n-r)*factrial(r));
    }

    public static int factrial (int n){
        if (n <= 1) return 1;
        return n * factrial(n - 1);
    }
}

