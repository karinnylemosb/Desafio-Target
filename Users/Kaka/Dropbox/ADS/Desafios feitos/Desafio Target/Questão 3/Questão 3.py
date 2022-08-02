import json
f = open ('Questão 3\dados.json')
dados = json.load(f)


vetor = 0
maior = 0
menor = 0
soma = 0
media = 0


for faturamentoDia in dados:


    if (faturamentoDia['valor']):
        vetor = faturamentoDia['valor']

        # Maior faturamento
        if (vetor > maior):
            maior = vetor

        #Menor faturamento
        if(menor == 0):
            menor = vetor
        elif (vetor < menor):
            menor = vetor

        # Somando os valores de faturamento
        soma += faturamentoDia['valor']

print('O maior valor de faturamento do mês foi: R$ ' + str(maior) + '.')
print('O menor valor de faturamento do mês foi: R$ ' + str(menor) + '.')

