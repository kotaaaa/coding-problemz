import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mod = 1000000007;
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] sum = new int[N+1];

        for (int i = 1; i <= N; i++){
            sum[i] = sum[i - 1] + i;
        }
        int ans = 0;
        int minK = 0;
        int maxK = 0;
        for (int i = K - 1; i <= N; i++) {
            minK = sum[i];
            if (N - i + 1 < 0){
                maxK = sum[N];
            } else {
                maxK = sum[N] - sum[N - i + 1];
            }

            ans += (maxK - minK);
            System.out.println(i+" ++ "+(maxK - minK + 1));
        }



//        minK = sum[K];
//        maxK = sum[N] - sum[N - K];

//        for (int i = 1; i <= N; i++){
//            System.out.println(sum[i]);
//        }

//        System.out.println("maxK "+maxK);
//        System.out.println("minK "+minK);
        System.out.println(ans);





    }
}