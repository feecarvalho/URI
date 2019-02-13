import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) throws IOException {

        int cod, qtd;
        double total;
        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        cod = input.nextInt();
        qtd = input.nextInt();

        if(cod == 1){
            total = qtd * (4.00);
            System.out.println("Total: R$ " + df.format(total));
            } else if(cod == 2) {
                total = qtd * (4.50);
                System.out.println("Total: R$ " + df.format(total));
                } else if(cod == 3){
                    total = qtd * (5.00);
                    System.out.println("Total: R$ " + df.format(total));
                } else if(cod == 4){
                    total = qtd * (2.00);
                    System.out.println("Total: R$ " + df.format(total));
                } else if(cod == 5){
                    total = qtd * (1.50);
                    System.out.println("Total: R$ " + df.format(total));
                } else {
                    System.out.println("Código Invalido");
                }
        }
}
