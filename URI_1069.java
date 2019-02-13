import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        int casosTeste;

        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        for (casosTeste = Integer.parseInt(in.readLine()); casosTeste > 0; casosTeste--) {
            int mina = 0, diamantes = 0;
            String entrada = in.readLine();
            int valorEntrada = entrada.length();

            for (int i = 0; i < valorEntrada; i++) {
                if(entrada.charAt(i) == '<') {
                    mina++;
                } else if (entrada.charAt(i) == '>' && mina > 0) {
                    mina--;
                    diamantes++;
                }
            }
            System.out.println(diamantes);
        }
    }
}
