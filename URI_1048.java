import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) throws IOException {

        double salario;

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.00");

        salario = input.nextDouble();

        double reajuste, aux;

        if(salario <= 400) {
            aux = salario + (salario * 0.15);
            System.out.println("Novo salario: " + df.format(aux));
            reajuste = aux - salario;
            System.out.println("Reajuste ganho: " + df.format(reajuste));
            System.out.println("Em percentual: 15 %");
        } else if(salario <= 800) {
            aux = salario + (salario * 0.12);
            System.out.println("Novo salario: " + df.format(aux));
            reajuste = aux - salario;
            System.out.println("Reajuste ganho: " + df.format(reajuste));
            System.out.println("Em percentual: 12 %");
          } else if(salario <= 1200) {
            aux = salario + (salario * 0.10);
            System.out.println("Novo salario: " + df.format(aux));
            reajuste = aux - salario;
            System.out.println("Reajuste ganho: " + df.format(reajuste));
            System.out.println("Em percentual: 10 %");
          } else if(salario<= 2000) {
            aux = salario + (salario * 0.07);
            System.out.println("Novo salario: " + df.format(aux));
            reajuste = aux - salario;
            System.out.println("Reajuste ganho: " + df.format(reajuste));
            System.out.println("Em percentual: 7 %");
          } else if(salario > 2000) {
            aux = salario + (salario * 0.04);
            System.out.println("Novo salario: " + df.format(aux));
            reajuste = aux - salario;
            System.out.println("Reajuste ganho: " + df.format(reajuste));
            System.out.println("Em percentual: 4 %");
          }
    }

}
