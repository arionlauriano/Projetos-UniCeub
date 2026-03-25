import sys
def inicializar ():
    # Lê 4 letras e converte em 23 boolenaos.
    while True:
        chave = input("Digite uma chave de 4 letras: ")
        if len(chave) == 4:
            break
        print("A chave precisa ter exatamente 4 letras.")

    registrador = []
    for letra in chave:
        # Converte a litra em binários de 8 bits
        binario = format(ord(letra), '08b')
        for bit in binario:
            registrador.append(bit == '1')

    return registrador

def rotacionar(registrador, tipo_polinomio):
    saida = registrador[0]
    # Aplicação do cálculo XOR dependendo do tipo do polinômio
    if not tipo_polinomio:
        novo_bit = saida ^ registrador[31] ^ registrador[6] ^ registrador[4] ^ registrador[2] ^ registrador[1]
    else:
        novo_bit = saida ^ registrador[31] ^ registrador[6] ^ registrador[5] ^ registrador[1]

    # Desloca os bits para a esquerda e insere o novo bit no final
    registrador.pop(0)
    registrador.append(novo_bit)

    return saida

def main():
    print("--- Inicializando os 3 Registradores ---")
    cabeça = inicializar()
    registrador0 = inicializar()
    registrador1 = inicializar()
    
    letra_binaria = ""

    print("\nGerando bluxo de texto (Precione Ctrl+C para aprar):")
    try:
        while True:
            bit0 = registrador0[0]
            bit1 = registrador1[0]

            if not rotacionar(cabeça, False):
                bit0 = rotacionar(registrador0, False)
            else:
                bit1 = rotacionar(registrador1, True)

            # XOR dos bits e acumula
            bit_final = bit0 ^ bit1
            letra_binaria += "1" if bit_final else "0"

            if len(letra_binaria) == 8:
                # Convedrte o binário de 8 bits em caractere e imprime
                char_saida = chr(int(letra_binaria, 2))
                sys.stdout.write(char_saida)
                sys.stdout.flush() # Força a saída instantânea
                letra_binaria = ""

    except KeyboardInterrupt:
        print("\nPrograma finalizado pelo usuário.")


if __name__ == "__main__":
    main()