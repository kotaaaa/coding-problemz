import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
import java.math.BigInteger;

class Result {

    /*
     * Complete the 'pythagoreanTriple' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER a as parameter.
     */

    public static List<BigInteger> pythagoreanTriple(int a) {
        // Write your code here
        List<BigInteger> ans = new ArrayList<BigInteger>();
        BigInteger bigA = BigInteger.valueOf(a);
        if (a % 2 == 1) {
            BigInteger k = bigA.multiply(bigA).subtract(BigInteger.valueOf(1)).divide(BigInteger.valueOf(2));
            ans.add(bigA);
            ans.add(k.add(BigInteger.valueOf(1)));
            ans.add(k);
        } else {
            ans.add(BigInteger.valueOf(a));
            BigInteger m = BigInteger.valueOf(a).divide(BigInteger.valueOf(2));

            ans.add(m.multiply(m).subtract(BigInteger.valueOf(1)));
            ans.add(m.multiply(m).add(BigInteger.valueOf(1)));

        }
        return ans;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int a = Integer.parseInt(bufferedReader.readLine().trim());

        List<BigInteger> triple = Result.pythagoreanTriple(a);

        bufferedWriter.write(
                triple.stream()
                        .map(Object::toString)
                        .collect(joining(" "))
                        + "\n");

        bufferedReader.close();
        bufferedWriter.close();
    }
}
