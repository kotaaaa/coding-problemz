import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int W = sc.nextInt();
        int[] Wz = new int[N+1];
        int[] Vz = new int[N+1];

        for (int i = 0; i < N; i++){
            Wz[i+1] = sc.nextInt();
            Vz[i+1] = sc.nextInt();
        }

        long[][] sum = new long[N+1][W+1];

        for (int i = 1; i <= N; i++){
            for (int j = 0; j <= W; j++){
                if (j - Wz[i] >= 0){
                    sum[i][j] = Math.max(Vz[i] + sum[i - 1][j - Wz[i]], sum[i - 1][j]);
                } else {
                    sum[i][j] = sum[i - 1][j];
                }
            }
        }
        System.out.println(sum[N][W]);
    }
}