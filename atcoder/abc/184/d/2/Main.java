import java.util.*;
public class Main {
    static double[][][] dp = new double[101][101][101];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        System.out.println(f(A,B,C));
    }

    public static double f (int a, int b, int c){
        if (dp[a][b][c]>0) return dp[a][b][c];
        if (a==100 || b==100|| c==100) return 0;
        double ans = 0;
        ans+=(f(a+1,b,c)+1)*a/(a+b+c);
        ans+=(f(a,b+1,c)+1)*b/(a+b+c);
        ans+=(f(a,b,c+1)+1)*c/(a+b+c);
        dp[a][b][c] = ans;
        return ans;
    }
}