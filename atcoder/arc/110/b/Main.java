import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.nextLine();
        S = sc.nextLine();

        if (N <= 2){
            if (S.equals("0")){
                System.out.println((long) (Math.pow(10,10)));
                System.exit(0);
            }
            if (S.equals("1")){
                System.out.println((long) (2 * Math.pow(10,10)));
                System.exit(0);
            }
            if (S.equals("11")){
                System.out.println((long) Math.pow(10,10));
                System.exit(0);
            }
            if (S.equals("10")){
                System.out.println((long) Math.pow(10,10));
                System.exit(0);
            }
            if (S.equals("01")){
                System.out.println((long) Math.pow(10,10) - 1);
                System.exit(0);
            }
            System.out.println(0);
            System.exit(0);
        }


        int start = 0;
        if ((S.charAt(0) == '1') && (S.charAt(1) == '1') && (S.charAt(2) == '0')) {
            start = 3;
        } else if ((S.charAt(0) == '1') && (S.charAt(1) == '0')) {
            start = 2;
        } else if (S.charAt(0) == '0') {
            start = 1;
        }

        double cnt = 0;
        for (int i = start; i < N; i++) {
            if (cnt % 3 == 0) {
                if (S.charAt(i) != '1') {
                    System.out.println(0);
                    System.exit(0);
//                    break;
                }
            } else if (cnt % 3 == 1) {
                if (S.charAt(i) != '1') {
                    System.out.println(0);
                    System.exit(0);
//                    break;
                }
            } else {
                if (S.charAt(i) != '0') {
                    System.out.println(0);
                    System.exit(0);
//                    break;
                }
            }
            cnt++;
        }

        double len110 = 0;
        len110 = Math.ceil((double) cnt / 3) + 1 - 1;
        long ans = (long) Math.pow(10, 10);
        System.out.println((long) (ans - len110));
    }
}