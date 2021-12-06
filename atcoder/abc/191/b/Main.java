import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] az = new int[n];

        int cnt = 0;
        for (int i = 0; i < n; i++){
            az[i] = sc.nextInt();
            if (az[i] != x) {
                System.out.print(az[i]+" ");
                cnt++;
            }
        }
        if (cnt == 0){
            System.out.println();
        }
    }
}