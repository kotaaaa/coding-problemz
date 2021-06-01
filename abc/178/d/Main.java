import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt();

        int[] sum = new int[S + 1];
        sum[0] = 1;
        for (int i = 3; i <= S; i++) {
            for (int j = 0; j <= i - 3; j++) {
                sum[i] += sum[j];
                sum[i] %= Math.pow(10,9)+7;
            }
        }
        System.out.println(sum[S]);
//        for (int i = 0; i <= S; i++){
//            System.out.println("aa "+ sum[i]);
//        }
    }
}