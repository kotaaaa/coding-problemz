import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int R = sc.nextInt();
        int S = sc.nextInt();
        int P = sc.nextInt();
        String T = sc.nextLine();
        T = sc.nextLine();

        int[] Rz = new int[N];
        int[] Sz = new int[N];
        int[] Pz = new int[N];

        if (T.charAt(0) == 'r'){
            Pz[0] = P;
        }
        if (T.charAt(0) == 's'){
            Rz[0] = R;
        }
        if (T.charAt(0) == 'p'){
            Sz[0] = S;
        }

        int ans = 0;

        int start = 0;
        for (int i = 0; i < K; i++){
            start = i;
            if (T.charAt(start) == 'r'){
                Pz[start] = P;
            }
            if (T.charAt(start) == 's'){
                Rz[start] = R;
            }
            if (T.charAt(start) == 'p'){
                Sz[start] = S;
            }
            int j = 0;
            int num = start+j*K;
//            int num = 0;
            while (start + (j+1)*K < N){

                num = start+j*K;
//                System.out.println("i j "+i+" "+j+" "+(start + (j+1)*K));
                if (T.charAt(num+K) == 'r'){
                    Pz[num+K] = Math.max(Rz[num], Sz[num]) + P;
                    Rz[num+K] = Math.max(Sz[num], Pz[num]);
                    Sz[num+K] = Math.max(Pz[num], Rz[num]);
                } else if (T.charAt(num+K) == 's'){
                    Pz[num+K] = Math.max(Rz[num], Sz[num]);
                    Rz[num+K] = Math.max(Sz[num], Pz[num]) + R;
                    Sz[num+K] = Math.max(Pz[num], Rz[num]);
                } else if (T.charAt(num+K) == 'p'){
                    Pz[num+K] = Math.max(Rz[num], Sz[num]);
                    Rz[num+K] = Math.max(Sz[num], Pz[num]);
                    Sz[num+K] = Math.max(Pz[num], Rz[num]) + S;
                }
                j++;
            }
//            System.out.println((start + (j+1)*K)+" "+(num+K)+" "+getMax(Pz[num+K], Rz[num+K], Sz[num+K]));
            if (j == 0){
//                System.out.println("a "+(start + (j+1)*K)+" "+(num+K)+" "+getMax(Pz[num], Rz[num], Sz[num])+" sss "+Pz[num]+" "+Rz[num]+" "+Sz[num]);
                ans += getMax(Pz[num], Rz[num], Sz[num]);
            } else {
//                System.out.println("b "+(start + (j+1)*K)+" "+(num+K)+" "+getMax(Pz[num+K], Rz[num+K], Sz[num+K]));
                ans += getMax(Pz[num+K], Rz[num+K], Sz[num+K]);
            }

        }

//        for (int i = 0; i < N; i++){
//            System.out.println(Rz[i]+" "+Sz[i]+" "+Pz[i]);
//        }

        System.out.println(ans);

    }

    public static int getMax(int a, int b, int c){
        int max = 0;
        if (a > b){
            max = a;
        } else {
            max = b;
        }
        if (c > max){
            max = c;
        }
        return max;
    }
}