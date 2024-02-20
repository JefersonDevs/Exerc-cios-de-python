palavra = input('Escolha a palavra para verificar :').replace(' ', '')
jun = ''.join(reversed(palavra))
if palavra == jun:
    print('Essa palavra é um polímedro')
else :
    print('Essa palavra não é um polímedro')
