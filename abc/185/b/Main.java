import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int T = sc.nextInt();

        int[] Az = new int[M];
        int[] Bz = new int[M];

        for (int i = 0; i < M; i++) {
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
        }

        int sum = N;
        int before = 0;
        for (int i = 0; i < M; i++) {
            sum -= Az[i] - before;
//            System.out.println("sum "+sum);
            if (sum <= 0){
//                System.out.println("sum no "+sum);
                System.out.println("No");
                System.exit(0);
            }

            sum += Bz[i] - Az[i];
            if (sum > N){
                sum = N;
            }
            before = Bz[i];
//            System.out.println("sum "+sum);
        }

        if (before < T){
            sum -= T - before;
        }

        if (sum <= 0){
            System.out.println("No");
            System.exit(0);
        }

        System.out.println("Yes");

    }
}