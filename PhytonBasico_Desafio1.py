
# ExercíciosExtrasdePython

# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneca a soma desses três argumentos.

# def soma_argumentos():
#     try:
#         argumento_1 = int(input('Digite o primeiro argumento:'))
#         argumento_2 = int(input('Digite o segundo argumento:'))
#         argumento_3 = int(input('Digite o terceiro argumento:'))
#     except ValueError as e:
#         print(f'O Tipo de dado informado está incorreto \n Detalhes {e}')
# #       return
    
#     soma = (argumento_1 + argumento_2 + argumento_3)
#     return soma

# soma_argumentos = soma_argumentos()

# print(f'A soma dos argumentos é {soma_argumentos}')

## Tem essa segunda versão muito boa também

# def soma_argumentos(arg1, arg2, arg3):
#     try:
#         soma = arg1 + arg2 + arg3
#         return soma
#     except ValueError as e:
#         print(f'O Tipo de dado informado está incorreto \n Detalhes {e}')
#         return None  # Retorna None em caso de erro

# # Solicita os argumentos ao usuário
# try:
#     argumento_1 = int(input('Digite o primeiro argumento: '))
#     argumento_2 = int(input('Digite o segundo argumento: '))
#     argumento_3 = int(input('Digite o terceiro argumento: '))
# except ValueError as e:
#     print(f'O Tipo de dado informado está incorreto \n Detalhes {e}')
#     argumento_1 = argumento_2 = argumento_3 = None  # Define como None em caso de erro

# # Chama a função e atribui o resultado a uma variável
# soma = soma_argumentos(argumento_1, argumento_2, argumento_3)

# # Verifica se a soma foi calculada corretamente
# if soma is not None:
#     print(f'A soma dos argumentos é {soma}')
# else:
#     print('Não foi possível calcular a soma devido a dados incorretos.')

# 2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Porexemplo:127->721

# def inverter_numero(numero):
#     # Converte o número para uma string, inverte a ordem dos caracteres e converte de volta para um número inteiro
#     numero_invertido = int(str(numero)[::-1])
#     return numero_invertido

# # Executando
# try:
#     numero = int(input('Digite um númeto: '))
#     numero_invertido = inverter_numero(numero)
#     print(f"O reverso de {numero} é {numero_invertido}")
# except ValueError as e:
#     print(f'O Tipo de dado informado está incorreto \n Detalhes {e}')

# 3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ouv ice-versa.
# Para cada opção, crie uma função.
# Plus:Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversã ocorreta
    
# def celsius_para_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_para_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# def menu():
#     print("Selecione uma opção:")
#     print("1. Converter de Celsius para Fahrenheit")
#     print("2. Converter de Fahrenheit para Celsius")
#     print("3. Sair")

#     opcao = input("Digite o número da opção desejada: ")
#     return opcao

# while True:
#     opcao = menu()

#     if opcao == '1':
#         celsius = float(input("Digite a temperatura em graus Celsius: "))
#         fahrenheit = celsius_para_fahrenheit(celsius)
#         print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F\n")
#     elif opcao == '2':
#         fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
#         celsius = fahrenheit_para_celsius(fahrenheit)
#         print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C\n")
#     elif opcao == '3':
#         print("Encerrando o programa.")
#         break
#     else:
#         print("Opção inválida. Por favor, digite 1, 2 ou 3.\n")


# 4. Crie um programa que leia quanto dinheiro uma pessoa temn a carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
# Considere a tabela de conversão abaixo: 
# Dólar Americano: R$4,91
# Peso Argentino: R$0,02
# Dólar Australiano :R$3,18
# Dólar Canadense: R$3,64
# Franco Suiço: R$0,42
# Euro: R$5,36
# Libra esterlina: R$6,21

# # calcula quanto da moeda estrangeira uma pessoa poderia comprar com base no dinheiro que ela tem na carteira e na taxa de conversão.   
# def calcular_valor_em_moeda(dinheiro, taxa): # 
#     return dinheiro / taxa

# # solicita ao usuário quanto dinheiro ele tem na carteira e, em seguida, itera sobre o dicionário de moedas, 
# # calculando e imprimindo quanto da moeda estrangeira ele poderia comprar com base nas taxas de conversão fornecidas.
# def main():
#     dinheiro_na_carteira = float(input("Digite quanto dinheiro você tem na carteira (em reais): "))

#     moedas = {
#         "Dólar Americano": 4.91,
#         "Peso Argentino": 0.02,
#         "Dólar Australiano": 3.18,
#         "Dólar Canadense": 3.64,
#         "Franco Suíço": 0.42,
#         "Euro": 5.36,
#         "Libra Esterlina": 6.21
#     }

#     print("Com", dinheiro_na_carteira, "reais, você poderia comprar:")
#     for moeda, taxa in moedas.items():
#         valor_em_moeda = calcular_valor_em_moeda(dinheiro_na_carteira, taxa)
#         print(f"{valor_em_moeda:.2f} {moeda}")

# # Quando um arquivo Python é executado como um programa principal), a variável especial __name__ é definida como "__main__". 
# # Isso significa que o código dentro do bloco if __name__ == "__main__": será executado. Caso contrário se ele for importado como
# # múdulo a variável é o nome do módulo e logo não será executado
        
# if __name__ == "__main__":
#     main()

# # 5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na 
# # string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

# def contar_vogais(frase):
#     # Define uma lista com as vogais
#     vogais = 'aeiouAEIOU'
#     # Inicializa o contador de vogais
#     total_vogais = 0
#     # Percorre cada caractere na frase
#     for caractere in frase:
#         # Verifica se o caractere é uma vogal
#         if caractere in vogais:
#             # Se sim, incrementa o contador de vogais
#             total_vogais += 1
#     # Retorna o total de vogais encontradas na frase
#     return total_vogais

# # Solicita ao usuário inserir uma frase
# frase = input("Digite uma frase: ")

# # Chama a função contar_vogais com a frase inserida pelo usuário e imprime o resultado
# print("Número de vogais na frase:", contar_vogais(frase))


