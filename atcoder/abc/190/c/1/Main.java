import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] az = new int[m+1];
        int[] bz = new int[m+1];
        for (int i = 1; i <= m; i++){
            az[i] = sc.nextInt();
            bz[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        int[] cz = new int[n+1];
        int[] dz = new int[n+1];
        for (int i = 1; i <= k; i++){
            cz[i] = sc.nextInt();
            dz[i] = sc.nextInt();
        }

//        int maxColor = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 0; i <= n; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        for (int i = 1; i <= k; i++){
            adjacentMatrix.get(cz[i]).add(dz[i]);
            adjacentMatrix.get(dz[i]).add(cz[i]);
        }
        System.out.println("adja");
        for (int i = 1; i <= n; i++){
            for (int j : adjacentMatrix.get(i)){
                System.out.println("adja " +i+" "+j);
            }

        }

        int[] visited = new int[n+1];
        int[] cycleNode = new int[n+1];

        int target = 0;
        int treeCnt = 0;
        int cycleCnt = 0;
        int cycleBool = 0;
        int isCycle = 0;

        Deque<Integer> stack; //  = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            isCycle = 0;
            cycleBool = 0;
            stack = new ArrayDeque<>();
            if (visited[i] == 1) {
                continue;
            }
            isCycle = dfs(i, 0, visited, adjacentMatrix, cycleBool, stack);
            System.out.println("iscycle "+isCycle);
            if (isCycle == 1) {
                while (!stack.isEmpty()) {
                    cycleNode[stack.pop()] = 1;
                }
            }
        }

        int cycleNodeCnt = 0;
        for (int i = 1; i <= n; i++){
            if (cycleNode[i] == 1){
                cycleNodeCnt++;
            }
            System.out.println("cycleNode "+i+" "+cycleNode[i]);
        }
        if (cycleNodeCnt == n){
            System.out.println(n);
            System.exit(0);
        }

        int cnt = 0;
        int maxCnt = 0;
        int node = 0
        for (int i = 1; i <= n; i++){
            if (cycleNode[i] == 1){
                node++;
                continue;
            } else {
                cnt = 0;
                for (int j = 1; j <= m; j++){
                    if ((az[j] != i) && (visited[j] == 1)) {
                        cnt++;
                    }
                }
                maxCnt = Math.max(cnt, maxCnt);
            }
        }
        System.out.println(maxCnt);
    }


    public static int dfs (int current, int before, int[] visited, ArrayList<ArrayList<Integer>> graph, int cycleBool, Deque<Integer> stack) {
        if (visited[current] == 1){
            return cycleBool;
        }
        System.out.println("current "+current+" before "+before);
        visited[current] = 1;
        stack.push(current);
        for (int j: graph.get(current)){
            if (j == before){
                continue;
            }
            System.out.println("j "+j+" visited[j] "+visited[j]);
            if (visited[j] == 1){
                cycleBool = 1;
//                System.out.println("cycleBool? "+cycleBool);
            }
            cycleBool = dfs(j, current, visited, graph, cycleBool, stack);
            System.out.println("current "+current+" before "+before+" cycleBool? "+cycleBool);
        }
//        stack.pop();
        return cycleBool;
    }
}