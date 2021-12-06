import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long K = sc.nextLong();
        int[] Az = new int[N];
        for (int i = 0; i < N; i++) {
            Az[i] = sc.nextInt();
        }
        int left = 0;
        int right = 0;
        long sum = 0;
        long count = 0;
        sum += Az[0];
        while (left < N) {
            if (left > right) {
                right++;
                sum += Az[right];
                continue;
            }
//            sum = 0;
//            for (int i = left; i <= right; i++) {
//                sum += Az[i];
//            }
//            System.out.println("sum "+sum+" left "+left+" right "+right+" count "+count);
            if (sum >= K) {
                left++;
                sum -= Az[left - 1];
//                count++;
                count += N - right;
            } else {
                if (right == N - 1){
                    break;
                }
                right++;
                sum += Az[right];
            }
//            System.out.println("sum "+sum+" left "+left+" right "+right+" count "+count);
        }
        System.out.println(count);
    }
}