texto = input("Digite o que quer criptografar: ")
result = ""

for char in texto:
    if 'A' <= char <= 'Z':
        cifra = ((ord(char) - ord('A')) + 13) % 26 + ord('A')
        result += chr(cifra)
    elif 'a' <= char <= 'z':
        cifra = ((ord(char) - ord('a')) + 13) % 26 + ord('a')
        result += chr(cifra)
    else:
        result += char

print(result)