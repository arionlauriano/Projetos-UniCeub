def vigenere_encript(texto, chave):
    cifra = ""
    for i in range(len(texto)):
        letra_texto = ord(texto[i])
        letra_chave = ord(chave[i % len(chave)])

        letra_cifra = letra_texto ^ letra_chave

        temp = hex(letra_cifra)[2:].zfill(2)
        cifra += temp

    return cifra

def vigenere_decript(cifra, chave):
    texto = ""
    for i in range(0, len(cifra), 2):
        par_hex = cifra[i:i+2]
        letra_cifra = int(par_hex, 16)

        letra_chave = ord(chave[(i // 2) % len(chave)])

        letra_texto = chr(letra_cifra ^ letra_chave)
        texto += letra_texto

    return texto

if __name__ == "__main__":
    cifra = input("Digite o texto a ser encriptado: ")
    chave = input("Digite a chave de encriptação: ")

    texto_decriptado = vigenere_decript(cifra, chave)
    print("Texto decriptado:", texto_decriptado)