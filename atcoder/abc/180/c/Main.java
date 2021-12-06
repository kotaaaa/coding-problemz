import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long ans = 0;

        List<Long> nums = new ArrayList<>();
        for (int i = 1; i < Math.sqrt(N); i++) {
            if (N % i == 0) {
                nums.add(N / i);
                System.out.println(i);
            }
        }

        if (N % Math.sqrt(N) == 0) {
//            nums.add(N / i);
            System.out.println((long) Math.sqrt(N));
        }

//        System.out.println("q "+nums.size());

        for (int i = nums.size() - 1; i >= 0; i--) {
            System.out.println(nums.get(i));
        }
    }
}