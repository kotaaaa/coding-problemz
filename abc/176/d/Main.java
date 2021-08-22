import java.util.*;
public class Main {
    static int H = 0;
    static int W = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        H = sc.nextInt();
        W = sc.nextInt();
        int[] Cz = new int[2];
        int[] Dz = new int[2];
        char[][] Sz = new char[H][W];
        int[][] checked = new int[H][W];
        for (int[] c: checked){
            Arrays.fill(c, -1);
        }
        int[][] rot = {{0,1}, {-1,0}, {0, -1}, {1,0}};
        int[][] rotMahou = {{0,2}, {-1,2}, {-2,2},{-2,1},{-2,0},{-2,-1},{-2,-2},{-1,-2},{0,-2},{1,-2},{2,-2},{2,-1},{2,0},{2,1},{2,2},{1,2},{-1,1},{-1,-1},{1,-1},{1,1}};

        String[] texts = new String[H];
        for (int i = 0; i < 2; i++) {
            Cz[i] = sc.nextInt() - 1;
        }
        for (int i = 0; i < 2; i++) {
            Dz[i] = sc.nextInt() - 1;
        }

        sc.nextLine();
        String S = "";
        for (int i = 0; i < H; i++) {
            S = sc.nextLine();
            for (int j = 0; j < W; j++) {
                Sz[i][j] = S.charAt(j);
            }
        }

        Deque<int[]> deque = new ArrayDeque<int[]>();
        deque.addFirst(Cz);
        checked[Cz[0]][Cz[1]] = 0;
        int mahou = 0;
        while (deque.size() > 0) {
            int[] vals = deque.pollFirst();

            if (checked[vals[0]][vals[1]] == -1){
                ;
            } else {
                mahou = checked[vals[0]][vals[1]];
            }

            int nextX = 0; int nextY = 0;
            int diffX = 0; int diffY = 0;
            for (int[] r: rot) {
                diffX = r[0];
                diffY = r[1];

                nextX = vals[0] + diffX;
                nextY = vals[1] + diffY;

                if ((massCheck(nextX, nextY)) && ('.' == Sz[nextX][nextY])) {
                    if ((checked[nextX][nextY] == -1) || (checked[nextX][nextY] > mahou)){
                        checked[nextX][nextY] = mahou;
                        int[] next = {nextX, nextY};
                        deque.addFirst(next);
                    }
                }
            }

            mahou++;
            for (int[] r: rotMahou){
                diffX = r[0];
                diffY = r[1];

                nextX = vals[0] + diffX;
                nextY = vals[1] + diffY;

                if ((massCheck(nextX, nextY)) && ('.' == Sz[nextX][nextY])) {
                    if ((checked[nextX][nextY] == -1) || (checked[nextX][nextY] > mahou)){
                        checked[nextX][nextY] = mahou;
                        int[] next = {nextX, nextY};
                        deque.addLast(next);
                    }
                }
            }
        }
        System.out.println(checked[Dz[0]][Dz[1]]);
    }
    public static boolean massCheck(int X, int Y){
        return !((X < 0) || (X >= H) || (Y < 0) || (Y >= W)); //範囲内ならtrue
    }
}