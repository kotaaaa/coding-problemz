import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        int K = sc.nextInt();
        int[] h = new int[K + 1];
        int[] w = new int[K + 1];
        char[][] mass = new char[H + 1][W + 1];

        long mod = 998244353;

        long noMarkCnt = 1;
        for (int i = 0; i < H*W - K; i++) {
            noMarkCnt = noMarkCnt*3 % mod;
        }

        System.out.println("noMarkCnt "+noMarkCnt);
        for (int i = 1; i <= K; i++) {
            h[i] = sc.nextInt();
            w[i] = sc.nextInt();
            char t = sc.next().toCharArray()[0];
//            if (t == 'D') {
            mass[h[i]][w[i]] = t;
//            } else if (t == 'R') {
//            mass[h[i]][w[i]] = 1;
//            } else {
//            mass[h[i]][w[i]] = 2;
//            }
        }

        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= W; j++) {
                System.out.println(i + " " + j + " " + mass[i][j]);
            }
        }

        long[][] dp = new long[H + 1][W + 1];
        dp[1][1] = 1;


        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= W; j++) {
                System.out.println("i "+i+" j "+j+" "+mass[i][j]+" "+dp[i][j]);
                if (i == H && j == W) {
                    break;
                }
                if (mass[i][j] == 'X') {
                    if (i + 1 <= H) {
                        dp[i + 1][j] += dp[i][j] % mod;
                    }
                    if (j + 1 <= W) {
                        dp[i][j + 1] += dp[i][j] % mod;
                    }
                } else if (mass[i][j] == 'D') {
                    if (i + 1 <= H) {
                        dp[i + 1][j] += dp[i][j] % mod;
                    }
                } else if (mass[i][j] == 'R') {
                    if (j + 1 <= W) {
                        dp[i][j + 1] += dp[i][j] % mod;
                    }
                } else {
                    if (i + 1 <= H) {
                        dp[i + 1][j] += 2 * dp[i][j] % mod;
                    }
                    if (j + 1 <= W) {
                        dp[i][j + 1] += 2 * dp[i][j] % mod;
                    }
//                    noMarkCnt++;/**/
                }
            }
        }

        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= W; j++) {
                System.out.println("i "+i+" j "+j+" "+dp[i][j]);
            }
        }

        System.out.println(dp[H][W]);

    }
}
