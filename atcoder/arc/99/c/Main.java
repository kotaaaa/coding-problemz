import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] Az = new int[N];
        for (int i = 0; i < N; i++){
            sc.nextInt();
        }

        int tmp = 0; int ans = 0;
        tmp = N - K;
        if (tmp <= 0){
            System.out.println("1");
            System.exit(0);
        } else {
            ans++;
        }

        ans += Math.ceil((double) tmp / (K-1));
        System.out.println(ans);
    }
}

