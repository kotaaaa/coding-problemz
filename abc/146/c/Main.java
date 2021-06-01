import java.util.*;

public class Main {

    Scanner sc = new Scanner(System.in);
    int A = sc.nextInt();
    int B = sc.nextInt();
    long X = sc.nextLong();

    public static void main (String[] args) {

        Scanner sc = new Scanner(System.in);
        long A = sc.nextInt();
        long B = sc.nextInt();
        long X = sc.nextLong();

        int left = 1;
        int right = 1000000000;
        int mid = 0;
        long price = 0;
        int ans = 0;
        while (left < right){
            mid = (left + right) / 2;
            price = check(A, B, mid);
            System.out.println(left+" "+right+" "+mid+" "+price);
            if (price == X){
                System.out.println("%%%%%");
                ans = mid;
                break;
            } else if (price > X){
                ans = mid;
                right = mid;
            } else {
                ans = mid;
                left = mid + 1;
            }
        }
        System.out.println("ans: "+ans);
    }

    public static long check(long A, long B, int n) {
//        System.out.println(A +" "+ n +" "+B+" "+String.valueOf(n).length());
//        System.out.println(A * n +" "+B * String.valueOf(n).length());
        long leftTerm = A * n;
        long rightTerm = B * String.valueOf(n).length();
//        System.out.println("l "+ leftTerm+" "+rightTerm+" "+(leftTerm+rightTerm));
        return leftTerm + rightTerm;
//        System.out.println("cal "+A * n + B * String.valueOf(n).length());
//        return A * n + B * String.valueOf(n).length();


    }

}
