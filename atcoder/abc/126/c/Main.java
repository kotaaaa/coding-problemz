import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int num = 0;
        int cnt = 0;
        double ans = 0;
        double prob = (double) 1/N;
//        System.out.println(prob);

        for (int i = 1; i <= N; i++){
            num = i;
            cnt = 0;
            while(num < K){
                cnt++;
                num *= 2;
            }
            ans += prob * Math.pow(0.5, cnt);
        }
        System.out.println(ans);
    }
}