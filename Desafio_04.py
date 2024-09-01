import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)
soma = (sp + rj + mg + es + outros )


def media(estd):
    md = (estd * 100)/ soma
    return (md)

print(f'O Valor total da Distribuidora Foi:')
print(locale.format_string('%.2f R$', soma, grouping=True))

sp_m = media(sp)
print(f'\nSP Representa {sp_m:.2f} %')

rj_m = media(rj)
print(f'RJ Representa {rj_m:.2f} %')

mg_m = media(mg)
print(f'MG Representa {mg_m:.2f} %')

es_m = media(es)
print(f'ES Representa {es_m:.2f} %')

outros_m = media(outros)
print(f'OUTROS Representa {outros_m:.2f} %')




