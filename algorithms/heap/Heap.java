import java.util.*;
/**
 * ヒープソート用のクラス
 */
public class Heap {
    int[] origArray;
    int[] origHeap;
    int[] forSortHeap;
    int[] sortedHeap;
    int arrayLength;
    /**
     * ヒープソート用の配列を取得する．
     */
    public void getForSortHeap(){
        for (int i: forSortHeap){
            System.out.print(i+", ");
        }
        System.out.println();
    }
    /**
     * ヒープソートされた配列を取得する
     */
    public void getSortedHeap(){
        for (int i: sortedHeap){
            System.out.print(i+", ");
        }
        System.out.println();
    }
    /**
     * コンストラクタ．配列データをヒープ配列に格納する
     * @param array ソート前の初期配列
     */
    public Heap(int[] array){
        arrayLength = array.length;
        this.origArray = new int[array.length];
        this.origArray = array;
        this.origHeap = new int[array.length];
        this.forSortHeap = new int[array.length];
        this.sortedHeap = new int[array.length];
        for (int i = 0; i < array.length; i++){
            insert(i);
        }
    }
    /**
     * idxN番目の要素をヒープ配列に格納する
     * @param idxN
     */
    public void insert(int idxN){
        int idxParent = idxN;
        int nextIdxParent = 0;
        int tmp = 0;
        this.forSortHeap[idxN] = this.origArray[idxN];
        while (idxParent >= 0){
            nextIdxParent = idxParent / 2;
            if (forSortHeap[nextIdxParent] < forSortHeap[idxParent]){
                swap(forSortHeap, nextIdxParent, idxParent);
            } else {
                break;
            }
            idxParent = nextIdxParent;
        }
    }
    /**
     * ヒープソートを実行（ヒープの最大値をヒープ配列から削除して，順に配列に追加する）
     */
    public void sort(){
        for (int i = 0; i < arrayLength; i++){
            sortedHeap[i] = getMax();
            removeMax(i);
        }
    }
    /**
     * ヒープ内の最大値をpopし，ヒープ用の新しい配列に再格納
     * @param idxNmax forSortHeapのidx (n-th max value in array will be deleted. )
     */
    public void removeMax(int idxNmax){ // n-th max value in array will be deleted.
        int idxChild = 0;
        forSortHeap[0] = forSortHeap[arrayLength - idxNmax - 1];
        forSortHeap[arrayLength - idxNmax - 1] = 0;
        while (2 * idxChild + 2 < arrayLength){
            if ((forSortHeap[idxChild] > forSortHeap[2 * idxChild + 1]) && (forSortHeap[idxChild] > forSortHeap[2 * idxChild + 2])){
                break;
            }
            if (forSortHeap[2 * idxChild + 1] >= forSortHeap[2 * idxChild + 2]){
                swap(forSortHeap, 2 * idxChild + 1, idxChild);
                idxChild = 2 * idxChild + 1;
            } else {
                swap(forSortHeap, 2 * idxChild + 2, idxChild);
                idxChild = 2 * idxChild + 2;
            }
        }
    }
    /**
     * ヒープの最大値を取得
     * @return 最大値
     */
    public int getMax(){
        return forSortHeap[0];
    }
    /**
     * 配列の要素の入れ替えを行う
     * @param arr swap対象の配列
     * @param a index 1つ目
     * @param b index 2つ目
     */
    public void swap(int[] arr, int a, int b){
        int tmp = 0;
        tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}