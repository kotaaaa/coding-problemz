import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N];

        int maxA = 0;
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            if (Az[i] > maxA){
                maxA = Az[i];
            }
        }

        int cnt = 0;
        int maxCnt = 0;
        int maxi = 0;
        for (int i = 2; i <= maxA; i++){
            cnt = 0;
            for (int j = 0; j < N; j++){
                if (Az[j] % i == 0){
                    cnt++;
                }
            }

            if (maxCnt < cnt){
                maxCnt = cnt;
                maxi = i;
            }
        }
        System.out.println(maxi);
    }
}