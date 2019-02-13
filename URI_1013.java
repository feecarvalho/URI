import static java.lang.Math.abs;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int a, b, c;
        int maiorAB, maiorMC;

        Scanner input = new Scanner(System.in);

        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();

        maiorAB = (a + b + abs((int) a - b)) / 2;
        maiorMC = (maiorAB + c + abs((int) maiorAB - c)) / 2;

        System.out.println(maiorMC + " eh o maior");
    }
}
