import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long X = sc.nextLong();
        long Y = sc.nextLong();
        long A = sc.nextLong();
        long B = sc.nextLong();


        long cnt = 0;

//        while(true){
//
//            if (A * sum > B) {
//                break;
//            }
//            sum = A * sum;
//            cnt += 1;
//        }
//
//        long syou = (long) Math.ceil( ((double) (Y - sum) / B) - 1);
//        cnt += syou;
//
//        System.out.println(cnt);

        while ((A*X < X*B) && X <= Long.MAX_VALUE / A && ((A*X) < Y)){
            X *= A;
            cnt += 1;
        }

        cnt += (Y - X - 1)/ B;
        System.out.println(cnt);


    }
}


//1000000007
//2000000000