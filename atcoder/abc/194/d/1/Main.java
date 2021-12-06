import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        String s = sc.next();
        String t = sc.next();

        int[] sInt = new int[4];
        int[] tInt = new int[4];

        HashMap<Integer, Integer> sMap = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> tMap = new HashMap<Integer, Integer>();

        for (int i = 1; i <= 9; i++) {
            sMap.put(i,0);
            tMap.put(i,0);
        }

        for (int i = 0; i < 4; i++) {
            sInt[i] = s.charAt(i) - 48;
            tInt[i] = t.charAt(i) - 48;
            sMap.put(sInt[i], sMap.get(sInt[i]) + 1);
            tMap.put(tInt[i], tMap.get(tInt[i]) + 1);
        }

        System.out.println("smap");
        for (int a : sMap.keySet()){
            System.out.println(a+" "+sMap.get(a));
        }
        System.out.println("tmap");
        for (int a : tMap.keySet()){
            System.out.println(a+" "+tMap.get(a));
        }

        List<int[]> list = new ArrayList<int[]>();

        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                System.out.println("i "+i+" j "+j);
                sMap.put(i, sMap.get(i) + 1);
                tMap.put(j, tMap.get(j) + 1);
                int sScore = 0;
                int tScore = 0;
                boolean doS = true;
                for (int r = 1; r <= 9; r++) {

//                    int lasti = 0;
//                    if (i == r){
//                        lasti++;
//                    }
//                    int lastj = 0;
//                    if (j == r){
//                        lastj++;
//                    }
                    if (!sMap.keySet().contains(r) || i != r) {
                        sScore += r + lasti;
                    } else {
                        if (sMap.get(r) + lasti > k) {
                            sScore = 0;

                        } else {
                            sScore += r * Math.pow(10, Math.min(sMap.get(r) + lasti, k));
                        }

                    }

                    if (!tMap.keySet().contains(r) || j != r) {
                        tScore += r + lastj;
                    } else {
                        tScore += r * Math.pow(10, Math.min(tMap.get(r) + lastj, k));
                    }
                    System.out.println(r+" sScore "+sScore+" tScore "+tScore);
                }

                if (sScore > tScore) {
                    int[] a = {i,j};
                    list.add(a);
                }
                System.out.println("sScore "+sScore+" tScore "+tScore);
//                break;
            }
//            break;
        }
        for (int[] a: list) {
            System.out.println(a[0]+" "+a[1]);
        }

    }
}