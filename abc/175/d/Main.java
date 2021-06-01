import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String Cz = sc.next();

        int firstR = -1;
        int cntW = 0;
        int cntR = 0;
        char thisChar = ' ';
        for (int i = 0; i < N; i ++){
            thisChar = Cz.charAt(i);
            if (thisChar == 'R'){
                cntR++;
            }
    }
}