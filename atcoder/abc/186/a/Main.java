import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] A = new int[4];
//                sc.nextInt();
//        int A2 = sc.nextInt();
//        int A3 = sc.nextInt();
//        int A4 = sc.nextInt();

        int min = 101;
        for (int i = 0; i < 4; i++){
            A[i] = sc.nextInt();
            if (min > A[i]){
                min = A[i];
            }
        }
        System.out.println(min);


    }
}