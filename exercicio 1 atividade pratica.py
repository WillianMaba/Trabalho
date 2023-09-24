print('Bem vindo a empresa do Willian de Lara Reginato Maba') #Identificador pessoal

valor_produto = float(input('Digite o valor do produto que deseja comprar: ')) #Foi utilizado o float devido à possibilidade do cliente escolher um número decimal.
quantidade_produto = int(input('Digite a quantidade desejada do produto: ')) #Foi utilizado o int pois não existe a possibilidade de um número decimal, apenas inteiros.
desconto_produto = 0



if quantidade_produto <= 9:
   desconto_produto = 0.00 #não possui desconto.
elif quantidade_produto >=10 and quantidade_produto < 99:
   desconto_produto = 0.05 #0,05 equivale a desconto de 5%.
elif quantidade_produto >=100 and quantidade_produto < 999:
   desconto_produto = 0.10 #0,10 equivale a desconto de 10%.
else:
   quantidade_produto > 1000
   desconto_produto = 0.15 #0,15 equivale a desconto de 15%.

total_sem_desconto = valor_produto * quantidade_produto
print('O valor do seu produto SEM desconto é de: R$ {:.2f}'.format(total_sem_desconto)) #Informa o valor final do produto sem o desconto.

total_com_desconto = total_sem_desconto - valor_produto * desconto_produto
print('O valor do seu produto COM desconto é de: R$ {:.2f}'.format(total_com_desconto)) #Informa o valor final do produto com o desconto, baseando-se no cálculo do valor final sem desconto - valor unitário do produto * a porcentagem do desconto.
print('O desconto aplicado foi de {}%'.format(desconto_produto)) #Utilizei para o cliente ter a informação do desconto que foi entregue a ele.

print('Obrigado pela preferência, volte sempre')
