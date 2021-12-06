import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        long[] Az = new long[N+1];
        for (int i = 1; i <= N; i++){
            Az[i] = sc.nextLong();
        }

        Arrays.sort(Az);
        long[] Scul = new long[N+1];
        long[] sum = new long[N+1];

//        Scul[1] = Az[1];
        long allSum = 0;
//        for (int i = 2; i <= N; i++){
////            sum[i] = (i-1)*Az[i] - Scul[i-1];
////            allSum += sum[i];
//            allSum += (i-1)*Az[i] - Scul[i-1];
//            Scul[i] = Scul[i-1]+Az[i];
//
//        }

        for (int i = 1; i <= N; i++){
//            sum[i] = (i-1)*Az[i] - Scul[i-1];
//            allSum += sum[i];
//            allSum += (i-1)*Az[i] - Scul[i-1];
            Scul[i] = Scul[i-1]+Az[i];
        }

        for (int i = 1; i <= N; i++){
            sum[i] = (i-1)*Az[i] - Scul[i-1];
            allSum += sum[i];
        }



        System.out.println(allSum);
    }
}