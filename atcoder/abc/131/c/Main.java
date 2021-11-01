import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();
        long B = sc.nextLong();
        long C = sc.nextLong();
        long D = sc.nextLong();

        long lcm = 0;
        lcm = C / gcd(C, D) * D;

        long numB = 0;
        long numA = 0;

//        System.out.println("lcm "+lcm+" B "+B);
//        System.out.println("b " + (B / C)+" "+ (B / D) +" "+(B / lcm));
//        System.out.println("a " + ((A-1) / C)+" "+ ((A-1) / D) +" "+ ((A-1) / lcm));
        numB = B / C + B / D - (B / lcm);
        numA = (A-1) / C + (A-1) / D - ((A-1) / lcm);

//        System.out.println("numB "+ numB);
//        System.out.println("numA "+ numA);
        System.out.println(B - numB - (A-1 - numA));

    }

    public static long gcd(long a, long b){
        if (a == 0) return b;
        if (b == 0) return a;

        long tmp = 0;
        if (a > b){
            tmp = a;
            a = b;
            b = tmp;
        }
        return gcd(a, b % a);
    }
}