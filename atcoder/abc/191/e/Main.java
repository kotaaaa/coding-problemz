import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] Az = new int[M+1];
        int[] Bz = new int[M+1];
        int[] Cz = new int[M+1];

        int CONSTMAX = 10000000;

        for (int i = 1; i <= M; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
            Cz[i] = sc.nextInt();
        }
        int[] confirmedDistance = new int[N+1];
        int[][] cost = new int[N+1][N+1];
        for (int i = 0; i <= N; i++){
            for (int j = 0; j <= N; j++){
                cost[i][j] = CONSTMAX;
            }
        }
        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 1; i <= N+1; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        for (int i = 1; i <= M; i++){
            adjacentMatrix.get(Az[i]).add(Bz[i]);
            if (cost[Az[i]][Bz[i]] > Cz[i]) {
                cost[Az[i]][Bz[i]] = Cz[i];
            }
        }
        Queue<Integer> queue = new ArrayDeque<Integer>();

        int[] distance = new int[N+1];
        Arrays.fill(distance, CONSTMAX);
        List<Integer> adjaList = new ArrayList<Integer>();
        int[] ans = new int[N+1];
        for (int i = 1; i <= N; i++) {
//            System.out.println("i >>>>>> "+i);
            int current = 0;
            int next = 0;
            int toGoalMin = CONSTMAX;
            confirmedDistance = new int[N+1];
            Arrays.fill(distance, CONSTMAX);
            queue.add(i);
            while (queue.size() > 0) {
                // キューから現在処理対象のノードを取り出す
                current = queue.poll();
//                System.out.println("current "+current);
                // targetに隣接するノードを取り出す
                adjaList = adjacentMatrix.get(current);
                int minIdx = 0;
                int min = CONSTMAX; // 毎処理ごとに，最小の整数を取得するための変数を用意
                for (int j = 0; j < adjaList.size(); j++) {
                    next = adjaList.get(j); // 1 -> 2
//                    System.out.println("current "+current + " next "+next+" cost[current][next] "+cost[current][next]);
                    if (confirmedDistance[next] > 0) { // 最短距離が確定している場合飛ばす．
                        continue;
                    }
                    queue.add(next); // 次処理するノードをキューに追加
                    // 距離が最小になるのであれば，最小値を更新する．
                    if (i == current) { // 最初の移動は，その道のコストのみ
                        distance[next] = cost[current][next];
                    } else {
                        distance[next] = Math.min(distance[next], distance[current] + cost[current][next]);
                    }

                    if (next == i) { // もしスタート地点に一周してきたら
                        if (toGoalMin > distance[next]) { // ゴールまでの距離を比較し，最小の距離を取得
                            toGoalMin = distance[next];
                        }
                    }
//                    System.out.println("min "+min+" distance[next] "+distance[next]+" j "+j);
                    // 次に確定するノードを決める．
                    if (min > distance[next]) {
                        min = distance[next];
                        minIdx = next;
                    }
                }
                //各処理ごと最小の値をそのノードまでの最短距離として確定させる．
                confirmedDistance[minIdx] = min;
            }
            if (toGoalMin == CONSTMAX) { // 出発したノードに帰ってこれない場合．
                ans[i] = -1;
            } else {
                ans[i] = toGoalMin;
            }
//            break;
        }

//        System.out.println("ans >>> ");
        for (int i = 1; i <= N; i++) {
            System.out.println(ans[i]);
        }
    }
}