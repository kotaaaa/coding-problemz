import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] Az = new int[M];
        int[] Bz = new int[M];

        for (int i = 0; i < M; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
        }
        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 0; i <= N; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        int[] visited = new int[N+1];
        visited[0] = 1;
        Queue<Integer> queue = new ArrayDeque<Integer>();
        for (int i = 0; i < M; i++){
            adjacentMatrix.get(Az[i]).add(Bz[i]);
            adjacentMatrix.get(Bz[i]).add(Az[i]);
        }
        int target = 0;
        int maxCnt = 0;
        int count = 0;
        for (int i = 1; i <= N; i++){
            if (visited[i] == 1){
                continue;
            }
            count = 1;
            queue.add(i);
            while (queue.size() > 0){
                target = queue.poll();
                visited[target] = 1;
                for (int j: adjacentMatrix.get(target)){
                    if (visited[j] == 1) {
                        continue;
                    }
                    queue.add(j);
                    visited[j] = 1;
                    count++;
                }
            }
            if (count > maxCnt){
                maxCnt = count;
            }
        }
        System.out.println(maxCnt);
    }
}