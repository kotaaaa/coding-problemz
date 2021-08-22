import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] Az = new int[N];

        int maxNum = 0;
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            if (maxNum < Az[i]){
                maxNum = Az[i];
            }
        }

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < N; i++){
            if (!map.keySet().contains(Az[i])){
                map.put(Az[i],1);
            } else {
                map.put(Az[i],map.get(Az[i]) + 1);
            }
        }

//        for (int i: map.keySet()){
//            System.out.println(i+ " " + map.get(i));
//        }

        int restCnt = K;
        int ans = 0;
        int diff = 0;
        int untilLast = 1;

//        System.out.println("maxNum "+ maxNum);
        for (int i = 0; i <= maxNum; i++){

            if (!map.keySet().contains(i)){
//                System.out.println("no ketSet ans "+ans+" restCnt "+restCnt+" i "+i);
//                restCnt -= K;
                ans += restCnt*i;
                restCnt = 0;

            } else {
//                System.out.println("rest i "+ i+" ans "+ans+" restCnt "+restCnt+" map.get(i) "+map.get(i));
                if (map.get(i) >= restCnt){
                    continue;
                } else {
                    diff = restCnt - map.get(i);
                    restCnt -= diff;
                    ans += diff*i;
//                    System.out.println("ans "+ans+" restCnt "+restCnt);
                }
            }
            if (restCnt == 0){
//                untilLast = 0;
                break;
            }
//            System.out.println("i "+ i+" ans "+ans);
        }

//        if (restCnt > 0){
        ans += (maxNum+1)*restCnt;
//        }

        System.out.println(ans);
    }
}
