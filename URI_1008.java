import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        int numero, horas;
        double valorHoras, salario;

        numero = input.nextInt();
        horas = input.nextInt();
        valorHoras = input.nextDouble();

        salario = (double)horas * valorHoras;

        System.out.println("NUMBER = " + numero);
        System.out.println("SALARY = U$ " + df.format(salario));
    }
}
