import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();

        if (Math.abs(X - Y) <= 2){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
}