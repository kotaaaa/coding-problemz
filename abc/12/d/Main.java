import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] Az = new int[M+1];
        int[] Bz = new int[M+1];
        int[] Tz = new int[M+1];
        int[][] cost = new int[N+1][N+1];

        for (int i = 1; i <= M; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
            Tz[i] = sc.nextInt();
        }
        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 0; i <= N; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        int[] fixed = new int[N+1];
        Queue<Integer> queue = new ArrayDeque<Integer>();
        for (int i = 1; i <= M; i++){
            adjacentMatrix.get(Az[i]).add(Bz[i]);
            adjacentMatrix.get(Bz[i]).add(Az[i]);
            cost[Az[i]][Bz[i]] = Tz[i];
        }

        int constMax = 1000000;
//        Queue<Integer> queue = new PriorityQueue<Integer>();
        Queue<Integer> queue = new DeQueue<Integer>();
        int[] ansz = new int[N+1];
        int[] distance = new int[N+1];
        int[] visited = new int[N+1];
        int current = 0;
        Array.fills(distance, Integer.MAX_VALUE);
        for (int i = 1; i <= N; i++){
            distance = new int[N+1];
            Arrays.fill(distance, constMax);
            confirmedCost = new int[N+1];
            confirmedCost[i] = 0;
//            visited = new int[N+1];
            queue = new DeQueue<Integer>();
            queue.add(i);
//            int current = i;
            ArrayList<Integer> nextCityList = new ArrayList<Integer>();
            int nextMin = constMax;
            int nextMinIdx = constMax;
            while (queue.size() > 0) {
                current = queue.poll();
//                visited[current] = 1;
                nextCityList = adjacentMatrix.get(current);
                for (int j = 0; j < nextCityList.size(); j++){
                    int next = nextCityList.get(j);
                    if (i == current) {
                        distance[next] = cost[current][next];
                    } else {
                        // 既存の仮のパス帳より短かったら，値を更新する
                        if (distance[next] > (distance[current] + cost[current][next])){
                            distance[next] = distance[current] + cost[current][next];
                        }
                    }

                    if (distance[i] < nextMin) {
                        nextMinIdx = next;
                        nextMin = distance[i];
                    }




                }

            }

        }




    }
}