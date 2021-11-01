import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String t = sc.next();

        char first = t.charAt(0);
        for (int i = 1; i < t.length(); i++){
            if (first != t.charAt(i)){
                System.out.println("Lost");
                System.exit(0);
            }
        }
        System.out.println("Won");

    }
}