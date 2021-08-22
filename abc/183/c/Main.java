import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[][] Tz = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Tz[i][j] = sc.nextInt();
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int n = 0; n < N-1; n++) {
            sb.append(Integer.toString(n + 1));
        }

        permutation(sb.toString(), "");

//        int a = 0; int b = 0;
        int ans = 0;
        int before = 0;
        int tmpSum = 0;
        for (int i = 0; i < z.size(); i++) {
            before = 0;
            tmpSum = 0;
//            System.out.println("z.get(i) "+z.get(i));
            String order = z.get(i);
            for (int j = 0; j < order.length(); j++){
//                System.out.println("before "+before + " order.charAt(j) "+order.charAt(j));
//                System.out.println(Tz[before][order.charAt(j)-48]);
                tmpSum += Tz[before][order.charAt(j)-48];
                before = order.charAt(j)-48;
            }
            tmpSum += Tz[before][0];
//            System.out.println("tmpsum "+tmpSum);
            if (tmpSum == K){
                ans++;
            }
        }
//        System.out.println("ans "+ans);
        System.out.println(ans);
    }


    public static void permutation(String q, String ans) {
        if (q.length() <= 1) {
            z.add(ans + q);
        } else {
            for (int i = 0; i < q.length(); i++) {
                permutation(q.substring(0, i) + q.substring(i + 1), ans + q.charAt(i));
            }
        }
    }
}