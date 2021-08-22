import java.util.*;

public class Main {

//    static int n = 5;
    static int[] S = {1,2,3,4,5,7,8,9,10,11,12};
//    static int q = 3;
    static int[] T = {3,4,1,15,0,6,7,8};//,12,13,15};

    public static void main (String[] args){
        int ans = 0;
        for (int i = 0; i < T.length; i++){
            int a = binarySearch(T[i]);
            ans += a;
            System.out.println("T[i]: "+T[i]+" a: "+a);
        }
        System.out.println("ans: "+ans);

        System.out.println(Math.max(1,3));
        System.out.println(Math.max(4,3));
    }

    public static int binarySearch(int num){
        int left = 0; int right = S.length-1;
        int mid = 0;
        while (left < right){
            System.out.println(num+" "+mid+" "+left+" "+right);
            mid = (left + right) / 2;
            if (S[mid] == num){
                return 1;
            } else if (S[mid] < num) {
                left = mid + 1;
            } else if (S[mid] > num) {
                right = mid;
            }
        }
        return 0;
    }
}