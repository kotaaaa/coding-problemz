import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double Sx = sc.nextInt();
        double Sy = sc.nextInt();
        double Gx = sc.nextInt();
        double Gy = sc.nextInt();

        double heightRatio = Sy / (Sy + Gy);
        double diffX = Gx - Sx;

//        System.out.println(heightRatio);
//        System.out.println(diffX);

        double x0 = heightRatio * diffX + Sx;
        System.out.println(x0);


    }
}