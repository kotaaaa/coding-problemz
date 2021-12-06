import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Lz = new int[N];
        for (int i = 0; i < N; i++){
            Lz[i] = sc.nextInt();
        }

        HashSet<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < N; i++){
            set.add(Lz[i]);
        }
        int cnt = 0;
        for (int i = 0; i < 2<<N; i++){
            HashSet<Integer> eachSet = new HashSet<Integer>();
            for (int j = 0; j < set.size(); j++){
                if ((i>>j&1)==1){
                    eachSet.add(j);
                }
            }
            if (eachSet.size() == 3){

                int[] ele = new int[3];
                int idx = 0;
                for (int e: eachSet) {
                    System.out.print(" "+ e);
                    ele[idx] = e;
                    idx++;
                }
                System.out.println();
                if (check(ele[0], ele[1], ele[2])){
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }

    public static boolean checktri(int a, int b, int c){
        if (!check(a, b, c)) return false;
        if (!check(c, b, a)) return false;
        if (!check(a, c, b)) return false;
        return true;
    }
    public static boolean check(int a, int b, int c){
        return (a + b > c);
    }

}