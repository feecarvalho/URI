import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.000");

        double A, B, C;

        final double PI = 3.14159;

        A = input.nextDouble();
        B = input.nextDouble();
        C = input.nextDouble();

        double triangulo, circulo, trapezio, quadrado, retangulo;

        triangulo = (A * C) / 2;
        circulo = PI * C * C;
        trapezio = ((A + B)*C) / 2;
        quadrado = B * B;
        retangulo = A * B;

        System.out.println("TRIANGULO: " + df.format(triangulo) + "\nCIRCULO: " + df.format(circulo) + "\nTRAPEZIO: " + df.format(trapezio) + "\nQUADRADO: " + df.format(quadrado) + "\nRETANGULO: " + df.format(retangulo));
    }
}
