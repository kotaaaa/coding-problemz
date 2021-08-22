import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Xz = new int[N];

        for (int i = 0; i < N; i++){
            Xz[i] = sc.nextInt();
        }

        long mann = 0;
        double yuu = 0;
        long che = 0;

        for (int i = 0; i < N; i++){
            mann += Math.abs(Xz[i]);
        }
        System.out.println(mann);

        for (int i = 0; i < N; i++){
            yuu += Math.pow(Xz[i],2);
        }
        System.out.println(Math.sqrt(yuu));

        for (int i = 0; i < N; i++){
            if (che < Math.abs(Xz[i])) {
                che = Math.abs(Xz[i]);
            }
        }
        System.out.println(che);

    }
}