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
        for (int i = 0; i < M; i++){
            adjacentMatrix.get(Az[i]).add(Bz[i]);
            adjacentMatrix.get(Bz[i]).add(Az[i]);
        }

        int cnt = 1;
        int[] path = new int[N+1];
        path[1] = 1;
        int[] signpost = new int[N+1];

        int tmpRoom = 0;
        List<Integer> tmpRoomPath = new ArrayList<>();
        Queue<Integer> queue = new ArrayDeque<Integer>();

        queue.add(1);
        while (queue.size() > 0){
            tmpRoom = queue.poll();
//            System.out.println("tmproom "+tmpRoom);
            tmpRoomPath = adjacentMatrix.get(tmpRoom);
            for (int i = 0; i < tmpRoomPath.size(); i++){
                if (path[tmpRoomPath.get(i)] != 0){
                    continue;
                }
//                System.out.println(tmpRoomPath.get(i)+" cnt "+cnt);
                queue.add(tmpRoomPath.get(i));
                path[tmpRoomPath.get(i)] = cnt;
                signpost[tmpRoomPath.get(i)] = tmpRoom;
            }
//            System.exit(0);
            cnt++;
        }

        for (int i = 2; i <= N; i++){
            if (path[i] == 0){
                System.out.println("No");
                System.exit(0);
            }
        }
        System.out.println("Yes");
        for (int i = 2; i <= N; i++){
//            System.out.println(path[i]);
            System.out.println(signpost[i]);
        }
    }
}