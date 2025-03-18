try: # Aqui começa um bloco de código, que pode gerar um erro! (O try é usado para lidar com erros no seu código.  
 # Ele tenta executar um bloco de código, e se ocorrer um erro, o except entra em ação para tratar esse erro!)
    numero = int(input("Digite um número para ver a tabuada: ")) # Mostra a mensagem para o usuário digitar o
 # valor.(O int converte a entrada para um número inteiro.) 
    print(f"\nTabuada do {numero}:\n") # exibi um título antes de mostrar os cálculos.
    for i in range(1, 11): # Aquio código cria um loop que vai de 1 até 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}") # Aqui o código exibi a multiplicação do número digitado pelo
 # usuário por cada valor de i        
except ValueError: # Se a pessoa digitar algo inválido, o código não trava. E exibe uma mensagem de erro.
    print("Por favor, digite um número inteiro válido!")
