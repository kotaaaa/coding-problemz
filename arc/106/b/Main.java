import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] Az = new long[N];
        long[] Bz = new long[N];
        int[] Cz = new int[M];
        int[] Dz = new int[M];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextLong();
        }
        for (int i = 0; i < N; i++){
            Bz[i] = sc.nextLong();
        }
        for (int i = 0; i < M; i++){
            Cz[i] = sc.nextInt();
            Dz[i] = sc.nextInt();
        }
        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 0; i <= N; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        int[] visited = new int[N+1];
        visited[0] = 1;
        Queue<Integer> queue = new ArrayDeque<Integer>();
        for (int i = 0; i < M; i++){
            adjacentMatrix.get(Cz[i]).add(Dz[i]);
            adjacentMatrix.get(Dz[i]).add(Cz[i]);
        }

        int target = 0;
        long beforeCnt = 0;
        long afterCnt = 0;
        for (int i = 1; i <= N; i++){
            if (visited[i] == 1){
                continue;
            }
            beforeCnt = Az[i-1];
            afterCnt = Bz[i-1];
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
                    beforeCnt += Az[j-1];
                    afterCnt += Bz[j-1];
                }
            }
            if (beforeCnt != afterCnt){
                System.out.println("No");
                System.exit(0);
            }
        }

        System.out.println("Yes");
    }
}