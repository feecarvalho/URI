import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        int x;

        Scanner input = new Scanner(System.in);

        String[] mes = new String[13];

        mes[1] = "January";
        mes[2] = "February";
        mes[3] = "March";
        mes[4] = "April";
        mes[5] = "May";
        mes[6] = "June";
        mes[7] = "July";
        mes[8] = "August";
        mes[9] = "September";
        mes[10] = "October";
        mes[11] = "November";
        mes[12] = "December";

        x = input.nextInt();

        if(x > 0 && x < 13) {
            System.out.println(mes[x]);
        } else {
            System.exit(0);
        }
    }
}
