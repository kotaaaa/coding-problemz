import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long X = sc.nextLong();
        long Y = sc.nextLong();
        long A = sc.nextLong();
        long B = sc.nextLong();
        long n = 0;

        while((X < (X+B)/A) && (X < Y/A)){
            X *= A;
            n++;
        }
        n += (Y-X-1)/B;

        System.out.println(n);
    }
}