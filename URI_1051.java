import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) throws IOException {

        double salario;

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.00");

        salario = input.nextDouble();

        double aux;

        if(salario <= 2000) {
            System.out.println("Isento");
        } else if(salario <= 3000) {
            aux = ((salario - 2000) * 0.08);
            System.out.println("R$ " + df.format(aux));
        } else if(salario <= 4500) {
            aux = salario - 2000;
            if(aux > 1000) {
                aux = (aux - 1000) * 0.18;
                aux = aux + (1000 * 0.08);
                System.out.println("R$ " + df.format(aux));
            } else {
                aux = aux * 0.08;
                System.out.println("R$ " + df.format(aux));
            }
          } else if(salario > 4500) {
            aux = salario - 2000;
            if(aux > 2500) {
                aux = (aux - 2500) * 0.28;
                aux += 1500 * 0.18;
                aux += 1000 * 0.08;
                System.out.println("R$ " + df.format(aux));
            }
          }
    }
}
