import java.util.*;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        long[] Az = new long[N];
        long[] Bz = new long[N];
        Long[] cities = new Long[N];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
        }

        long sum = 0;
        for (int i = 0; i < N; i++){
            cities[i] = 2*Az[i] + Bz[i];
            sum -= Az[i];
        }

        Arrays.sort(cities, Comparator.reverseOrder());
        for (int i = 0; i < N; i++){
            sum += cities[i];
            if (sum > 0) {
                System.out.println(i+1);
                System.exit(0);
            }
        }
    }
}