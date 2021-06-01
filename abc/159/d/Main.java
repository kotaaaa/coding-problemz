import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N];
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            if (!map.keySet().contains(Az[i])){
                map.put(Az[i],1);
            } else {
                map.put(Az[i],map.get(Az[i]) + 1);
            }
        }
        long sumCmb = 0;
        for (int i: map.keySet()){
            if (map.get(i) > 1){
                sumCmb += Combination(map.get(i), 2);
            }
        }
        long ans = sumCmb;
        for (int i = 0; i < N; i++){
            if (map.get(Az[i]) == 1){
                System.out.println(ans);
            }
            else if (map.get(Az[i]) == 2){
                System.out.println(ans - 1);
            } else {
                System.out.println(ans - Combination(map.get(Az[i]),2) + Combination(map.get(Az[i]) - 1, 2));
            }
        }
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