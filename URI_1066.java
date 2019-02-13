import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        int x1, x2, x3, x4, x5, auxP = 0, auxI = 0, pos = 0, neg = 0;

        Scanner input = new Scanner(System.in);

        x1 = input.nextInt();
        x2 = input.nextInt();
        x3 = input.nextInt();
        x4 = input.nextInt();
        x5 = input.nextInt();

        if(x1 < 0) {
            neg++;
        } else if(x1 > 0) {
            pos++;
        }
        if(x2 < 0) {
            neg++;
        } else if(x2 > 0) {
            pos++;
        }
        if(x3 < 0) {
            neg++;
        } else if(x3 > 0) {
            pos++;
        }
        if(x4 < 0) {
            neg++;
        } else if(x4 > 0) {
            pos++;
        }
        if(x5 < 0) {
            neg++;
        } else if(x5 > 0) {
            pos++;
        }

        if(x1 % 2 == 0){
            auxP++;
        } else {
            auxI++;
        }

        if(x2 % 2 == 0){
            auxP++;
        } else {
            auxI++;
        }

        if(x3 % 2 == 0){
            auxP++;
        } else {
            auxI++;
        }

        if(x4 % 2 == 0){
            auxP++;
        } else {
            auxI++;
        }

        if(x5 % 2 == 0){
            auxP++;
        } else {
            auxI++;
        }

        System.out.println(auxP + " valor(es) par(es)");
        System.out.println(auxI + " valor(es) impar(es)");
        System.out.println(pos + " valor(es) positivo(s)");
        System.out.println(neg + " valor(es) negativo(s)");
    }
}
