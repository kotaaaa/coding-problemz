import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] Az = new int[N];
        int[] AzIdx = new int[N];

        int[] Xz = new int[M];
        int[] Yz = new int[M];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            AzIdx[i] = i;
        }

        for (int i = 0; i < M; i++){
            Xz[i] = sc.nextInt();
            Yz[i] = sc.nextInt();
        }

        mergeSort(Az, AzIdx, 0, Az.length);

        ArrayList<ArrayList<Integer>> adjacentMatrix = new ArrayList<>();
        for (int i = 0; i <= N; i++){
            adjacentMatrix.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < M; i++){
            adjacentMatrix.get(Xz[i]).add(Yz[i]);
        }

        int[] visited = new int[N+1];
        Queue<Integer> queue = new ArrayDeque<Integer>();
        int target = 0;
        int tmpMin = 0;
        int tmpDiffMax = -1*Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            if (visited[AzIdx[i]+1] == 1) {
                continue;
            }
            queue.add(AzIdx[i]);
            tmpMin = Az[AzIdx[i]];
            while (queue.size() > 0){
                target = queue.poll();
                visited[target+1] = 1;
                if ((tmpDiffMax < Az[target] - tmpMin) && (AzIdx[i] != target)){
                    tmpDiffMax = Az[target] - tmpMin;
                }
                for (int j: adjacentMatrix.get(target+1)){
                    if (tmpDiffMax < Az[j-1] - tmpMin){
                        tmpDiffMax = Az[j-1] - tmpMin;
                    }
                    if (visited[j] == 1) {
                        continue;
                    }
                    queue.add(j-1);
                    visited[j] = 1;
                }
            }
        }
        System.out.println(tmpDiffMax);
    }

    public static void mergeSort (int[] a, int[] aIdx, int left, int right) {
        if (right - left == 1){
            return;
        }
        int mid = (left + right)/2;

        int[] lIdx = new int[mid - left];
        int[] rIdx = new int[right - mid];

        mergeSort(a, aIdx, left, mid);
        mergeSort(a, aIdx, mid, right);

        for (int i = 0; i < mid - left; i++){
            lIdx[i] = aIdx[left + i];
        }
        for (int i = 0; i < right - mid; i++){
            rIdx[i] = aIdx[mid + i];
        }
        merge(a, aIdx, left, lIdx, rIdx);
    }

    public static void merge(int[] a, int[] aIdx, int left, int[] lIdx, int[] rIdx) {
        int i = 0; int j = 0; int k = left;
        while (i < lIdx.length && j < rIdx.length) {
            if (a[lIdx[i]] <= a[rIdx[j]]){
                aIdx[k++] = lIdx[i++];
            } else {
                aIdx[k++] = rIdx[j++];
            }
        }
        while (i < lIdx.length){
            aIdx[k++] = lIdx[i++];
        }
        while (j < lIdx.length){
            aIdx[k++] = rIdx[j++];
        }
    }

}