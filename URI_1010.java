import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("00.00");

        int peca1, peca2, quantidade1, quantidade2;
        double valor1, valor2;

        peca1 = input.nextInt();
        quantidade1 = input.nextInt();
        valor1 = input.nextDouble();

        peca2 = input.nextInt();
        quantidade2 = input.nextInt();
        valor2 = input.nextDouble();

        System.out.println("VALOR A PAGAR: R$ " + df.format((valor1 * quantidade1)+(valor2 * quantidade2)));
    }
}
