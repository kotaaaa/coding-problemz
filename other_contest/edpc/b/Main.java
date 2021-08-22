import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] Hz = new int[N+1];
        int[] sum = new int[N+1];
        int minVal = 0;

        for (int i = 0; i < N; i++){
            Hz[i+1] = sc.nextInt();
        }

        sum[1] = 0; // カエルは最初, 足場1にいる
        sum[2] = Math.abs(Hz[2] - Hz[1]); // 1つ目は+1ジャンプしかできない．
        for (int i = 3; i <= N; i++){
            int tempMin = Integer.MAX_VALUE;
            for (int j = 1; j <= K; j++){
                if (i - j < 1){
                    continue;
                }
                int diff = sum[i - j] + Math.abs(Hz[i] - Hz[i - j]);
                if (tempMin > diff){
                    tempMin = diff;
                }
            }
            sum[i] = tempMin;
        }

//        for (int i = 1; i <= N; i++){
//            System.out.println("rrr "+i+" "+sum[i]);
//        }
        System.out.println(sum[N]);

    }
}