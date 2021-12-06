import java.util.*;
public class Main {
    // sort 時，indexも合わせて保持しておきたいときの，モジュール．
    // 使い方
    //　mergetSort, merge関数をコピペして，main 関数のように呼び出す
    // 注意点: 0-indexの配列でしか使えない，TODO: 1-indexの配列対応

    static int[] a = {0,21,100,13,41,40,1,30,0};
    static int[] aOrig = {0,21,100,13,41,40,1,30,0};
//    static int[] aIdx = new int[a.length];

    public static void main(String[] args) {
        int[] aIdx = new int[a.length];
        for (int i = 0; i < a.length; i++){
            aIdx[i] = i;
        }
        mergeSort(a, aIdx, 0,a.length);
        for (int i = 0; i < a.length; i++){
            System.out.println("a "+a[i]);
        }
        for (int i = 0; i < a.length; i++){
            System.out.println("aIdx "+aIdx[i]);
        }
        for (int i = 0; i < a.length; i++){
            System.out.println("a[aIdx] "+aOrig[aIdx[i]]);
        }
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