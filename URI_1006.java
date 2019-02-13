import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0");

        double A, B, C, MEDIA;

        A = input.nextDouble();
        B = input.nextDouble();
        C = input.nextDouble();


        if (A > 10 && B > 10 && C > 10){
            System.out.println("Valor invalido");
        } else {

            A *= 2.0;
            B *= 3.0;
            C *= 5.0;

            MEDIA = (A+B+C)/10;

            System.out.println("MEDIA = " + df.format(MEDIA));
        }
    }
}
