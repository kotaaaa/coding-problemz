import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Integer[] Az = new Integer[N];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
        }
        Arrays.sort(Az, Comparator.reverseOrder());

        int ans = 0;
        int before = 0;
        for (int i = 0; i < N; i++){
            if (before == Az[i]){
                continue;
            }
            before = Az[i];
            int canDivide = 1;
            for (int j = i+1; j < N; j++){
                if (Az[i]%Az[j] == 0){
                    canDivide = 0;
                    break;
                }
            }
            ans += canDivide;
        }
        System.out.println(ans);

    }
}