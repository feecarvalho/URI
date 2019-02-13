import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.000");

        int x;
        double y;

        x = input.nextInt();
        y = input.nextDouble();

        double consumo = x / y;
        System.out.println(df.format(consumo) + " km/l");
    }
}
