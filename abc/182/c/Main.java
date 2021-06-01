import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();

        if (N <= 10){
            if (N % 3 == 0){
                System.out.println("0");
            } else {
                System.out.println("-1");
            }
            System.exit(0);
        }

        String StrN = String.valueOf(N);
        int[] amariEach = new int[StrN.length()];

        int amari0 = 0;
        int amari1 = 0;
        int amari2 = 0;

        int sumN = 0;
        int amariSum = 0;
        for (int i = 0; i < StrN.length(); i++){

            sumN += (StrN.charAt(i) - 48);
            amariEach[i] = (StrN.charAt(i) - 48) % 3;
            if (amariEach[i] == 0){
                amari0++;
            }
            else if (amariEach[i] == 1){
                amari1++;
            } else {
                amari2++;
            }
        }

        amariSum = sumN % 3;

        if (amariSum == 0){
            System.out.println("0");
            System.exit(0);
        }
        if (amariSum == 1){
            if (amari1 >= 1){
                System.out.println("1");
                System.exit(0);
            }
            if ((amari2 >= 2) && (StrN.length() >= 3)){
                System.out.println("2");
                System.exit(0);
            }
        }
        if (amariSum == 2){
            if (amari2 >= 1){
                System.out.println("1");
                System.exit(0);
            }
            if ((amari1 >= 2) && (StrN.length() >= 3)){
                System.out.println("2");
                System.exit(0);
            }
        }

        System.out.println("-1");

    }
}