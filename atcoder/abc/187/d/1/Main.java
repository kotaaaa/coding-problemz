import java.util.*;
public class Main {

//    static int[] a = {0,21,100,13,41,40,1,30,0};
//    static int[] aOrig = {0,21,100,13,41,40,1,30,0};
    static int[] diffzIdx = new int[4];


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] Az = new int[N];
        int[] Bz = new int[N];
        int[] diffz = new int[N];
        int[] diffzIdx = new int[N];

        for (int i = 0; i < N; i++){
            Az[i] = sc.nextInt();
            Bz[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++){
            diffz[i] = Az[i] - Bz[i];
        }

        for (int i = 0; i < N; i++){
            diffzIdx[i] = i;
        }

        mergeSort(diffz, 0, N);

        for (int i = 0; i < N; i++){
            System.out.println("diffz "+diffz[i]);
        }
        for (int i = 0; i < N; i++){
            System.out.println("diffzIdx "+diffzIdx[i]);
        }
        for (int i = 0; i < N; i++){
            System.out.println("diffz[aIdx] "+diffz[diffzIdx[i]]);
        }
    }

    public static void mergeSort (int[] a, int left, int right) {
        if (right - left == 1){
            return;
        }
        int mid = (left + right)/2;

        int[] l = new int[mid - left];
        int[] r = new int[right - mid];

        int[] lIdx = new int[mid - left];
        int[] rIdx = new int[right - mid];

        mergeSort(a, left, mid);
        mergeSort(a, mid, right);

        for (int i = 0; i < mid - left; i++){
            l[i] = a[left + i];
            lIdx[i] = diffzIdx[left + i];
        }
        for (int i = 0; i < right - mid; i++){
            r[i] = a[mid + i];
            rIdx[i] = diffzIdx[mid + i];
        }
        merge(a, l, r, left, lIdx, rIdx);
    }

    public static void merge(int[] a, int[] l, int[] r, int left, int[] lIdx, int[] rIdx) {
        int i = 0; int j = 0; int k = left;
        while (i < l.length && j < r.length) {
            if (l[i] <= r[j]){
                a[k] = l[i];
                diffzIdx[k] = lIdx[i];
                i++;
            } else {
                a[k] = r[j];
                diffzIdx[k] = rIdx[j];
                j++;
            }
            k++;
        }
        while (i < l.length){
            a[k] = l[i];
            diffzIdx[k] = lIdx[i];
            k++;
            i++;
        }
        while (j < l.length){
            a[k] = r[j];
            diffzIdx[k] = rIdx[j];
            k++;
            j++;
        }
    }
}