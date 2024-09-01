import json

from time import sleep

# Verificação da entrada do menu e string do menu:
def menu():
    print('''      ----- MENU ------
1 - Dia Com o Menor Faturamento
2 - Dia Com o Maior Faturamento
3 - Dia Com Faturamento Maior que a Media
0 - Sair do Programa
        ''')
    entr = input('Digite a Opção Desejada: ')
    
    try:
        num_retorno = int(entr)
        return(num_retorno)
    except ValueError:
        return("Opção invalida")
    
# Variaveis...  
dados = []
dia_menor = 0
menor_lucro = 5000000
dia_maior = 0
maior_lucro = 0
media_mes = 0
dias_zerados = 0
total_dias = 30

# Abrindo Arquivo:
with open('faturamento.json','r') as fat:
        dados = json.load(fat)

# Preenchendo as variaveis com os valores:
for l in dados['faturamento']:

    if l['lucro_dia'] < menor_lucro and l['lucro_dia'] != 0:
        menor_lucro = l['lucro_dia']
        dia_menor = l['dia']
            
    if l['lucro_dia'] > maior_lucro and l['lucro_dia'] != 0:
        maior_lucro = l['lucro_dia']
        dia_maior = l['dia']
            
    if l['lucro_dia'] == 0:
        total_dias -= 1
            
    if l['lucro_dia'] != 0:
        media_mes += l['lucro_dia']
        
    
# Segunda definição de Varivaveis situacionais do Menu:
media = media_mes // total_dias
med_lucro_maior = []
dia_med_lucro_maior = []

for l_2 in dados['faturamento']:
    if l_2['lucro_dia'] >= media:
        acima_lu = l_2['lucro_dia']
        acima_dia = l_2['dia']
        med_lucro_maior.append(acima_lu)
        dia_med_lucro_maior.append(acima_dia)

range_dia = len(dia_med_lucro_maior)

#Menu: ///
while menu != 0:
    m_nu = menu()
    match m_nu:
    
        case 1:
            print('Dia Com o Menor Faturamento Foi:')
            print(f'Dia - {dia_menor}\nFaturamento - {menor_lucro} R$\n')
            sleep(3)    
            
        case 2:   
            print('Dia Com o Maior Faturamento Foi:')
            print(f'Dia: {dia_maior}\nFaturamento: {maior_lucro} R$\n')
            sleep(3)
            
        case 3:
            print(f'Foram {len(dia_med_lucro_maior)} Dias, Cujo o Lucro Foi Maior que a Média - {media} R$ :')    
            for j in range(0, range_dia):
                print (f'Dia - {dia_med_lucro_maior[0]} // Lucro - {med_lucro_maior[0]} R$')
                med_lucro_maior.pop(0)
                dia_med_lucro_maior.pop	(0)
            sleep(3)
        case 0:
            print('Saindo do Programa Obrigado!... ')
            menu = 0
        case _:
            print("Digite Uma Opção Válida...\n")
            sleep(3)
