import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int d = sc.nextInt();

        int[] xz = new int[n];
        int[] yz = new int[n];

        for (int i = 0; i < n; i++){
            xz[i] = sc.nextInt();
            yz[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++){
            if ((xz[i] < s) && (yz[i] > d)) {
                System.out.println("Yes");
                System.exit(0);
            }
        }
        System.out.println("No");
    }
}