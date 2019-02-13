import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) throws IOException {

        double A, B, C;
        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.0");

        A = input.nextDouble();
        B = input.nextDouble();
        C = input.nextDouble();

        double perimetro = A + B + C;
        double areaT = (C * (A + B)) / 2;

        if(A < 0 || B < 0 || C < 0) {
            System.exit(0);
        } else if (Math.abs(B - C) < A && A < (B + C)) {
            System.out.println("Perimetro = " + df.format(perimetro));
        } else {
            System.out.println("Area = " + df.format(areaT));
        }
    }
}
