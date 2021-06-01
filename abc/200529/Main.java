import java.util.*;


public class Main {
    static int count = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.println(a);
        int underDigitCount = under1Digit(a);
        count += underDigitCount;
//        System.out.println(underDigitCount);
        f(a,0);
        System.out.println(count);
    }

    public static int under1Digit(int num){
        int targetDigit = 0;
        while(num!=0){
            num /= 10;
            targetDigit++;
        }
        targetDigit--;
        if (targetDigit <= 2) {
            return 0;
        }
        int[] deno = new int[3];
        Arrays.fill(deno, targetDigit / 3);
        int rest3 = targetDigit % 3;
        int diffNum = 1;
        if (rest3 == 0) diffNum = 1;
        else diffNum = 3;
        for (int r = 0; r < rest3; r++){
            deno[r]++;
        }
        return diffNum * factrial(targetDigit) / (factrial(deno[0])*factrial(deno[1])*factrial(deno[2]));
    }

    public static int factrial (int n){
        if (n <= 1) return 1;
        return n * factrial(n - 1);
    }
    public static int digit (int n){
        int digitNum = 0;
        while(n!=0){
            n /= 10;
            digitNum++;
        }
        return digitNum;
    }

    public static void f (int num, int K){
        System.out.println("num, K "+num+" "+K);
        int[] digitNums = new int[digit(num)];
        int targetNum = num;
        System.out.println("digit(num)"+digit(num));
        for (int n = digit(num)-1; n >= 0; n--){
            digitNums[n] = targetNum%10; targetNum/=10;
        }
//        for (int n = 0; n < digit(num); n++){
//            System.out.println(digitNums[n]);
//        }
        int[] nums357 = new int[10];
        for (int k = 0; k < K; k++){
            nums357[digitNums[k]]++;
        }
        if (digit(num) == K){
            if ((nums357[3] >= 1) && (nums357[5] >= 1) && (nums357[7] >= 1)){
                count++;
            }
            return ;
        }
        System.out.println("digitNums[K]:"+digitNums[K]);
        for (int i = 1; i <= digitNums[K]; i++) {
//            System.out.println("i"+i);
            if ((i != 3) && (i != 5) && (i != 7)) {
                continue;
            }
            nums357[i]++;
//            System.out.println("i"+i);
            if ((nums357[3] >= 1) && (nums357[5] >= 1) && (nums357[7] >= 1)){
                count += factrial(digit(num)- K - 1);
                return ;
            }
            System.out.println(nums357[3]+" "+nums357[5]+" "+nums357[7]);
            f (num, K+1);
//            System.out.println("i"+i);
        }

    }
}