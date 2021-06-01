import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        double[][][] dp = new double[101][101][101];
        double ans = 0;
        for (int a = 99; a >= 0; a--){
            for (int b = 99; b >= 0; b--){
                for (int c = 99; c >= 0; c--){
                    if (a+b+c == 0) continue;
                    double now = 0;
                    now += (dp[a+1][b][c] + 1) * a;
                    now += (dp[a][b+1][c] + 1) * b;
                    now += (dp[a][b][c+1] + 1) * c;
                    dp[a][b][c] = now/(a+b+c);
                }
            }
        }
        System.out.println(dp[A][B][C]);
    }
}