import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.nextLine();
        S = sc.nextLine();
        Deque<String> deque = new ArrayDeque<String>();

        char removeChar = ' ';
        for (int i = 0; i < N; i++){
            char now = S.charAt(i);
            if (i < 2){
                deque.push(String.valueOf(now));
                continue;
            }
            if (now == 'x'){ // x のとき
                if (deque.peek().toCharArray()[0] == 'o'){ // x,oときたとき
                    removeChar = deque.poll().toCharArray()[0]; // remove 'o'
                    if (deque.peek().toCharArray()[0] == 'f'){ // x,o,fときたとき
                        removeChar = deque.poll().toCharArray()[0]; // remove 'f'
                    } else {
                        deque.push(String.valueOf('o')); // 'o'を戻す
                        deque.push(String.valueOf('x')); // 'x'も追加する
                    }
                } else { // x だけのとき
                    deque.push(String.valueOf('x')); // 'x'を追加する
                }
            } else { // x 以外のとき
                deque.push(String.valueOf(now)); // x 以外
            }
        }
        System.out.println(deque.size());

    }
}