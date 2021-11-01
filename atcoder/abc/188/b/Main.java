import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int l = (int) Math.pow(2,N);
        int[] Az = new int[l];

        int[] first = new int[l/2];
        int[] second = new int[l/2];

        for (int i = 0; i < l; i++){
            Az[i] = sc.nextInt();

            if (i < l/2){
                first[i] = Az[i];
            } else {
                second[i - l/2] = Az[i];
            }
        }

        int max = 0;
        int maxIdx = -1;
        for (int i = 0; i < l; i++){
            if (Az[i] > max) {
                max = Az[i];
                maxIdx = i;
            }
        }

        int maxFirst = 0;
        int maxIdxFirst = 0;
        for (int i = 0; i < l/2; i++){
            if (first[i] > maxFirst) {
                maxFirst = first[i];
                maxIdxFirst = i;
            }
        }

        int maxSecond = 0;
        int maxIdxSecond = 0;
        for (int i = 0; i < l/2; i++){
            if (second[i] > maxSecond) {
                maxSecond = second[i];
                maxIdxSecond = i;
            }
        }

//        System.out.println("1 "+maxFirst);
//        System.out.println("2 "+maxSecond);
//
//        System.out.println("maxIdx "+maxIdx);
//        System.out.println("max "+max);

        if (maxIdx < l/2){
            System.out.println(maxIdxSecond+1+l/2);
        } else {
            System.out.println(maxIdxFirst+1);
        }

//        System.out.println(Math.pow(10,9) > Integer.MAX_VALUE);
    }
}