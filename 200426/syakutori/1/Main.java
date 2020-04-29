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
        String[] a_array = new String[N];
        a_array = sc.nextLine().split(" ");
        int[] a_int = new int[N];
        for(int i = 0; i < a_array.length ; i++){
            a_int[i] = Integer.parseInt(a_array[i]);
        }
        int left = 0, right = 1, cnt = 0;
        while(true){
            if (left == a_int.length && right == a_int.length) break;
            if (a_int[right-1] < a_int[right]){
                right++;
                // cnt++;
            } else if (left == right){
                left++;
                right++;
            } else {//left<right
                left++;
            }
            cnt++;
            System.out.println(left+" "+right+" "+cnt);
        }
        System.out.println(cnt);
    }
}
