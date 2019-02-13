import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        double n1, n2, n3, n4, n5, n6;
        int aux = 0;

        Scanner input = new Scanner(System.in);

        n1 = input.nextDouble();
        n2 = input.nextDouble();
        n3 = input.nextDouble();
        n4 = input.nextDouble();
        n5 = input.nextDouble();
        n6 = input.nextDouble();

        if(n1 > 0) {
            aux++;
        }
        if(n2 > 0) {
            aux++;
        }
        if(n3 > 0) {
            aux++;
        }
        if(n4 > 0) {
            aux++;
        }
        if(n5 > 0) {
            aux++;
        }
        if(n6 > 0) {
            aux++;
        }
        System.out.println(aux + " valores positivos");
    }
}
