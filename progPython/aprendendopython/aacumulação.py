numero = int(input("Digite um número inteiro: "))

# Inicializa a variável acumuladora
resultado = 0

# Acumulação condicional
if numero > 10:
    resultado += 10  # Adiciona 10 se o número for maior que 10
elif numero > 5:
    resultado += 5  # Adiciona 5 se o número for maior que 5
else:
    resultado += 1  # Adiciona 1 para qualquer outro valor

print(f"O resultado acumulado é: {resultado}")