import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
//        System.out.println("N "+N);
        BigInteger bigIntN = new BigInteger(String.valueOf(N));
        BigInteger ans = new BigInteger(String.valueOf("0"));
        long mod = (long) Math.pow(10,9) + 7;
        BigInteger bigIntMod = new BigInteger(String.valueOf(mod));
        BigInteger a = new BigInteger("0");
        BigInteger b = new BigInteger("0");
        BigInteger c = new BigInteger("0");
        BigInteger base10 = new BigInteger("10");
        BigInteger base9 = new BigInteger("9");
        BigInteger base8 = new BigInteger("8");

        a = base10.modPow(bigIntN,bigIntMod);
        b = base9.modPow(bigIntN,bigIntMod);
        c = base8.modPow(bigIntN,bigIntMod);

//        System.out.println("a " +a);
//        System.out.println("b " +b);
//        System.out.println("c " +c);
//        ans = a - b - b + c;
        ans = ans.add(a);
        ans = ans.subtract(b);
        ans = ans.subtract(b);
        ans = ans.add(c);
        ans = ans.add(bigIntMod);
        ans = ans.remainder(bigIntMod);
//        System.out.println(ans);
        ans = ans.add(bigIntMod);
        ans = ans.remainder(bigIntMod);
        System.out.println(ans);
    }
}