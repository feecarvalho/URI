import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) {

        double raio, area;
        final double PI = 3.14159;

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("00.0000");

        raio = input.nextDouble();

        area = PI * raio * raio;

        System.out.println("A="+ df.format(area));
    }
}
