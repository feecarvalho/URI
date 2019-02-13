import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.0000");

        double x1, y1, x2, y2;

        x1 = input.nextDouble();
        y1 = input.nextDouble();
        x2 = input.nextDouble();
        y2 = input.nextDouble();

        double distancia = Math.sqrt( Math.pow(x2-x1, 2) + Math.pow(y2 - y1, 2) );

        System.out.println(df.format(distancia));
    }
}
