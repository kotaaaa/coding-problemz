import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long X = sc.nextLong();
        long K = sc.nextLong();
        long D = sc.nextLong();
        long syou = 0;
        long amari1 = 0;
        long amari2 = 0;
        long ans = 0;

//        double waruResult = X / D;
        syou = (long) Math.ceil((double) X / D) - 1;
        System.out.println(syou+" syou");
        amari1 = X % D;
        amari2 = D - amari1;

        System.out.println(amari1+" "+amari2);
        if (K <= syou){
            System.out.println(X - D * K);
            System.exit(0);
        }

        if ((K - syou) % 2 == 0){
            ans = amari1;
        } else {
            ans = amari2;
        }
        System.out.println(ans);
    }
}

//1000000000000000
//1000000000000000


//1000000000000000
//1000000000000000


//import java.util.*;
//
//public class Main {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        long X = sc.nextLong();
//        long K = sc.nextLong();
//        long D = sc.nextLong();
//        long syou = 0;
//        long amari1 = 0;
//        long amari2 = 0;
//        long ans = 0;
//
////        double waruResult = X / D;
//        syou = (long) Math.ceil((double) X / D) - 1;
//        System.out.println(syou+" syou");
//        amari1 = X % D;
//        amari2 = D - amari1;
//
//        System.out.println(amari1+" "+amari2);
//        if (K <= syou){
//            System.out.println(X - D * K);
//            System.exit(0);
//        }
//
//        if ((K - syou) % 2 == 0){
//            ans = amari1;
//        } else {
//            ans = amari2;
//        }
//        System.out.println(ans);
//    }
//}
//
////1000000000000000
////1000000000000000
//
//
////1000000000000000
////1000000000000000