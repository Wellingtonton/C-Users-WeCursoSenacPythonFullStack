# Solicita um número ao usuário. Caso digite algo inválido, como letras, o programa não vai quebrar.
try:
    numero = int(input("Digite um número: ")) # Aqui o código exibe uma mensagem e aguarda o usuário digitar um
 # valor. O int converte para um número inteiro.   
    print(f"Números pares de 1 até {numero}:\n") # Aqui o código informa até qual número ele vai listar os pares.
    
    # Loop for é para encontrar e imprimir números pares e interar de 1 até o número digitado pelo usuário; ele
 # verifica se o número atual (i) é par; se é par, o número é impresso.
    for i in range(1, numero + 1): # Cria uma repetição que percorrer os números de 1 até o número digitado.
        if i % 2 == 0:  # Aqui o código verifica se o número é par.
            print(i)

except ValueError: # Aqui acorre um erro, se o usuário não digitar um número inteiro válido. O códogo exibe uma
 # mensagem e não trava.  
    print("Por favor, digite um número inteiro válido.")

