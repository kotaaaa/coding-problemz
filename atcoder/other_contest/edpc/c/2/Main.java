import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N+1];
        int[] Bz = new int[N+1];
        int[] Cz = new int[N+1];

        int[][] sum = new int[N+1][3];
        int minVal = 0;

        for (int i = 0; i < N; i++){
            Az[i+1] = sc.nextInt();
            Bz[i+1] = sc.nextInt();
            Cz[i+1] = sc.nextInt();
        }

        sum[1][0] = Az[1];
        sum[1][1] = Bz[1];
        sum[1][2] = Cz[1];

        for (int i = 2; i <= N; i++){
            sum[i][0] = Math.max(sum[i - 1][1], sum[i - 1][2]) + Az[i];
            sum[i][1] = Math.max(sum[i - 1][0], sum[i - 1][2]) + Bz[i];
            sum[i][2] = Math.max(sum[i - 1][0], sum[i - 1][1]) + Cz[i];
        }


        int ans = Math.max(Math.max(sum[N][0], sum[N][1]), sum[N][2]);
//        for (int i = 1; i <= N; i++){
//            System.out.println("rrr "+i+" "+sum[i]);
//        }
        System.out.println(ans);
    }
}