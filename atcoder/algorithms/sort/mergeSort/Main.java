import java.util.*;
public class Main {

    static int[] a = {0,21,100,13,41,40,1,30,0};

    public static void main(String[] args) {

//        int i = 0;
//        while(i < a.length){
//            System.out.println(a[i++]);
//        }
        mergeSort(a,0,a.length);
        for (int i = 0; i < a.length; i++){
            System.out.println("a "+a[i]);
        }
    }

    public static void mergeSort (int[] a, int left, int right) {
//        System.out.println("left right "+left+" "+right);
        if (right - left == 1){
            return;
        }
        int mid = (left + right)/2;

        int[] l = new int[mid - left];
        int[] r = new int[right - mid];

        mergeSort(a, left, mid);
        mergeSort(a, mid, right);

        for (int i = 0; i < mid - left; i++){
            l[i] = a[left + i];
        }

        for (int i = 0; i < right - mid; i++){
            r[i] = a[mid + i];
        }

        merge(a, l, r, left);
    }

    public static void merge(int[] a, int l[], int r[], int left) {
        int i = 0; int j = 0; int k = left;
        while (i < l.length && j < r.length) {
            if (l[i] <= r[j]){
                a[k++] = l[i++];
//                i++;
            } else {
                a[k++] = r[j++];
//                j++;
            }
//            k++;
        }
        while (i < l.length){
            a[k++] = l[i++];
//            k++;
//            i++;
        }
        while (j < l.length){
            a[k++] = r[j++];
//            k++;
//            j++;
        }
    }
}