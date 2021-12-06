import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = (long) sc.nextDouble() * 10000; //  % 1;
        long y = (long) sc.nextDouble() * 10000; //  % 1;
        long r = (long) sc.nextDouble() * 10000;

//        System.out.println((long) Math.floor(4));
//        System.out.println((long) Math.floor(4.1));
//
//        System.out.println((long) Math.ceil(4));
//        System.out.println((long) Math.ceil(4.1));

        long xmax = (long) Math.floor(x + r); //切り捨て
        long xmin = (long) Math.ceil(x - r); // 切り上げ

        long p = 0;
        long ymin = 0;
        long ymax = 0;
        long sum = 0;

        for (long i = xmin; i <= xmax; i++) {
            p = (long) Math.sqrt((r * r) - ((i - x) * (i - x)));
            ymax = (long) Math.floor(y + p); // 切り捨て
            ymin = (long) Math.ceil(y - p); // 切り上げ
            sum += ymax - ymin + 1;
//            sum += Math.ceil((y + p) - (y - p));
        }
//        System.out.println(sum / 10000);
        System.out.println(sum);
    }
}