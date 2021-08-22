import java.util.*;
public class Main {
    static List<String> z = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] Az = new int[M];
        for (int i = 0; i < M; i++){
            Az[i] = sc.nextInt();
//            System.out.println("Az "+Az[i]);
        }

        if (M == 0){
            String a = sc.nextLine();
            a = sc.nextLine();
            System.out.println("1");
            System.exit(0);
        }

        Arrays.sort(Az);
        int min = 1000000001;
        int[] diff = new int[M+1];
        for (int i = 0; i < M; i++){
//            System.out.println("Az "+Az[i]);
            if (i == 0){
                diff[0] = Az[0]-1;
            } else {
                diff[i] = Az[i] - Az[i - 1] - 1;
            }

            if ((diff[i] < min) && (diff[i] != 0)){
                min = diff[i];
            }
//            System.out.println("diff "+diff[i]);
        }
        diff[M] = N - Az[M - 1];

        int sum = 0;
        for (int i = 0; i <= M; i++){
            sum += Math.ceil((double) diff[i] / min);
        }
        System.out.println(sum);
    }
}