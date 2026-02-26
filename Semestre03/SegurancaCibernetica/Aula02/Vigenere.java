public class Vigenere {
    private static String encriptar(String texto, String chave) {
        String cifra = "";

        for (int i=0; i < texto.length(); i++) {
            int letraTexto = texto.charAt(i);
            int letraChave = chave.charAt(i% chave.length());
            int letraCifra = (letraTexto ^ letraChave);

            String temp = Integer.toHexString(0xFF & letraCifra);
            if (temp.length() == 1) temp = ("0" + temp);

            cifra += temp
        }

        return cifra;
    }

    private static String decriptar(String cifra, String chave) {
        String texto = "";

        for (int i = 0; i < cifra.length(); i+=2) {
            int letraCifra = Integer.parseInt(cifra.substring(i,i+2), 16);
            int letraChave = chave.charAt((i/2) % chave.length());
            int letraTexto = (letraCifra ^ letraChave);

            texto += ((char) letraTexto);
        }

        return texto;
    }
    public static void main(String[] args) {
        BufferedReader leitor = new BufferedReader(new InputStreamReader(System.in));
        String texto = "";
        String chave = "";
        String cifra = "";

        try {
            System.out.print("Digite o texto: "):
            texto = leitor.readLine();

            System.out.print("Digite a chave: ");
            chave = leitor.readLine();

            cifra = encriptar(texto, chave);
            System.out.println(cifra);

            System.out.print("Digite a cifra: ");
            cifra = leitor.readLine();

            System.out.print("Digite a chave: ");
            chave = leitor.readLine();

            texto = decriptar(cifra, chave);
            System.out.println(texto);
        } catch (Exception erro) {
            System.out.println("Fodeu!!!" + erro);
        }
    }
}