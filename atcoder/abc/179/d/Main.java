import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] Lz = new int[K];
        int[] Rz = new int[K];

        for (int i = 0; i < K; i++) {
            Lz[i] = sc.nextInt();
            Rz[i] = sc.nextInt();
        }

        long[] sum = new long[N+1];
        long[] s = new long[N+1];

        s[0] = 0;
        s[1] = 1;
        sum[1] = 1;
        long mod = 998244353L;

        for (int i = 2; i <= N; i++){
            for (int j = 0; j < K; j++){
                int li = i - Lz[j];
                int ri = i - Rz[j] - 1;
                ri = Math.max(ri, 0);
                if (li >= 1){
                    sum[i] += (s[li] - s[ri]) % mod;
                    if (sum[i] < 0){
                        long tmp = sum[i];
                        sum[i] = mod - (-1)*tmp;
                    }
                }
            }
            s[i] = (s[i-1] + sum[i]) % mod;
        }
        System.out.println(sum[N] % mod);
//        System.out.println(sum[N]);

//        for (int i = 1; i <= N; i++){
//            System.out.println(i+">> "+sum[i]+" "+s[i]);
////            if (i == 100) break;
//            if (sum[i] < 0 || s[i] < 0) break;
//        }
    }
}