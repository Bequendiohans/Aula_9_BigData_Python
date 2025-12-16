
def imc_alunos(a, p):
    imc = p / (a**2)
    print(f'Seu IMC é igual a: {imc:.2f}')
    return imc


altura = float(input('Informe sua altura em metros: '))
peso = float(input('informe seu peso em kg: '))

massa_corpo = imc_alunos(altura, peso)

match massa_corpo:
    case m if m <= 16.9:
        print('Muito abaixo do peso')
    case m if m <= 18.4:
        print('Abaixo do peso')
    case m if m <= 24.9:
        print('Peso normal')
    case m if m <= 29.9:
        print('Acima do peso')
    case m if m <= 34.9:
        print('Obesidade grau I')
    case m if m <= 40:
        print('Obesidade grau II')
    case m if m > 40:
        print('Obesidade grau III')
    case _:
        print('Dados Inválidos')
