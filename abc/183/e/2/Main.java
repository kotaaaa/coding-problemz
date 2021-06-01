import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();

        char[][] Tz = new char[H][W];

        String S = sc.nextLine();
        for (int i = 0; i < H; i++) {
            S = sc.nextLine();
            for (int j = 0; j < W; j++) {
                Tz[i][j] = S.charAt(j);
            }
        }

        int[][] dp = new int[H][W];
        int[][] X = new int[H][W];
        int[][] Y = new int[H][W];
        int[][] Z = new int[H][W];
        int mod = 1000000007;

        dp[0][0] = 1;
        X[0][0] = 1;
        Y[0][0] = 1;
        Z[0][0] = 1;
        int minHW = 0;

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {

                if (Tz[i][j] == '#'){
                    X[i][j] = 0;
                    Y[i][j] = 0;
                    Z[i][j] = 0;
                    continue;
                }
                // dp 計算
                if (j >= 1){
                    dp[i][j] += X[i][j - 1];
                    dp[i][j] %= mod;
                }
                if (i >= 1){
                    dp[i][j] += Y[i - 1][j];
                    dp[i][j] %= mod;
                }
                if (i >= 1 && j >= 1) {
                    dp[i][j] += Z[i - 1][j - 1];
                    dp[i][j] %= mod;
                }
//                 累積和 計算
                if (j >= 1){
                    X[i][j] = X[i][j - 1] + dp[i][j];
                    X[i][j] %= mod;
                }
                if (i >= 1){
                    Y[i][j] = Y[i - 1][j] + dp[i][j];
                    Y[i][j] %= mod;
                }
                if (i >= 1 && j >= 1) {
                    Z[i][j] = Z[i - 1][j - 1] + dp[i][j];
                    Z[i][j] %= mod;
                }

                // 初期化
                if ((i == 0) && (Tz[i][j] != '#')){
                    Y[i][j] = dp[i][j];
                }
                if ((j == 0) && (Tz[i][j] != '#')){
                    X[i][j] = dp[i][j];
                }
                if (((i == 0) || (j == 0)) && (Tz[i][j] != '#')){
                    Z[i][j] = dp[i][j];
                }
            }
        }
        System.out.println(dp[H - 1][W - 1]);


    }
}