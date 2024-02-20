print('[F]Fahrenheit\n[C]Celsius\n[K]Kelvin')
entrada = input('Escolha a unidade de entrada: ').upper()
saida = input('Escolha a unidade de saida: ')
temperatura = float(input('Digite a temperatura que deseja converter: '))
if entrada == 'C' and saida == 'F':
    solução = ((9/5) * temperatura) + 32
elif entrada == 'C' and saida == 'k':
    solução = entrada + 273.15
elif entrada == 'F' and saida == 'C':
    solução = (5/9) * (temperatura - 32)
elif entrada == 'F' and saida =='K':
    solução = ((5/9)*(temperatura - 32))+273.15
elif entrada == 'K' and saida == 'C':
    solução = temperatura - 273.15
elif entrada == 'K' and saida == 'F':
    solução = (9/5) * (temperatura - 273.15) + 32
elif entrada == saida:
    print('A entra e a sida são iguais!')
else:
    print('Sua escolha é inválida!!')
print('={}'.format(solução))