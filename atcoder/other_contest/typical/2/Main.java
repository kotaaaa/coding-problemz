import java.util.*;

// https://atcoder.jp/contests/atc001/tasks/dfs_a
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long M = sc.nextLong();
        long P = sc.nextLong();

        long ans = cal_pow(N, M, P);
        System.out.println(ans);

    }

    public static long cal_pow(long n, long m, long p){
        if (p <= 0){
            return 1;
        }
        if (p % 2 == 0){
            long tmp = 0;
            tmp = cal_pow(n, m, p/2);
            return tmp * tmp % m;
        } else {
            long tmp = 0;
            tmp = cal_pow(n, m, p-1) * n % m;
            return tmp;
        }
    }

    // なぜこれでできないのか？？？
//    public static long cal_pow(long n, long m, long p){
//        if (p <= 0){
//            return 1;
//        }
//        if (p % 2 == 0){
//            long tmp = 0;
//            tmp = cal_pow(n, m, p/2);
//            return tmp * tmp % m;
//        } else {
//            long tmp = 0;
//            tmp = cal_pow(n, m, (p-1)/2);
//            return tmp * tmp * n % m;
//        }
//    }
}
