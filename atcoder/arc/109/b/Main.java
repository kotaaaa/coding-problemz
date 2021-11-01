import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long sum = 0;
//        for (long i = 1; i < Math.pow(10, 10); i++){
//            sum += i;
//            System.out.println(i+" "+sum);
//        }
        long left = 1;
        long right = (long)Math.sqrt(N + 1) * 4;
        long mid = 0;
        long sumi = 0;
        while (left < right){

            mid = (left + right) / 2;

            sumi = mid * (mid + 1) / 2;
            if (N + 1 > sumi){
                left = mid + 1;
            } else if (N + 1 == sumi){
                System.out.println(N + 1 - (mid));
                System.exit(0);
                break;
            } else {
                right = mid;
            }
        }

        if (N + 1 > sumi){
            System.out.println(N + 1 - (mid));
        } else {
            System.out.println(N + 1 - (mid - 1));
        }

    }
}