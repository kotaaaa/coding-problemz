import java.util.*;

// https://atcoder.jp/contests/atc001/tasks/dfs_a
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        String[] rows = new String[H];
        char[][] mass = new char[W][H];
        int[][] reached = new int[W][H];

        for (int i = 0; i < H; i++) {
            rows[i] = sc.next();
        }
        int[] start = {0, 0};
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                mass[j][i] = rows[i].charAt(j);
                if (rows[i].charAt(j) == 's'){
                    start[0] = j; start[1] = i;
                }
            }
        }
        Deque<int[]> stack = new ArrayDeque<int[]>();
        stack.push(start);

        int[] each = {0, 0};
        int[] forpush = {0, 0};
        int goal = 0;


//        while(true) {
        while(stack.size() > 0) {
            each = stack.pop();
            reached[each[0]][each[1]] = 1;
            if (each[0] + 1 < W){
                if (reached[each[0] + 1][each[1]] == 0) { // right
                    if (mass[each[0] + 1][each[1]] == '.') {
                        forpush[0] = each[0] + 1;
                        forpush[1] = each[1];
                        stack.push(forpush);
                        continue;
                    }

                    if (mass[each[0] + 1][each[1]] == 'g'){
                        goal = 1;
                        break;
                    }
                }
            }

            if (each[1] - 1 >= 0){
                if (reached[each[0]][each[1] - 1] == 0) { // up
                    if (mass[each[0]][each[1] - 1] == '.') {
                        forpush[0] = each[0];
                        forpush[1] = each[1] - 1;
                        stack.push(forpush);
                        continue;
                    }
                    if (mass[each[0]][each[1] - 1] == 'g'){
                        goal = 1;
                        break;
                    }
                }
            }

            if (each[0] - 1 >= 0){
                if (reached[each[0] - 1][each[1]] == 0) { // left
                    if (mass[each[0] - 1][each[1]] == '.') {
                        forpush[0] = each[0] - 1;
                        forpush[1] = each[1];
                        stack.push(forpush);
                        continue;
                    }
                    if (mass[each[0]][each[1] - 1] == 'g'){
                        goal = 1;
                        break;
                    }
                }
            }
            if (each[1] + 1 < H) {
                if (reached[each[0]][each[1] + 1] == 0) { // down
                    if (mass[each[0]][each[1] + 1] == '.') {
                        forpush[0] = each[0];
                        forpush[1] = each[1] + 1;
                        stack.push(forpush);
                        continue;
                    }
                    if (mass[each[0]][each[1] + 1] == 'g'){
                        goal = 1;
                        break;
                    }
                }
            }
//            System.out.println("size "+ stack.size());

        }
        if (goal == 1){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
}
