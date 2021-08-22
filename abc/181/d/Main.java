import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        String tmpS = S;

        int num = 0;
        // 100 未満のとき．
        int intS = Integer.parseInt(S);
        if (intS == 8){
            System.out.println("Yes");
            System.exit(0);
        }
        List<String> pattern8low100 = new ArrayList<String>();
        for (int i = 1; i <= 100; i++){
            String strVal = String.valueOf(i);
            if (i % 8 == 0){
                pattern8low100.add(String.valueOf(i));
            }
        }
        // 2桁のときfor文回す
        if (intS < 100){
            for (int j = 0; j < pattern8low100.size(); j++){
                num = 0;
                tmpS = S;
                for (int k = 0; k < 2; k++){
                    if (tmpS.contains(pattern8low100.get(j).substring(k,k+1))){
                        num++;
                        tmpS = tmpS.replaceFirst(pattern8low100.get(j).substring(k,k+1), "");
                    }
                }
                if (num == 2) {
                    System.out.println("Yes");
                    System.exit(0);
                }
            }
            System.out.println("No");
            System.exit(0);
        }

        // 下三桁の数字のリストを作成する．
        List<String> pattern8 = new ArrayList<String>();

        for (int i = 101; i <= 1000; i++){
            String strVal = String.valueOf(i);
            if (i % 8 == 0){
                pattern8.add(String.valueOf(i));
            }
        }


        // for 文回す
        for (int j = 0; j < pattern8.size(); j++){
            num = 0;
            tmpS = S;
            for (int k = 0; k < 3; k++){
                if (tmpS.contains(pattern8.get(j).substring(k,k+1))){
                    num++;
                    tmpS = tmpS.replaceFirst(pattern8.get(j).substring(k,k+1), "");
                }
            }
            if (num == 3) {
                System.out.println("Yes");
                System.exit(0);
            }
        }
        System.out.println("No");
    }
}