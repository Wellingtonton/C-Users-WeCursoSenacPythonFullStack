try:
    while True:  # Essa função é para simular o comportamento do while.( Loop infinito)
        numero = int(input("Digite um número maior que 10: ")) # O código pede um número e o transforma em 
 # inteiro.        
        if numero > 10: # Se o n´mero for maior que 10, ele imprime.
            print(f"Você digitou um número válido: {numero}")
            break  # Sai do loop se o número for válido.
        else:
            print("Número inválido! Tente novamente.") # Se o número for menor ou igual a 10, le mostra.
except ValueError:  # Aqui acorre um erro, se o usuário não digitar um número inteiro válido. O códogo exibe uma
 # mensagem e não trava.
    print("Por favor, digite um número inteiro válido.")