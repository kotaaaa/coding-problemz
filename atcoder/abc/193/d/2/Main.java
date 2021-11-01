import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        double k = sc.nextInt();
        String s = sc.next();
        String t = sc.next();

        int[] sInt = new int[4];
        int[] tInt = new int[4];

        HashMap<Integer, Integer> sMap = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> tMap = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> allMap = new HashMap<Integer, Integer>();

        for (int i = 1; i <= 9; i++) {
            sMap.put(i, 0);
            tMap.put(i, 0);
        }

        for (int i = 0; i < 4; i++) {
            sInt[i] = s.charAt(i) - 48;
            tInt[i] = t.charAt(i) - 48;
            sMap.put(sInt[i], sMap.get(sInt[i]) + 1);
            tMap.put(tInt[i], tMap.get(tInt[i]) + 1);
        }

        for (int i = 1; i <= 9; i++) {
            allMap.put(i, sMap.get(i) + tMap.get(i));
        }

//        System.out.println("smap");
//        for (int a : sMap.keySet()) {
//            System.out.println(a + " " + sMap.get(a));
//        }
//        System.out.println("tmap");
//        for (int a : tMap.keySet()) {
//            System.out.println(a + " " + tMap.get(a));
//        }

        List<int[]> list = new ArrayList<int[]>();

        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {

                sMap.put(i, sMap.get(i) + 1);
                tMap.put(j, tMap.get(j) + 1);
                allMap.put(i, allMap.get(i) + 1);
                allMap.put(j, allMap.get(j) + 1);
//                System.out.println("i " + i + " j " + j+" sMap "+sMap+" tMap "+tMap+" allMap "+allMap);
                int sScore = 0;
                int tScore = 0;
                for (int r = 1; r <= 9; r++) {
                    if (allMap.get(r) > k) {
                        sScore = 0;
                        break;
                    }
                    sScore += r * Math.pow(10, sMap.get(r));
                }
                for (int r = 1; r <= 9; r++) {
                    if (allMap.get(r) > k) {
                        tScore = 0;
                        break;
                    }
                    tScore += r * Math.pow(10, tMap.get(r));
                }
                sMap.put(i, sMap.get(i) - 1);
                tMap.put(j, tMap.get(j) - 1);
                allMap.put(i, allMap.get(i) - 1);
                allMap.put(j, allMap.get(j) - 1);
//                System.out.println("sScore " + sScore + " tScore " + tScore);

                if (sScore > tScore) {
                    int[] a = {i, j};
                    list.add(a);
                }
            }
//            break;
        }
        double ans = 0;
        for (int[] a : list) {
//            System.out.println(a[0] + " " + a[1]);
            if (a[0] == a[1]) {
                ans += (k - allMap.get(a[0])) * (k - allMap.get(a[1]) - 1);
            } else {
                ans += (k - allMap.get(a[0])) * (k - allMap.get(a[1]));
            }

//            System.out.println("1, 2 " + (k - allMap.get(a[0])) + " " + (k - allMap.get(a[1])));
//            System.out.println("ans " + ans);
        }
        double bunbo = (9 * k - 8) * (9 * k - 9);
//        System.out.println("aaaa "+ans+" "+bunbo);
        System.out.println(ans / bunbo);

    }
}