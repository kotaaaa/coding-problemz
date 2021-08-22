import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int R = sc.nextInt();
        int S = sc.nextInt();
        int P = sc.nextInt();
        String T = sc.nextLine();
        T = sc.nextLine();

        int maxIdx = 0;
        int max = 0;
        int[] te = new int[N];

        int[] Rz = new int[N];
        int[] Sz = new int[N];
        int[] Pz = new int[N];

        // グー: 1, チョキ :2, パー :3
        // 初回
        if('r' == T.charAt(0)){
            max = P;
            maxIdx = 1;
            te[0] = 1;
        } else if ('s' == T.charAt(0)){
            max = R;
            maxIdx = 2;
            te[0] = 2;
        } else {
            max = S;
            maxIdx = 4;
            te[0] = 4;
        }
        for (int i = 1; i < N; i++) {
            int currentMax = max;
            if (i < K){
                if('r' == T.charAt(i)){
                    max = currentMax + P;
                    maxIdx = 1;
                    te[i] = 1;
                } else if ('s' == T.charAt(i)){
                    max = currentMax + R;
                    maxIdx = 2;
                    te[i] = 2;
                } else {
                    max = currentMax + S;
                    maxIdx = 4;
                    te[i] = 4;
                }
                continue;
            }
            if (Integer.bitCount(te[i - K]) == 2){

            }

            if (i - k)
        }

    }
}