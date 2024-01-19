
// import java.io.*;
import java.util.*;

// User function Template for Java
class Solution {
    boolean checkTriplet(int[] arr, int n) {

        // int maxVal = 0;
        // Arrays.stream(arr).forEach(
        // i -> maxVal = Math.max(i, maxVal)
        // );
        int maxVal = Arrays.stream(arr).max().orElse(0);

        boolean array[] = new boolean[maxVal + 1];
        Arrays.fill(array, false);

        Arrays.stream(arr).forEach(
                i -> array[i] = true);
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {

                if (array[i] != true || array[j] != true) {
                    continue;
                }
                int k = (int) Math.sqrt(i * i + j * j);
                if (i * i + j * j != k * k || k > maxVal) {
                    continue;
                }
                if (array[k] != true) {
                    continue;
                }

                return true;
            }
        }
        return false;
    }
}
