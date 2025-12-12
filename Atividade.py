# def excesso(p):
#     vm = (p-100)*4
#     return vm


# peso = float(input('Informe quantos quilos foram pegos no dia: '))
# if peso > 100:
#     valor_multa = excesso(peso)
#     print(f'Foi detectado excesso de peso em sua pesca! \n O valor da multa é de: R${valor_multa:.2f}')
# else:
#     print(f'Tudo certo com seu pescado. Tenho um bom dia!')

#CORREÇÃO - OUTRO MÉTO POSSÍVEL
    
def calcula_multa(excesso):
    multa = excesso * MULTA_KG
    return multa

MULTA_KG = 4.00
QUILOS_PERMITIDOS = 100.0

peso_pescado = float(input('Informe o peso (kg): '))

if peso_pescado > QUILOS_PERMITIDOS:
    excedente = peso_pescado - QUILOS_PERMITIDOS
    vl_multa = calcula_multa(excedente)
    print(f'O valor da multa é: R${vl_multa}')
else:
    print('Não há multa a pagar.')
print('Programa encerrado.')