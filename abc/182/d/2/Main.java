import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N+1];
        long[] sum = new long[N+1];
        long[] piz = new long[N+1];

        for (int i = 1; i <= N; i++){
            Az[i] = sc.nextInt();
        }

        sum[1] = Az[1];
        piz[1] = Az[1];
        long tmpMax = Math.max(0,Az[1]);
        for (int i = 2; i <= N; i++){
            sum[i] = Az[i] + sum[i - 1];
            if (sum[i] > tmpMax) {
                tmpMax = sum[i];
            }
            piz[i] = tmpMax;
        }

        long r = 0;
        long x = 0;
        for (int i = 1; i <= N; i++){
            r = Math.max(r, x + piz[i]);
            x = x + sum[i];
        }
        System.out.println(r);
    }
}
