import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        StringBuilder sb = new StringBuilder();
        sb.append(S);
        int N = sc.nextInt();
        int[] Qz = new int[N];
        int[] change = new int[N];
        char[] chars = new char[N];
        for (int i = 0; i < N; i++){
            Qz[i] = sc.nextInt();
            if (Qz[i] == 2){
                change[i] = sc.nextInt();
                chars[i] = sc.next().charAt(0);
            }
        }

        int direction = 0; // % 2 == 1 or 0

        for (int i = 0; i < N; i++){
            if (Qz[i] == 1){ // 前後逆転のとき
                direction++;
            } else {
                if ((direction % 2 == 0) && (change[i] == 1)){ // 正順で前から
                    sb.insert(0,String.valueOf(chars[i]));
                } else if ((direction % 2 == 0) && (change[i] == 2)){ // 正順で後ろから
                    sb.append(String.valueOf(chars[i]));
                } else if ((direction % 2 == 1) && (change[i] == 1)){ // 逆順で前から
                    sb.append(String.valueOf(chars[i]));
                } else if ((direction % 2 == 1) && (change[i] == 2)){ // 逆順で後ろから
                    sb.insert(0,String.valueOf(chars[i]));
                }
            }
        }

        if (direction % 2 == 0){ // 正順なら普通に出力する
            System.out.println(sb);
            System.exit(0);
        }
        System.out.println(sb.reverse());
    }
}