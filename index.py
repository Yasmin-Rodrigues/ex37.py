preço =float(input('Qual o valor do produto?'))
pg =int(input('Qual será a forma de pagamento? Digite:\n[1] Dinheiro/cheque com 10% de desconto \n[2] Cartão à vista com 5% de desconto\n[3] 2x no cartão com preço normal\n[4] 3x ou mais no cartão com 20% de juros\033[32m'))
desconto1 = preço *0.1
desconto2 = preço *0.05
juros = preço * 0.2
if pg == 1:
    print(f'O valor a ser pago é: R${preço - desconto1}')
elif pg ==2:
    print(f'O valor a ser pago é: R${preço - desconto2}')
elif pg ==3:
    print(f'O valor a ser pago é: R${preço}')
else:
    print(f'O valor a ser pago é: R${preço + juros}')