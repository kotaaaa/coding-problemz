import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        long[] Az = new long[N+1];
        long[] reverseAz = new long[N+1];
        for (int i = 1; i <= N; i++){
            Az[i] = sc.nextLong();
        }

        Arrays.sort(Az);
        for (int i = 1; i <= N; i++){
            reverseAz[i] = Az[N+1-i];
        }
//        for (int i = 1; i <= N; i++){
//            System.out.println("r "+reverseAz[i]);
//        }


        long[] Scul = new long[N+1];
        long[] sum = new long[N+1];

        long allSum = 0;

        Scul[N] = reverseAz[N];
        for (int i = N-1; i > 1; i--){
            Scul[i] = Scul[i+1]+reverseAz[i];
        }
//        for (int i = 1; i <= N; i++){
//            System.out.println("Scul["+i+"] "+Scul[i]);
//        }

        for (int i = 1; i < N; i++){

            allSum += (long)(N-i)*reverseAz[i] - Scul[i+1];
//            System.out.println("allSum "+allSum);
        }
        System.out.println(allSum);
    }
}