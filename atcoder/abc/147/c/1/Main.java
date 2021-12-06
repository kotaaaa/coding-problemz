import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N];
        int[][] Xz = new int[N][N];
        int[][] Yz = new int[N][N];
        for (int i = 0; i < N; i++) {
            Az[i] = sc.nextInt();
            for (int j = 0; j < Az[i]; j++) {
                Xz[i][j] = sc.nextInt()-1;
                Yz[i][j] = sc.nextInt();
            }
        }
        int maxHonestCnt = 0;
        for (int i = 0; i < (1<<N); i++){
            HashSet<Integer> set = new HashSet<Integer>();
            for (int j = 0; j < N; j++){
                if ((1&i>>j)==1){
                    set.add(j);
                }
            }
            System.out.println(set);
            int[] predz = new int[N];
            Arrays.fill(predz, -1);

            int break_flg = 0;
            int honestCnt = 0;
            for (int k: set){
                for (int h = 0; h < Az[k]; h++) {
                    if (predz[Xz[k][h]] == -1){
                        predz[Xz[k][h]] = Yz[k][h];
                    } else if (predz[Xz[k][h]] != Yz[k][h]) {
                        break_flg = 1;
                        break;
                    }
                }
//                System.out.println("k "+k);
                if (break_flg == 1){
                    break;
                }
                honestCnt++;
                System.out.println(honestCnt);
            }

            if (honestCnt > maxHonestCnt){
                maxHonestCnt = honestCnt;
            }
        }
        System.out.println(maxHonestCnt);
    }
}