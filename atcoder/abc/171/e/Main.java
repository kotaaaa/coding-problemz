import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
        }

        long sum = 0;
        for (int i = 0; i < N; i++){
            sum = sum ^ Az[i];
        }

        for (int i = 0; i < N; i++){
            System.out.print(sum ^ Az[i]);
            System.out.print(" ");
        }
    }
}