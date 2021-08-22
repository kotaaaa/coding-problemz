import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Hz = new int[N+1];
        int[] sum = new int[N+1];

        for (int i = 0; i < N; i++){
            Hz[i+1] = sc.nextInt();
        }

        sum[1] = 0; // カエルは最初, 足場1にいる
        sum[2] = Math.abs(Hz[2] - Hz[1]); // 1つ目は+1ジャンプしかできない．
        for (int i = 3; i <= N; i++){
            int before2 = 0; int before1 = 0;
            before2 = sum[i - 2] + (Math.abs(Hz[i] - Hz[i - 2]));
            before1 = sum[i - 1] + (Math.abs(Hz[i] - Hz[i - 1]));
            sum[i] = Math.min(before2, before1);
        }

//        for (int i = 0; i < N; i++){
//            System.out.println("rrr "+sum[i]);
//        }
        System.out.println(sum[N]);

    }
}