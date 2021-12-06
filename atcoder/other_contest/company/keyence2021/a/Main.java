import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long[] Az = new long[N];
        long[] Bz = new long[N];
        long[] Cz = new long[N];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextLong();
        }
        for (int i = 0; i < N; i++){
            Bz[i] = sc.nextLong();
        }
        long currentAzMax = 0;
        long currentMax = 0;
        long tmp = 0;
        currentAzMax = Az[0];
        Cz[0] = Az[0]*Bz[0];
        currentMax = Cz[0];
        for (int i = 1; i < N; i++){
            if (currentAzMax < Az[i]){
                currentAzMax = Az[i];
            }
            tmp = currentAzMax * Bz[i];
            if (currentMax < tmp){
                currentMax = tmp;
            }
            Cz[i] = currentMax;
        }
        for (int i = 0; i < N; i++){
            System.out.println(Cz[i]);
        }
    }
}
