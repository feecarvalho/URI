import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) throws IOException {

        double A, B, C, delta, x1, x2;

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00000");

        A = input.nextDouble();
        B = input.nextDouble();
        C = input.nextDouble();

        if(A != 0) {
            delta = (Math.pow(B, 2) - (4 * A * C));
            if(delta < 0){
                System.out.println("Impossivel calcular");
            } else {
                x1 = ((-B) + (Math.sqrt(delta))) / (2 * A);
                x2 = ((-B) - (Math.sqrt(delta))) / (2 * A);
                System.out.println("R1 = " + df.format(x1));
                System.out.println("R2 = " + df.format(x2));
            }
        } else {
            System.out.println("Impossivel calcular");
        }
    }
}
