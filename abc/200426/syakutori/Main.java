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
        int[] a_int = new int[N];
        for(int i = 0 ; i < N; i++) {
            a_int[i] = sc.nextInt();
        }

        // int[] a_int = new int[N];
        // for(int i = 0; i < a_array.length ; i++){
        //     a_int[i] = Integer.parseInt(a_array[i]);
        // }
        // int left = 0,
        int right = 1;
        long cnt = 0;
        for (int left = 0; left < N; left++) {
            System.out.println(left+" "+right+" "+cnt);
            while (right < N && (right == left || a_int[right - 1] < a_int[right])) {
                right++;
            }
            cnt += right - left;
            if (left == right) right++;
        }
        System.out.println(cnt);
    }
}
