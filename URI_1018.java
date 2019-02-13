import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int N, x;

        N = input.nextInt();

        System.out.println(N);

        if(N > 0 && N < 1000000) {
            x = N / 100;
            N -= x * 100;
            System.out.println(x + " nota(s) de R$ 100,00");

            x = N / 50;
            N -= x * 50;
            System.out.println(x + " nota(s) de R$ 50,00");

            x = N / 20;
            N -= x * 20;
            System.out.println(x + " nota(s) de R$ 20,00");

            x = N / 10;
            N -= x * 10;
            System.out.println(x + " nota(s) de R$ 10,00");

            x = N / 5;
            N -= x * 5;
            System.out.println(x + " nota(s) de R$ 5,00");

            x = N / 2;
            N -= x * 2;
            System.out.println(x + " nota(s) de R$ 2,00");

            x = N / 1;
            N -= x * 1;
            System.out.println(x + " nota(s) de R$ 1,00");

        }
    }
}
