import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

    int N, horas, minutos;

    N = input.nextInt();

    horas = N / 3600;
    N -= 3600 * horas;
    minutos = N / 60;
    N -= 60 * minutos;


    System.out.println(horas + ":" + minutos + ":" + N);

    }
}
