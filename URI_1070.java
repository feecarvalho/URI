import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        int x;

        Scanner input = new Scanner(System.in);

        x = input.nextInt();

        for(int i = 0; i < 12; i++) {
            if(x % 2 != 0) {
                System.out.println(x);
            }
            x = x + 1;
        }
    }
}
