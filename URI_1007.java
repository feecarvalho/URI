import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int A, B, C, D, DIFERENCA;

        Scanner input = new Scanner(System.in);

        A = input.nextInt();
        B = input.nextInt();
        C = input.nextInt();
        D = input.nextInt();

        DIFERENCA = (A * B - C * D);

        System.out.println("DIFERENCA = " + DIFERENCA);
    }
}
