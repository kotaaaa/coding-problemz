import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int W = sc.nextInt();

        int[] Sz = new int[N];
        int[] Tz = new int[N];
        int[] Pz = new int[N];

        int tmax = 0;
        for (int i = 0; i < N; i++) {
            Sz[i] = sc.nextInt();
            Tz[i] = sc.nextInt();
            if (Tz[i] > tmax){
                tmax = Tz[i];
            }
            Pz[i] = sc.nextInt();
        }

        long[] sum = new long[tmax+1];
        long[] delta = new long[tmax+1];

        for (int i = 0; i < N; i++){
            delta[Sz[i]] += Pz[i];
            delta[Tz[i]] -= Pz[i];
        }

        sum[0] = delta[0];
        for (int i = 1; i <= tmax; i++){
            sum[i] = sum[i - 1] + delta[i];
        }
        for (int i = 0; i <= tmax; i++){
            if (sum[i] > W){
                System.out.println("No");
                System.exit(0);
            }
        }
        System.out.println("Yes");


    }
}