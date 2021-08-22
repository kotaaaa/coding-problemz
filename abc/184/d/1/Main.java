import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        double[][][] dp = new double[101][101][101];
        dp[A][B][C] = 1;
        dp[A-1][B][C] = 1;
        dp[A][B-1][C] = 1;
        dp[A][B][C-1] = 1;
        double ans = 0;
        for (int a = A; a <= 99; a++){
            for (int b = B; b <= 99; b++){
                for (int c = C; c <= 99; c++){
                    System.out.println(a+" "+b+" "+c);
                    if ((a == 99) && (b == 99) && (c == 99)){
                        ans = dp[99][99][99] + dp[99][99][99] + dp[99][99][99];
                        System.out.println(ans);
                        System.exit(0);
                    }
                    System.out.println((a+b+c));
                    System.out.println((double) a/(a+b+c));
                    System.out.println((double) b/(a+b+c));
                    System.out.println((double) c/(a+b+c));
                    System.out.println("dp[a][b][c] "+dp[a][b][c]);
                    dp[a][b][c] += dp[a-1][b][c] * ((double) (a-1)/(a+b+c));
                    System.out.println("dp[a][b][c] "+dp[a][b][c]);
                    dp[a][b][c] += dp[a][b-1][c] * ((double) (b-1)/(a+b+c));
                    System.out.println("dp[a][b][c] "+dp[a][b][c]);
                    dp[a][b][c] += dp[a][b][c-1] * ((double) (c-1)/(a+b+c));
                    System.out.println("dp[a][b][c] "+dp[a][b][c]);
                }
            }
        }

//        System.out.println(dp[100][99][99]);
//        System.out.println(dp[99][100][99]);
//        System.out.println(dp[99][99][100]);
//        double ans = dp[100][99][99] + dp[99][100][99] + dp[99][99][100];
        ans = dp[99][99][99] + dp[99][99][99] + dp[99][99][99];
        System.out.println(ans);


    }
}