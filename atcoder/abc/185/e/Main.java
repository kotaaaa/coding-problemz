import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] Az = new int[N];
        int[] Bz = new int[M];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
        }
        for (int i = 0; i < M; i++){
            Bz[i] = sc.nextInt();
        }
        int[][] dp = new int[N+1][M+1];
        for (int[] c: dp){
            Arrays.fill(c, 2001);
        }
        dp[0][0] = 0;
        for (int i = 0; i <= N; i++){
            for (int j = 0; j <= M; j++){
                // Ai の末尾を削除
                if (i > 0){
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j] + 1);
                }
                // Bi の末尾を削除
                if (j > 0){
                    dp[i][j] = Math.min(dp[i][j], dp[i][j-1] + 1);
                }
                // Ai, Bi の末尾を対応させる
                if ((i > 0) & (j > 0)){
                    if (Az[i-1] == Bz[j-1]){
                        dp[i][j] = Math.min(dp[i][j], dp[i-1][j-1]);
                    } else {
                        dp[i][j] = Math.min(dp[i][j], dp[i-1][j-1] + 1);
                    }
                }
            }
        }
        System.out.println(dp[N][M]);
    }
}