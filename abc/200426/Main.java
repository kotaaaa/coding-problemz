import java.util.*;
import java.util.Arrays;

public class Main {
    static int f (int n){
        if (n == 1) return 1;
        if (n == 0) return 0;
        return n + f(n-1);
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N;
        N = Integer.parseInt(sc.nextLine());
        // String[] a_array = new String[N];
        // a_array = sc.nextLine().split(" ");
        // int[] a_int = new int[N];
        // for(int i = 0; i < a_array.length ; i++){
            // a_int[i] = Integer.parseInt(a_array[i]);
        // }
        int[] a_int = new int[N];
        for(int i = 0 ; i < N; i++) {
            a_int[i] = sc.nextInt();
        }

        int[] memo = new int[N];
        long cnt = 0;
        for (int i = 0; i < a_int.length; i++){
            int k = 1;
            int zouka = 0;
            while (true){
                if (i+k == a_int.length) break;
                if (memo[i+k-1] == 0) memo[i+k-1] = 1;
                else break;

                if (a_int[i+k-1] < a_int[i+k]){
                    zouka++;
                    k++;
                    continue;
                }
                else break;
            }
            cnt+=f(zouka);
        }
        cnt += a_int.length;
        System.out.println(cnt);
    }
}
