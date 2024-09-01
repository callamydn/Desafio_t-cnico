texto = []
texto = (input('Digite o texto para vê-lo ao contrario: '))
novo_texto = []

for i in texto:
    novo = texto[::-1]
    novo_texto.append(novo)
print(novo_texto[0])    
