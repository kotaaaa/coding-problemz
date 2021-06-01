import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N+1];
        int[] sum = new int[N+1];
//        int[] allSum = new int[N+1];
        int[] piz = new int[N+1];

        for (int i = 1; i <= N; i++){
            Az[i] = sc.nextInt();
        }

        sum[1] = Az[1];
        piz[1] = Az[1];
//        allSum[1] = Az[1];
        int tmpMax = Math.max(0,Az[1]);
        for (int i = 2; i <= N; i++){
            sum[i] = Az[i] + sum[i - 1];
//            allSum[i] = sum[i] + allSum[i - 1];
            if (sum[i] > tmpMax) {
                tmpMax = sum[i];
            }
            piz[i] = tmpMax;
        }
//        System.exit(0);

        int r = 0;
        int x = 0;
        for (int i = 1; i <= N; i++){
            System.out.println("r "+r+" x "+x);
            r = Math.max(r, x + piz[i]);
            x = x + sum[i];
        }
//
//        System.out.println("sum[i], piz[i], +allSum[i]");
//        for (int i = 1; i <= N; i++){
//            System.out.println(sum[i]+" "+piz[i]+" "+allSum[i]);
//        }
//        System.out.println("r "+r);
        System.out.println(r);

    }
}
