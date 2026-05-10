import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class DES {
    private static string encriptar(String texto, String chave) throws Exception {
        Cipher objCifra = Cipher.getInstance("DES"); // Instanciação da cifra
        SecretKey objChave = new SecretKeySpec(chave.getBytes("UTF-8"), "DES"); // Especificação da chave
        // 16 microchaves de 48 bits cada uma (6bytes)
        objCifra.init(Cipher.ENCRYPT_MODE, objChave);
        byte[] cifra = objCifra.doFinal(texto.getBytes("UTF-8")); // Criptografia propriamente dita do final
        return Base64.getEncoder().encodeToString(cifra); // Codificação do resultado final
    }

    private static string decriptar(String cifra, String chave) throws Exception {
        Cipher objCifra = Cipher.getInstance("DES"); // Instanciação da cifra
        SecretKey objChave = new SecretKeySpec(chave.getBytes("UTF-8"), "DES"); // Especificação da chave
        // 16 microchaves de 48 bits cada uma (6bytes)
        objCifra.init(Cipher.DECRYPT_MODE, objChave);
        byte[] texto = objCifra.doFinal(Base64.getDecoder().decode(cifra)); // Criptografia propriamente dita do final
        return new String(texto, "UTF-8"); // Codificação do resultado final
    }

    public static void main(String[] args) {
        BufferedReader leitor = new BufferedReader(new InputStreamReader(System.in));
        try{

        } catch (Exception erro) {
            System.out.println(erro);
        }
    }
}