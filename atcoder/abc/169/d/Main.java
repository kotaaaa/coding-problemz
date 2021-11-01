import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long origN = N;
        int sosuu = 0;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        if (N == 1) {
            System.out.println(0);
            System.exit(0);
        }
        for (int i = 2; i <= Math.sqrt(origN); i++){
//            System.out.println("i "+i);
            if (N % i != 0){
                continue;
            }
            sosuu = 1;
            int cnt = 0;
            while (N % i == 0){
                cnt++;
                N = N / i;
//                System.out.println("N "+N);
            }
            map.put(i, cnt);
//            System.out.println("N "+ N+" i "+ i+ " "+cnt);
        }

        if (sosuu == 0){
            System.out.println(1);
            System.exit(0);
        }
        int ans = 0;

        if (N > Math.sqrt (origN)) {
            if (boolSosuu(N)){
                ans++;
            }
        }


        for (int i: map.keySet()){
//            System.out.println(i+" "+ map.get(i));
            long cnt = 2;
            long sum = 1;
            int times = 1;
            int k = map.get(i);
            while (true){
                if (k >= sum + cnt){
                    sum = sum + cnt;
                    cnt++;
                } else {
                    break;
                }
                times++;
            }
//            System.out.println("sum "+sum+" times "+times);
            ans = ans + times;
        }

//        System.out.println("ans "+ans);
        System.out.println(ans);
    }


    public static boolean boolSosuu(long a){
        long origA = a;
        for (int i = 2; i <= Math.sqrt(origA); i++) {
            if (a % i == 0) {
                return false;
            }
        }
        return true;
    }
}