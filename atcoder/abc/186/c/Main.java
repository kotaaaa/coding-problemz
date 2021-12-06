import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int cnt = 0;
        for (int i = 1; i <= N; i++){
//            System.out.println(i+" "+Integer.toOctalString(i)+" "+Integer.toOctalString(i).contains("7"));
            if (String.valueOf(i).contains("7")) {
                continue;
            }
            if (Integer.toOctalString(i).contains("7")){
                continue;
            }
            cnt++;
        }

        System.out.println(cnt);
    }

}