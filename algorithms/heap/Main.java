import java.util.*;
public class Main {
    public static void main(String[] args){
        int[] a = {3,9,1,6,10,13,2,18,4,7,20};
        Heap heap = new Heap(a);
        System.out.println("getForSortHeap>>> ");
        heap.getForSortHeap();
        heap.sort();
        System.out.println("getSortedHeap>>> ");
        heap.getSortedHeap();
    }
}
