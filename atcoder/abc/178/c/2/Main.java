import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
//        long mod = (long) Math.pow(10, 9) + 7;
        long mod = 1000000007;
        long ans = 0;
        long ans10 = 1; long ans9 = 1; long ans8 = 1;
        for (int i = 0; i < N; i++){
//            ans10 *= 10;
//            ans10 %= mod;
            ans10 = (ans10 * 10) % mod;
        }
        for (int i = 0; i < N; i++){
//            ans9 *= 9;
//            ans9 %= mod;
            ans9 = (ans9 * 9) % mod;
        }
        for (int i = 0; i < N; i++){
//            ans10 *= 8;
//            ans10 %= mod;
            ans8 = (ans8 * 8) % mod;
        }
//        System.out.println("a "+ans10);
//        System.out.println("b "+ans9);
//        System.out.println("c "+ans8);
        ans = ans10 - ans9 - ans9 + ans8;
        ans %= mod;
        ans=(ans+mod)%(mod);
        System.out.println(ans);
    }
}