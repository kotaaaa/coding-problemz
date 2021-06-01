import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long b = sc.nextLong();
        long c = sc.nextLong();
        long in = 0;
        long out = 0;
        in = Math.min(c+1, 2*b+1);
        if ((c - b)/2+1 > 0){
            out = (c - b)-1;
        } else {
            out = 0;
        }

        System.out.println("in "+in);
        System.out.println("out "+out);
        System.out.println(in + out);
    }
}