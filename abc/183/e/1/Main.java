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
        int mod = 1000000007;

        dp[0][0] = 1;
        int minHW = 0;

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {

                if (Tz[i][j] == '#'){
                    continue;
                }

                // 横
                if (j >= 1){
                    for (int k = 1; k <= j; k++){
                        if (Tz[i][j - k] != '#') {
                            dp[i][j] += dp[i][j - k];
                            dp[i][j] %= mod;
                        } else {
                            break;
                        }
                    }
                }

                // たて
                if (i >= 1){
                    for (int k = 1; k <= i; k++){
                        if (Tz[i - k][j] != '#') {
                            dp[i][j] += dp[i - k][j];
                            dp[i][j] %= mod;
                        } else {
                            break;
                        }
                    }
                }

//                int minHW = 0;
//                if (i < j){
//                    minHW = i;
//                } else {
//                    minHW = j;
//                }
                minHW = Math.min(i,j);

                // ナナメ
                if (i >= 1 && j >= 1) {
                    for (int k = 1; k <= minHW; k++) {
                        if (Tz[i - k][j - k] != '#') {
                            dp[i][j] += dp[i - k][j - k];
                            dp[i][j] %= mod;
                        } else {
                            break;
                        }
                    }
                }

//                System.out.println(Tz[i][j]);
            }
        }

//        for (int i = 0; i < H; i++) {
//            for (int j = 0; j < W; j++) {
//                System.out.println("i "+i+" j "+j +" >> "+dp[i][j]);
//            }
//        }
//        System.out.println("ans "+dp[H - 1][W - 1]);

        System.out.println(dp[H - 1][W - 1]);


    }
}