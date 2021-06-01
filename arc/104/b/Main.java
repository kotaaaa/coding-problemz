import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();


//        System.out.println("n1 "+ N+" n2");
//        System.out.println("S1 "+ S +" S2 "+S.length());
        int[] numS = new int[N];

        int cntA = 0; int cntG = 0; int cntC = 0; int cntT = 0;
        int ans = 0;

        for (int i = 0; i < N; i++){
            cntA = 0; cntG = 0; cntC = 0; cntT = 0;

            if (S.charAt(i) == 'A') {
                cntA++;
            } else if (S.charAt(i) == 'T') {
                cntT++;
            } else if (S.charAt(i) == 'C') {
                cntC++;
            } else {
                cntG++;
            }
            for (int j = i+1; j < N; j++){
//                System.out.println(i+" "+j+" "+S.charAt(i)+" "+S.charAt(j));
                if (S.charAt(j) == 'A') {
                    cntA++;
                } else if (S.charAt(j) == 'T') {
                    cntT++;
                } else if (S.charAt(j) == 'C') {
                    cntC++;
                } else {
                    cntG++;
                }


                if ((cntA == cntT) && (cntC == cntG)){
                    ans++;
                }
//                System.out.println(cntA+" "+cntT+" "+cntC+" "+cntG+" "+ans);
            }


        }

        System.out.println(ans);
    }
}