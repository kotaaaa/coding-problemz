import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        String S = sc.nextLine();
        S = sc.nextLine();
//        System.out.println("sss "+S+" eee");

        for (int i = 0; i < S.length(); i++){
//            System.out.println(S.charAt(i));
            if (S.charAt(i) == 'x'){
                if (X > 0){
                    X--;
                }
            } else {
//                System.out.println("aa");
                X++;
            }
        }

        System.out.println(X);

    }
}