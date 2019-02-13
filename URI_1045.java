import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
       float A, B, C, ord;

        Scanner input = new Scanner(System.in);

        A = input.nextFloat();
        B = input.nextFloat();
        C = input.nextFloat();

        float[] v = new float[3];
        v[0] = A;
        v[1] = B;
        v[2] = C;

        for(int i = 0; i < v.length; i++){
            for(int j = 0; j < v.length; j++){
                if(v[i] > v[j]){
                    ord = v[j];
                    v[j] = v[i];
                    v[i] = ord;
                }
            }
        }

        if(v[0] >= (v[1] + v[2])) {
            System.out.println("NAO FORMA TRIANGULO");
            } else if(((v[0] * v[0])) == ((v[1] * v[1]) + (v[2] * v[2]))) {
                System.out.println("TRIANGULO RETANGULO");
            } else if((v[0] * v[0]) > ((v[1] * v[1]) + (v[2] * v[2]))) {
                System.out.println("TRIANGULO OBTUSANGULO");
            } else if((v[0] * v[0]) < ((v[1] * v[1]) + (v[2] * v[2]))) {
                System.out.println("TRIANGULO ACUTANGULO");
            }


        if(v[0] == v[1] && v[0] == v[2] && v[1] == v[2]) {
                System.out.println("TRIANGULO EQUILATERO");
        } else if(v[0] == v[1] || v[0] == v[2] || v[2] == v[1]) {
            System.out.println("TRIANGULO ISOSCELES");
        }
    }
}
