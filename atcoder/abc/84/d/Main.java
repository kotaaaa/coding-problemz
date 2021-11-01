import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        int[] Lz = new int[Q];
        int[] Rz = new int[Q];

        for (int i = 0; i < Q; i++){
            Lz[i] = sc.nextInt();
            Rz[i] = sc.nextInt();
        }
        int MAX = 100001;
        int[] Az = new int[MAX];
        int[] bitset = new int[MAX];
        Arrays.fill(bitset,1);

        bitset[0] = 0;
        bitset[1] = 0;
//        bitset[2] = 0;
        for (int i = 2; i < MAX; i++){
            if (bitset[i] == 0) continue;
            for (int j = i*2; j < MAX; j+=i){
                bitset[j] = 0;
            }
        }

//        for (int i = 2; i < MAX; i++){
//            System.out.println(i+" "+bitset[i]);
//            if (i == 50) break;
//        }

        for (int i = 2; i < MAX; i++){
            if (bitset[i] == 0) continue;

            if (bitset[(i+1)/2] == 1){
                Az[i] = 1;
            }
        }

//        for (int i = 0; i < MAX; i++){
//            System.out.println(i+" "+Az[i]);
//            if (i == 55) break;
//        }


        int[] sums = new int[MAX];
        sums[0] = 0;
        for (int i = 1; i < MAX; i++){
            sums[i] = sums[i-1] + Az[i];
        }

        for (int i = 0; i < Q; i++){
            System.out.println(sums[Rz[i]] - sums[Lz[i]-1]);
        }


    }
}