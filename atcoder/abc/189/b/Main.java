import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long X = sc.nextInt();
        int[] Vz = new int[N];
        int[] Pz = new int[N];

        double sum = 0;
        for (int i = 0; i < N; i++){
            Vz[i] = sc.nextInt();
            Pz[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++){
            sum += (double) Vz[i] * Pz[i] / 100;
//            System.out.println("i "+i+" sum "+sum+" X " + X +" "+((double) Vz[i]* ( (double) Pz[i]/ 100)));
            if (X < sum){
                System.out.println(i+1);
                System.exit(0);
            }
        }
        System.out.println(-1);
    }
}