/*
これは正解
3は不正解している
*/

import java.util.*;
public class Main {

    static int c = 0;
    static int cycleBool = 0;
    static int ans = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Az = new int[N+1];
        int[] Bz = new int[N+1];

        int maxColor = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i = 1; i <= N; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
            if (Az[i] > maxColor){
                maxColor = Az[i];
            }
            if (Bz[i] > maxColor){
                maxColor = Bz[i];
            }
        }

        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 0; i <= maxColor; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        for (int i = 1; i <= N; i++){
            adjacentMatrix.get(Az[i]).add(Bz[i]);
            adjacentMatrix.get(Bz[i]).add(Az[i]);
        }

        int[] visited = new int[maxColor+1];

        for (int i = 1; i <= maxColor; i++) {
            if (visited[i] == 1) {
                continue;
            }
            c = 0;
            cycleBool = 0;
            dfs(i, 0, visited, adjacentMatrix);
            if (cycleBool == 1){
                ans += c;
            } else {
                ans += c-1;
            }
        }
        System.out.println(ans);
    }

    public static void dfs (int current, int before, int[] visited, ArrayList<ArrayList<Integer>> graph) {
        if (visited[current] == 1){
            return;
        }
        c++;
        visited[current] = 1;
        for (int j: graph.get(current)){
            if (j == before){
                continue;
            }
            if (visited[j] == 1){
                cycleBool = 1;
            }
            dfs(j, current, visited, graph);
        }
        return;
    }
}