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

        System.out.println("aa1 ");
        int[][] adjacentMatrix = new int[N+1][N+1];
//        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        System.out.println("aa2 ");
        int[] visited = new int[N+1];
        visited[0] = 1;
        System.out.println("aa ");
        Queue<Integer> queue = new ArrayDeque<Integer>();
        for (int i = 0; i < M; i++){
            adjacentMatrix[Az[i]][Bz[i]] = 1;
            adjacentMatrix[Bz[i]][Az[i]] = 1;
        }
//        for (int i = 0; i < M; i++){
//            adjacentMatrix.get(Az[i]-1).add(Bz[i]-1);
//        }
        System.out.println("bb ");

        int target = 0;
        int maxCnt = 0;
        int count = 0;
        for (int i = 1; i <= N; i++){
            count = 0;
            if (visited[i] == 1){
                continue;
            }
            queue.add(i);
            while (queue.size() > 0){
                System.out.println("target "+target);
                target = queue.poll();
                visited[target] = 1;
                for (int j = 1; j <= N; j++){
                    if (adjacentMatrix[target][j] == 0) {
                        continue;
                    }
                    if (visited[j] == 1) {
                        continue;
                    }
                    queue.add(i);
                    visited[j] = 1;
                }
                count++;
            }
            if (count > maxCnt){
                maxCnt = count;
            }
        }

//        System.out.println("max "+maxCnt);
        System.out.println(maxCnt);



    }
}