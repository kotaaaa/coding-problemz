import java.util.*;


public class permu {
    static List<String> z;

    public static void permutation(String q, String ans) {
        if (q.length() <= 1) {
            z.add(ans + q);
        } else {
            for (int i = 0; i < q.length(); i++) {
                permutation(q.substring(0, i) + q.substring(i + 1), ans + q.charAt(i));
            }
        }
    }

    public static void main(String[] args) {
        z = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        StringBuilder sb = new StringBuilder();

        for (int n = 0; n < N; n++) {
            sb.append(Integer.toString(n + 1));
        }

        permutation(sb.toString(), "");

        int a = 0; int b = 0;
        for (int i = 0; i < z.size(); i++) {
            System.out.println(z.get(i));
        }
    }
}