#Listas e Variaveis
fib = [0,1]
lista = [0,1]
num = 0

# Definição de valor de entrada
entrada = int(input('''         Sequência de Fibonacci:
Digite um Número para saber se ele esta nessa sequência: '''))

# Variavel de controle
fib_igual = False

# Condição para Zero
if entrada == 0:
    fib_igual = True

# Criação da Tabela Fibo
for i in range(1, entrada + 2):
    num = lista[0] + lista[1]
    lista.append(num)
    lista.pop(0)
    fib.append(num)

# Quebrando Loop  
    if num == entrada:
        fib_igual = True
        break
    elif num > entrada:
        break

# Print Condicional da Varivel de controle
if fib_igual is True:
    print(f'O número digitado: {entrada}, pertence a Sequência de Fibonacci!')
if not fib_igual:
    print('O número digitado não pertence a Sequência de Fibonacci!')

# Print final
print(f'''Sequência Fibonacci:
{fib}''') 
  
