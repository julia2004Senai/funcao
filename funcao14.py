def verificar_palindromo(texto):
    tetxo = texto.lower().replace(" ", "")
    return tetxo == texto[::-1]

texto = "Socorram-me, subi no ônibus em marrocos"
if verificar_palindromo(texto):
    print(texto, "é um palíndromo")
else:
    print(texto, "não é um palíndromo")