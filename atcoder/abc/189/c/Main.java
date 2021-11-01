import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N];

        int max = 0;
        int tempVal = 0;
        int sectionMin = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
        }

        for (int l = 0; l < N; l++){
            sectionMin = Az[l];
            if (sectionMin > max){
                max = sectionMin;
            }
            for (int r = l+1; r < N; r++){
                if (Az[r] < sectionMin){
                    sectionMin = Az[r];
                }
                tempVal = sectionMin*(r-l+1);
                if (tempVal > max){
                    max = tempVal;
                }
            }
        }

        System.out.println(max);
    }
}