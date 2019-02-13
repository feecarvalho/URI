import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args) throws IOException {

        double A;
        double B;
        double MEDIA;

        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00000");

        A = input.nextFloat();
        B = input.nextFloat();

        if(A > 10 && B > 10) {
            System.out.println("Não é possivel continuar");
        } else {
        MEDIA = ((A * 3.5) + (B * 7.5))/11;
        System.out.println("MEDIA = " + df.format(MEDIA));
        }
    }
}
