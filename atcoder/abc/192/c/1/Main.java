import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        long a = n;
//        long aNext = 0;
        for (int i = 0; i < k; i++) {
            a = f(a);
//            System.out.println("a "+a);
//            break;
        }
        System.out.println(a);
    }

    public static long f (long x) {
        char[] g1 = String.valueOf(x).toCharArray();
        Arrays.sort(g1);
        String g1Str = new String(g1);
        long g1Long = Long.parseLong(g1Str);

        char[] g2 = String.valueOf(x).toCharArray();
//        Arrays.sort(g2, Collections.reverseOrder());
//        Arrays.sort(g2);
        StringBuilder sb = new StringBuilder();
        for (int i = g1Str.length()-1; i >= 0; i--){
            sb.append(g1Str.charAt(i));
        }
        String g2Str = sb.toString();
        long g2Long = Long.parseLong(g2Str);

//        System.out.println("g1Long "+g1Long+" g2Long "+g2Long);
        return g2Long - g1Long;
    }
}