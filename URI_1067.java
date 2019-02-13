import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

    int num;

        Scanner input = new Scanner(System.in);

        num = input.nextInt();

        for(int i = 0; i <= num; i++) {
            if(i % 2 != 0){
                System.out.println(i);
            }
        }
    }
}
