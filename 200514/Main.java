import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] Ss = new int[M];
        int[] Cs = new int[M];
        for (int m = 0; m < M; m++){
            Ss[m] = sc.nextInt();
            Cs[m] = sc.nextInt();
        }
        System.out.println("\n\n");
        for (int m = 0; m < M; m++){
            System.out.println(Ss[m]+" "+Cs[m]);
        }
        char[] text = new char[N];
        for (int m = 0; m < M; m++){
            System.out.println(Cs[m]+ "");
            text[m] = 'a';//(Cs[m]+ "");
        }
        System.out.println("\n\n");
        for (int m = 0; m < M; m++){
            System.out.println(Ss[m]+" "+Cs[m]);
        }
    }
}
