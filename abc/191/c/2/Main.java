import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] az = new int[m + 1];
        int[] bz = new int[m + 1];
        for (int i = 1; i <= m; i++) {
            az[i] = sc.nextInt();
            bz[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        int[] cz = new int[k + 1];
        int[] dz = new int[k + 1];
        for (int i = 1; i <= k; i++) {
            cz[i] = sc.nextInt();
            dz[i] = sc.nextInt();
        }
        int cnt = 0;
        int maxCnt = 0;
        for (int i = 0; i < (1<<k); i++){
            HashSet<Integer> dishSet = new HashSet<Integer>();
            HashSet<Integer> set = new HashSet<Integer>();
            for (int j = 0; j < k; j++){
                if ((1&i>>j)==1){
                    set.add(j+1);
                }
            }
//            System.out.println(set);
            for (int j = 1; j <= k; j++){
                if (set.contains(j)) {
                    dishSet.add(cz[j]);
                } else {
                    dishSet.add(dz[j]);
                }
            }
            cnt = 0;
            for (int j = 1; j <= m; j++){
                if ((dishSet.contains(az[j])) && (dishSet.contains(bz[j]))) {
                    cnt++;
                }
            }
            maxCnt = Math.max(cnt, maxCnt);
        }
        System.out.println(maxCnt);

    }
}