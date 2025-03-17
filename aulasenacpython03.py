try: # Esse código solicita um número ao usuário. Caso digite algo inválido, como letras, o programa não vai
 # quebrar.    
    numero = int(input("Digite um número para calcular o fatorial: ")) # Aqui o código exibe uma mensagem e 
 # aguarda o usuário digitaa um valor. O int converte para um número inteiro.
    if numero < 0: # Aqui o código verifica se o número é negativo! Se for negativo, ele mostra uma mensagem que
 # não existe fatorial de números negativos.       
        print("Não existe fatorial de número negativo.")
    else:     # Número positivo ou zero, o programa cria 2 váriveis.
        fatorial = 1  # Onde vamos guarda o resultado.
        contador = numero  # inicia uma contagem regressiva.
        
        while contador > 0: # Aqui o loop cálcula o fatorial.
            fatorial *= contador  # Multiplica o fatorial pelo número atual
            contador -= 1
        
        print(f"O fatorial de {numero} é {fatorial}.") # Depois o programa mostra o resultado na tela.

except ValueError: # Aqui ocorre um erro, se o usuário não digitar um número inteiro válido. O programa exibe
 # uma mensagem de erro e não trava.     
    print("Por favor, digite um número inteiro válido.")
