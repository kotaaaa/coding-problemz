import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();
        int[] Az = new int[N];
        int[] Bz = new int[N];
        int[] Cz = new int[N];

        int Bmax = 0;
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
            Cz[i] = sc.nextInt();
        }
        TreeMap<Integer, Long> sum = new TreeMap<Integer, Long>();
        TreeMap<Integer, Long> delta = new TreeMap<Integer, Long>();

        for (int i = 0; i < N; i++){
            if (!delta.keySet().contains(Az[i])){
                delta.put(Az[i], (long) Cz[i]);
            } else {
                delta.put(Az[i],delta.get(Az[i]) + Cz[i]);
            }
            if (!delta.keySet().contains(Bz[i]+1)){
                delta.put(Bz[i]+1, (long) -Cz[i]);
            } else {
                delta.put(Bz[i]+1,delta.get(Bz[i]+1) - Cz[i]);
            }
        }

        long beforeVal = 0;
        for (int idx: delta.keySet()){
            sum.put(idx, beforeVal + delta.get(idx));
            beforeVal = sum.get(idx);
        }
        long ans = 0;
        int start = 0;
        long startVal = 0;
        for (int idx: sum.keySet()){
            if (start == 0){
                start = idx;
                startVal = sum.get(idx);
                continue;
            }
            if (startVal <= C){
                ans += (long)(idx-start)*startVal;
            } else {
                ans += (long)(idx-start)*C;
            }
            start = idx;
            startVal = sum.get(idx);
        }
        System.out.println(ans);
    }
}