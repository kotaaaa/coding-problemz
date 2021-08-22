import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.nextLine();
        String T = sc.nextLine();

        int[][] dp = new int[S.length()+1][T.length()+1];

        dp[0][0] = 0;

        StringBuilder sb = new StringBuilder();
        StringBuilder sb_ = new StringBuilder();

        int cnt = 1;
        for (int i = 0; i <= S.length(); i++){
            for (int j = 0; j <= T.length(); j++){

                if (i > 0){
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                }
                if (j > 0){
                    dp[i][j] = Math.max(dp[i][j], dp[i][j-1]);
                }

                if ((i > 0) && (j > 0)){
                    if (S.charAt(i-1) == T.charAt(j-1)){
                        dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + 1);
                    }
                }
            }
        }

        int i = S.length();
        int j = T.length();

        while (i > 0 && j > 0){
            if (dp[i][j] == dp[i-1][j]){
                i--;
            } else if (dp[i][j] == dp[i][j-1]){
                j--;
            } else {
                sb.insert(0, S.charAt(i-1));
                i--; j--;
            }
        }

        System.out.println(sb.toString());

    }
}