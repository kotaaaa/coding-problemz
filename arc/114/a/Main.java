import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Lz = new int[N];
        int[] Rz = new int[N];
        long[] ans = new long[N];

        long n = 0;
        for (int i = 0; i < N; i++) {
            Lz[i] = sc.nextInt();
            Rz[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            n = (long) Rz[i] - Lz[i] - (Lz[i] - 1);
            if (n <= 0){
                ans[i] = 0;
            } else {
                ans[i] = n*(1+n)/2;
            }

        }
        for (int i = 0; i < N; i++) {
            System.out.println(ans[i]);
        }

    }

}
