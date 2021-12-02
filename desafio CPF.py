'''elabore um sistema para calcular os dois últimos dígitos de um CPF
exemplo CPF válido: 16899535009'''
cpf = (input('Digite seu CPF: '))
i1 = 10
i2 = 11
soma1 = 0
soma2 = 0

for digito in cpf:
    soma1 = soma1 + (int(digito) * int(i1))
    i1 -= 1
    if i1 < 2:
        break

for digito in cpf:
    soma2 = soma2 + (int(digito) * int(i2))
    i2 -= 1
    if i2 < 2:
        break
print(f'soma1: {soma1}, soma2: {soma2}')

frase = cpf
tamanho_frase = len(frase) #iterar: passar por cada elemento de toda a string, frase
print(f'numero elementos: {tamanho_frase}')
contador = 0
novo_cpf = ''

while contador < 9:
    novo_cpf += frase[contador]
    contador += 1
    formula = 11 - (soma1 % 11)
    formula2 = 11 - (soma2 % 11)
    if formula > 9:
        formula = 0
    if formula2 > 9:
        formula2 = 0
    if contador >= 9:
        novo_digito = str(formula)
        novo_cpf += novo_digito
        novo_digito = str(formula2)
        novo_cpf += novo_digito

print(f'últimos dígitos têm que ser: {formula}, {formula2}')
print(novo_cpf)
#APÊNDICE PARA EVITAR sequências repetidas. Ex.: 11111111111, 22222222222, 99999999999
sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

if cpf == novo_cpf and not sequencia:
    print("CPF VÁLIDO")
else:
    print("CPF INVÁLIDO")

