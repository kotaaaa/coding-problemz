import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = Math.abs(sc.nextInt());
        long ans = 0;
        for (int i = 2+K; i <= 2*N; i++){
            ans += f(i, N) * f(i - K, N);
        }
        System.out.println(ans);
    }
    public static long f (long a, long b){
        return Math.min(a-1, -1*a + 2*b+1);
    }
}