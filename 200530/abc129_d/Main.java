import java.util.*;


public class Main {
//    static int count = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
//        System.out.println(a);
        int n = Integer.toString(a).length();
        int memo[][][] = new int[11][2][11];
        memo[0][0][0] = 1;
        for (int i = 0; i < n; i++) {
            int ni = Integer.toString(a).charAt(i);
            for (int j = 0; j < 10; j++){
                //i桁目がNより小さく，i+1桁目もNより小さい
                memo[i + 1][1][j] += memo[i][1][j] * 9;
                memo[i + 1][1][j + 1] += memo[i][1][j];

                //i桁目までがNで，i+1桁目は，Nより小さい
                if (ni > 1) {
                    memo[i + 1][1][j] += memo[i][0][j] * (ni - 1);
                    memo[i + 1][1][j + 1] += memo[i][0][j];
                } else if (ni == 1){
                    memo[i + 1][1][j] += memo[i][0][j];
                }
                //i桁目までがNで，i+1桁目もN
                if (ni == 1) {
                    memo[i + 1][0][j + 1] = memo[i][0][j];
                } else {
                    memo[i + 1][0][j] = memo[i][0][j];
                }
            }
        }
        int ans = 0;
        for (int j = 0; j < 10; j++){
            ans += (memo[n][0][j] + memo[n][1][j]) * j;
        }
        System.out.println(ans);

    }
}