import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N+1];
        long[] sum = new long[N+1];

        int mod = (int) Math.pow(10,9) + 7;

        for (int i = 1; i <= N; i++){
            Az[i] = sc.nextInt();
        }

        sum[N] = Az[N];
        for (int j = N - 1; j > 0; j--){
            sum[j] = sum[j + 1] + Az[j];
            sum[j] %= mod;
        }

//        System.out.println("sum start");
//        for (int j = N ; j > 0; j--){
//            System.out.println("sum "+j+" "+sum[j]);
//        }
//        System.out.println("sum end");

        long ans = 0;
        for (int i = 1; i < N; i++){
//            System.out.println("Az[i] "+Az[i]+" sum[i+1] "+sum[i+1]);
            ans += Az[i] * sum[i+1];
            ans %= mod;
        }
        System.out.println(ans);

    }
}