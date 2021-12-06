import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N+1];
        int[] Bz = new int[N+1];
        int[] Cz = new int[N+1];

        int[] sum = new int[N+1];
        int minVal = 0;

        for (int i = 0; i < N; i++){
            Az[i+1] = sc.nextInt();
            Bz[i+1] = sc.nextInt();
            Cz[i+1] = sc.nextInt();
        }

        sum[1] = 0;
        sum[2] = getMax(Az[2], Bz[2], Cz[2]);

        for (int i = 2; i <= N; i++){

            if ()

            int candi1 = 0; int candi2 = 0;
            candi1 = sum[i - 1] + Math.max(Az[i], Bz[i]);
            candi2 = sum[i - 2] + Math.max(Az[i - 1], Bz[i - 1]) + Cz[i];
            sum[i] = Math.max(candi1, candi2);
        }

        for (int i = 1; i <= N; i++){
            System.out.println("rrr "+i+" "+sum[i]);
        }
        System.out.println(sum[N]);

    }

    public int getMax(int a, int b, int c){
        int max = 0; int maxInd = -1;
        if (a > max){
            max = a;
            maxInd = 0;
        }
        if (b > max){
            max = b;
            maxInd = 1;
        }
        if (c > max){
            max = c;
            maxInd = 2;
        }
        return max;
    }

    public int getMaxId(int a, int b, int c){
        int max = 0; int maxInd = -1;
        if (a > max){
            max = a;
            maxInd = 0;
        }
        if (b > max){
            max = b;
            maxInd = 1;
        }
        if (c > max){
            max = c;
            maxInd = 2;
        }
        return maxInd;
    }


}