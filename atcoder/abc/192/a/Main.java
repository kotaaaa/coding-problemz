import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int ans = x % 100;
        if (ans == 0) {
            System.out.println(100);
            System.exit(0);
        }
        System.out.println(100-ans);

    }
}