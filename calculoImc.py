print('Olá! Digite os dados e eu irei calcular o seu IMC (Índice de massa corporal')

peso = float(input('Digite seu peso (em Kg): '))
altura = float(input('Digite sua altura (em metros): '))
imc = peso/(altura ** 2)
classificacao = 'classificacao'

if(imc<18.50):
    classificacao = 'Magreza'
elif(imc>=18.50 and imc<24.9):
    classificacao = 'Normal'
elif(imc>=24.9 and imc <30):
    classificacao = 'Sobrepeso'
else:
    classificacao = 'Obesidade'

print('O cálculo do seu IMC é: ', round(imc, 2), ', sua classificação é: ', classificacao)



