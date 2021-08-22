import java.util.*;

public class Main{
    static int fz[] = new int[10000001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 1; i <=N; i++) {
            fz[i] = f(i);
        }

        long ans = 0;
        for (int i = 1; i <=N; i++) {
            ans += i*fz[i];
        }
        System.out.println(ans);
    }

    public static int f (int n){
        int cnt = 0;
        int sqrtN = (int) Math.sqrt(n) + 1;
        System.out.println(sqrtN);
        for (int i = sqrtN; i >= 1; i--){
            if (n % i == 0) {
                cnt++;
                if (n/i != i){
                    cnt++;
                }
            }
        }
        return cnt;
    }
}