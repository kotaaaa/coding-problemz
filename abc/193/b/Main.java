import java.util.*;
//import Math;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] a = new int[n];
        int[] p = new int[n];
        int[] x = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            p[i] = sc.nextInt();
            x[i] = sc.nextInt();
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (x[i] - a[i] >= 1) {
                min = Math.min(min, p[i]);
            }
        }

        if (min == Integer.MAX_VALUE) {
            System.out.println("-1");
            System.exit(0);
        }
        System.out.println(min);

    }
}