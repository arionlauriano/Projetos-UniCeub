public class LFSR {
    private static void inicializar(boolean[] registrador) {
        BufferedReader leitor = new BufferedReader(new InputStreamReader(System.in));

        String chave = "";

        try {
            System.out.print("Digite uma chave de 4 letras: ")
            chave = leitor.readLine();

            for (int i = 0 ; i < 4 ; i++) {
                int letra = chave.charAt(i);
                String binario = Integer.toBinaryString(letra);

                for (int j = 0 ; j < binario.length() ; j++) {
                    registrador[j + (8 * i)] = (binario.charAt(j) == '1')
                }
            }
        } catch (Exception erro) {
            System.out.println(erro);
        }
    }

    private static boolean rotacionar(boolean[] registrador, boolean tipo) {
        String retorno = registrador[0];
        String novoBit = retorno;

        if (! tipo) {
            novoBit = (novoBit ^ registrador[31] ^ registrador[6] ^ registrador[4] ^ registrador[2] ^ registrador[1] ^ registrador[0]);
        } else {
            novoBit = (novoBit ^ registrador[31] ^ registrador[6] ^ registrador[5] ^ registrador[1]);
        }

        for (int i = 0 ; i < 31 ; i++) {
            registrador[i] = registrador[i + 1];
        }
        registrador[31] = novoBit;

        return retorno;
    }
    public static void main(String[] args) {
        boolean[] cabeca = new boolean[32];
        boolean[] registrador0 = new boolean[32];
        boolean[] registrador1 = new boolean[32];
        String letra = "";

        inicializar(cabeca);
        inicializar(registrador0);
        inicializar(registrador1);

        while (true) {
            boolean bit0 = registrador0[0];
            boolean bit1 = registrador1[0];

            if (! rotacionar(cabeca, false)) {
                bit0 = rotacionar(registrador0, false);
            } else {
                bit1 = rotacionar(registrador1, true);
            }

            letra += ((bit0 ^ bit1) ? "1" : "0");
            if (letra.length() == 8) {
                System.out.print((char) Integer.parseInt(letra, 2));
                letra = "";
            }
        }
    }
}