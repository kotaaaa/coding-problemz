import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long y = sc.nextLong();
        long a = sc.nextLong();
        long b = sc.nextLong();
        long exp = 0;
        while(x * a < x + b && x <= Long.MAX_VALUE / a && x * a < y ) {
            x *= a;
            exp++;
        }
        exp += (y - 1 - x) / b;
        System.out.println(exp);
    }
}