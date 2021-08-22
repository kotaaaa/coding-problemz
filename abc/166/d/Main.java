import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        double result = 0;
        for (int a = -120; a < 120; a++){
            for (int b = -120; b < 120; b++){
                result = Math.pow(a, 5) - Math.pow(b, 5);
                if (result == N){
                    System.out.println(a+" "+b);
                    System.exit(0);
                }
            }
        }
    }
}