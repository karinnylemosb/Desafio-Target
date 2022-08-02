# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.IMPORTANTE:Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código#

numero1 = int(0)
numero2 = int(1)
numero3 = int(0)


print("Vamos saber se o numero digitado pertence a Sequência de Fibonacci.")


numDigitado = int(input("Digite um número:"))

# Calculando a sequência com base no número informado
while numDigitado > numero3:
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3

# Caso o número digitado seja igual ao número gerado na sequência:
if numDigitado == numero3:
    print("O número " + str(numDigitado) + " pertence a Sequência de Fibonacci.")
else:
    print("O número não pertence a Sequência de Fibonacci.")
   
# 0 e 1: 
if numDigitado == 0 | numDigitado == 1:
    print("O número " + str(numDigitado) + " está na sequência de Fibonacci.")