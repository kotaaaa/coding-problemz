import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] Sz = new String[N+1];
        long[][] dp = new long[2][N+1];
        dp[0][0] = 1; // i番目がTRUEだったときに，i番目までの個数
        dp[1][0] = 1; // i番目がFALSEだったときに，i番目までの個数

        String s = sc.nextLine();
        for (int i = 1; i <= N; i++){
            Sz[i] = sc.nextLine();
        }
        for (int i = 1; i <= N; i++){
            if (Sz[i].equals("AND")) {
                dp[0][i] = dp[0][i-1] + dp[1][i-1]*0; // >> OK
                dp[1][i] = 0;
            } else { // "OR"
                dp[0][i] += (long) Math.pow(2,i);
                dp[1][i] = dp[0][i-1]; //
            }
//            System.out.println(i + " dp[true][i], dp[false][i] "+dp[0][i]+" "+dp[1][i]);
        }
        System.out.println(dp[0][N]);
    }
}