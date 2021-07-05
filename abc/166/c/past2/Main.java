import java.util.*;

public class Main {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] Hz = new int[N];
        for (int i = 0; i < N; i++){
            Hz[i] = sc.nextInt();
        }
        int[] Az = new int[M];
        int[] Bz = new int[M];
        for (int i = 0; i < M; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
        }

//        int[][] matrix = new int[N][N];
        Map<Integer, Map<Integer,Integer>> matrix = new HashMap<Integer, Map<Integer, Integer>>();

        for (int i = 0; i < M; i++){

            int x = 0; int y = 0;
            if (Az[i] < Bz[i]){
                x = Bz[i];
                y = Az[i];
            } else {
                x = Az[i];
                y = Bz[i];
            }

            if (Hz[x-1] == Hz[y-1]){
//                matrix[Az[i]-1][Bz[i]-1] = -1;
//                matrix[Bz[i]-1][Az[i]-1] = -1;
                matrix.put(x-1, new HashMap<Integer, Integer>());
                matrix.get(x-1).put(y-1,-1);
            } else {
//                matrix[Az[i]-1][Bz[i]-1] =   Hz[Az[i]-1] - Hz[Bz[i]-1];
//                matrix[Bz[i]-1][Az[i]-1] = - (Hz[Az[i]-1] - Hz[Bz[i]-1]);
                matrix.put(x-1, new HashMap<Integer, Integer>());
                matrix.get(x-1).put(y-1,  Hz[x-1] - Hz[y-1]);
                matrix.put(y-1, new HashMap<Integer, Integer>());
                matrix.get(y-1).put(x-1,- (Hz[x-1] - Hz[y-1]));

            }
        }
        System.out.println("aa"+matrix.keySet());
        int ans = 0;
        int minus_flg = 0;
        for (int i = 0; i < N; i++){
            System.out.println(i+" "+matrix.get(i));
            if (!matrix.keySet().contains(i)){
                continue;
            }
//            for (int j = 0; j < N; j++){
            for (int j: matrix.get(i).keySet()){
//                System.out.println(matrix.get(i));
                if (matrix.get(i).get(j) < 0){
                    minus_flg = 1;
                    break;
                }
            }
            if (minus_flg != 1){
                ans++;
            }
            minus_flg = 0;
        }
        System.out.println(ans);
    }
}