import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        float N;

        N = input.nextFloat();

        if(N >= 0 && N <= 1000000.00){
            System.out.println("NOTAS:");

            System.out.printf("%.0f nota(s) de R$ 100.00\n", Math.floor(N / 100));
            N -= Math.floor(N/100)*100;

            System.out.printf("%.0f nota(s) de R$ 50.00\n", Math.floor(N / 50));
            N -= Math.floor(N/50)*50;

            System.out.printf("%.0f nota(s) de R$ 20.00\n", Math.floor(N / 20));
            N -= Math.floor(N/20)*20;

            System.out.printf("%.0f nota(s) de R$ 10.00\n", Math.floor(N / 10));
            N -= Math.floor(N/10)*10;

            System.out.printf("%.0f nota(s) de R$ 5.00\n", Math.floor(N / 5));
            N -= Math.floor(N/5)*5;

            System.out.printf("%.0f nota(s) de R$ 2.00\n", Math.floor(N / 2));
            N -= Math.floor(N/2)*2;

            System.out.println("MOEDAS:");

            System.out.printf("%.0f moeda(s) de R$ 1.00\n", Math.floor(N / 1));
            N -= Math.floor(N/1)*1;

            System.out.printf("%.0f moeda(s) de R$ 0.50\n", Math.floor(N / 0.5));
            N -= Math.floor(N/0.5)*0.5;

            System.out.printf("%.0f moeda(s) de R$ 0.25\n", Math.floor(N / 0.25));
            N -= Math.floor(N/0.25)*0.25;

            System.out.printf("%.0f moeda(s) de R$ 0.10\n", Math.floor(N / 0.1));
            N -= Math.floor(N/0.1)*0.1;

            System.out.printf("%.0f moeda(s) de R$ 0.05\n", Math.floor(N / 0.05));
            N -= Math.floor(N/0.05)*0.05;

            System.out.printf("%.0f moeda(s) de R$ 0.01\n", (N / 0.01));
        }
    }
}
