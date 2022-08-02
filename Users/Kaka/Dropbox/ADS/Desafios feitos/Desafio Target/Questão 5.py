

palavra = str(input("Digite uma palavra:"))
caracteres = []
palavraInvertida = ''

for letra in palavra:
    caracteres.append(letra)

tamanho = len(caracteres) - 1

while tamanho >= 0:
    palavraInvertida += (caracteres[tamanho])
    tamanho -= 1

print("A palavra invertida fica: ")
print(palavraInvertida)