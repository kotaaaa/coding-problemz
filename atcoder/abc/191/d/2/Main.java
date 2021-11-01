import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x = sc.nextDouble(); //  % 1;
        double y = sc.nextDouble(); //  % 1;
        double r = sc.nextDouble();

//        long xmax = (long) Math.floor(x + r); //切り捨て
//        long xmin = (long) Math.ceil(x - r); // 切り上げ
        xmax = (x - r) / 10000;
        xmin = (x + r) / 10000;

        double p = 0;
        long ymin = 0;
        long ymax = 0;
        long sum = 0;

        for (long i = xmin; i <= xmax; i++) {
            p = Math.sqrt((r * r) - ((i - x) * (i - x)));
//            ymax = (long) Math.floor(y + p); // 切り捨て
//            ymin = (long) Math.ceil(y - p); // 切り上げ
            ymax =
            sum += ymax - ymin + 1;
        }
        System.out.println(sum);
    }
}