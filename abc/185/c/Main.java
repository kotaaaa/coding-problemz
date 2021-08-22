import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();

        System.out.println(Combination(L-1,11));
//        System.out.println(Math.pow(2,63));
//        System.out.println(Combination(L-1,11) < Math.pow(2,63));

    }

    public static long Combination(int n, int r) { //cmb
        if (n < 0 || r < 0 || r > n) return -1;
        if (n - r < r) r = n - r;
        if (r == 0) return 1;
        if (r == 1) return n;
        int[] numerator = new int[r];
        int[] denominator = new int[r];
        for (int k = 0; k < r; k++) {
            numerator[k] = n - r + k + 1;
            denominator[k] = k + 1;
        }
        for (int p = 2; p <= r; p++) {
            int pivot = denominator[p - 1];
            if (pivot > 1) {
                int offset = (n - r) % p;
                for (int k = p - 1; k < r; k += p) {
                    numerator[k - offset] /= pivot;
                    denominator[k] /= pivot;
                }
            }
        }
        long result = 1;
        for (int k = 0; k < r; k++) {
            if (numerator[k] > 1) result *= numerator[k];
        }
        return result;
    }
}