// vamo tentar em java agr

import java.util.Scanner;
public class Cometa {
    public static void main(String[] args) {
        Scanner ano = new Scanner(System.in);
        int Ano = ano.nextInt();
        int jp = (Ano - 1986) / 76; // todas as vezes que o cometa passou desde 1986
        int resultado = 1986 + (jp + 1) * 76; // quando o cometa vai passar de novo. Aquele um é porque sempre pegar a proxima passagem
        System.out.println(resultado);
    }
}