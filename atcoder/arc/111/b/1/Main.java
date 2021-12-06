import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N];
        int[] Bz = new int[N];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
        }


        int max = 400001;
        int[] status = new int[max];
        int check = 0;

        for (int i = 0; i < N; i++){
//            System.out.println("status "+ status[Az[i]]+" "+status[Bz[i]]);
            //オモテウラ同じとき
            if (Az[i] == Bz[i]){
                status[Az[i]] = 1;
                continue;
            }
            // 同じでなく，どっちも初めて 0 0
//            if ((status[Az[i]] == 0) && (status[Bz[i]] == 0)){
//                status[Az[i]] = -1;
//                status[Bz[i]] = -1;
//                continue;
//            }
            // どっちかは確定状態 -1 1 or -1 1
            if ((status[Az[i]] == 1) || (status[Bz[i]] == 1)) {
                if (status[Az[i]] == 1) {
                    status[Bz[i]] = 1;
                }
                if (status[Bz[i]] == 1) {
                    status[Az[i]] = 1;
                }
                continue;
            }
            // どちらも-1状態
            if ((status[Az[i]] == -1) && (status[Bz[i]] == -1)){
                status[Az[1]] = 1;
                status[Bz[1]] = 1;
                continue;
            }

            // どちらとも初めて，もしくは，片方のみ-1状態
            if (((status[Az[i]] == 0) && (status[Bz[i]] == -1)) || ((status[Az[i]] == -1) && (status[Bz[i]] == 0)) || ((status[Az[i]] == 0) && (status[Bz[i]] == 0))){
                status[Az[i]] = -1;
                status[Bz[i]] = -1;
                continue;
            }

//            System.out.println("sss "+ Az[i]+" "+Bz[i]);
            check++;
        }


//        System.out.println("check "+check);

        for (int i = 0; i < N; i++){
            if (status[Az[i]] == 1) {
                status[Bz[i]] = 1;
            }
            if (status[Bz[i]] == 1) {
                status[Az[i]] = 1;
            }
        }

        int count = 0;
        int countMinus1 = 0;
        for (int i = 1; i < max; i++){
            if (status[i] == 1){
                count++;
            }
            if (status[i] == -1){
                countMinus1++;
            }
        }

        System.out.println(count + (int) Math.ceil((double)countMinus1 / 2));


    }
}