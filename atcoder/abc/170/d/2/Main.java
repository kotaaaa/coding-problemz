import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Integer[] Az = new Integer[N];

        int aMax = 0;
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            aMax = Math.max(Az[i], aMax);
        }
        Arrays.sort(Az, Comparator.reverseOrder());

        int ans = 0;
        int before = 0;

        int[] divs = new int[aMax+1];
        int[] dupNums = new int[aMax+1];

//        for (int i = 2; i <= aMax; i++){
        for (int i = 0; i < N; i++){
            dupNums[Az[i]]++;
            for (int j = 0; j < N; j++){
//                dupNums[Az[j]] = 1;
//                System.out.println(" ss " +Az[j]+" "+i);
//                if (Az[j] % i == 0){
                if (Az[i] % Az[j] == 0){
                    divs[Az[i]]++;
//                    divs[i]++;
//                    if (dupNums[Az[j]] == 1){ // 2つ以上同じ数字が存在するとき．
//
//
//                    }

                }
            }
        }
//        if (dupNums)
//        for (int i = 1; i <= aMax; i++){
//            System.out.println(i+" "+divs[i]);
//        }
        for (int i = 0; i < N; i++){
            if ((dupNums[Az[i]] <= 1) && (divs[Az[i]] <= 1 )){
                ans++;
            }
        }

//        System.out.println("ans "+ans);
        System.out.println(ans);


    }
}