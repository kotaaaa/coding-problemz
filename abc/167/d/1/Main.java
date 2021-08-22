import java.util.*;

public class Main {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long K = sc.nextLong();
        int[] Az = new int[N];
        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt() - 1;
        }

        List<Integer> numList = new ArrayList<Integer>();

        int[] doneAz = new int[N];
        doneAz[0] = 1;

//        int roop = 0;
        int rootIdx = 0;
        int roopStart = 0;
        for (int i = 0; i < N; i++){
            if (doneAz[Az[i]] == 0){
                doneAz[Az[i]] = 1;
            } else if (Az[i] == 0) {
                roopStart = 0;
                rootIdx = i;
                break;
            } else {
                roopStart = Az[i];
                rootIdx = i;
                break;
            }
        }

        int next = 0;
        next = rootIdx;
        int cnt = 0;
        while (true) {
            System.out.println("next "+next);
            next = Az[next];
            cnt++;
            if (next == roopStart){
                break;
            }
        }
        System.out.println(cnt);
//        rootIdx = numList.indexOf(roop);
//        System.out.println(numList.size() - rootIdx);
//        System.out.println("aaa> "+numList.size()+" "+rootIdx);

    }
}