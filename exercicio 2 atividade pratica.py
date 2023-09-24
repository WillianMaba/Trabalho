print('Bem vindo à lanchonete do Willian de Lara Reginato Maba') #Identificador pessoal
print('-----------------Cardápio-------------------')
print('| Código  |      Descrição       |valor(R$)|')
print('|   100   |   Cachorro-Quente    | 9,00    |')
print('|   101   | Cachorro-Quente Duplo| 11,00   |')
print('|   102   |       X-Egg          | 12,00   |')
print('|   103   |       X-Salada       | 12,00   |')
print('|   104   |       X-Bacon        | 14,00   |')
print('|   105   |       X-Tudo         | 17,00   |')
print('|   200   | Refrigerante Lata    | 5,00    |')
print('|   201   |      Chá Gelado      | 4,00    |')

Total = 0 #variável utilizada para efetuar os cálculos do valor final da compra!
while True:
    codigo = input('Entre com o código do produto desejado: ') #Variável utilizada para o cliente escolher o produto conforme o código descrito no cardápio!
    if codigo != '100' and codigo != '101'  and codigo != '102'  and codigo != '103'  and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201' :
      print('Código Inválido, por favor digite o código corretamente!')
      continue #Caso o cliente digite algum caractere diferente dos códigos presentes no cardápio, a ação fará ele voltar ao inicio do programa para uma nova tentativa!

    elif codigo == '100': #variável utilizada para o cliente escolher apenas o produto Cachorro-Quente do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um Cachorro-Quente pelo valor de R$9,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 9.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '101':#variável utilizada para o cliente escolher apenas o produto Cachorro-Quente Duplo do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um Cachorro-Quente Duplo pelo valor de R$11,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 11.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '102':#variável utilizada para o cliente escolher apenas o produto X-Egg do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um X-Egg pelo valor de R$12,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 12.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '103':#variável utilizada para o cliente escolher apenas o produto X-Salada do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um X-Salada pelo valor de R$12,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 12.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '104':#variável utilizada para o cliente escolher apenas o produto X-Bacon do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um X-Bacon pelo valor de R$14,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 14.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '105':#variável utilizada para o cliente escolher apenas o produto X-Tudo do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um X-Tudo pelo valor de R$17,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 17.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '200':#variável utilizada para o cliente escolher apenas o produto Refrigerante Lata do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um Refrigerante Lata pelo valor de R$5,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 5.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    elif codigo == '201':#variável utilizada para o cliente escolher apenas o produto Chá Gelado do cardápio, e assim mostrar também o valor do produto!
        print('Você escolheu um Chá Gelado pelo valor de R$4,00!') #print para que o cliente saiba o que escolheu e não compre algo por engano!
        Total = Total + 4.00 #variável utilizada para que no final da compra o cliente saiba o valor gasto!

    adicionar_pedido = input('Deseja adicionar mais algum pedido à sua compra?(S/Digite qualquer outra tecla para sair):') #Variável escolhida para que o cliente possa decidir se vai ou não comprar mais produtos, assim não ficando num looping infinito!
    adicionar_pedido = adicionar_pedido.upper() #variável utilizada para que independente se o cliente utilizar letra minúscula ou maiúscula, a opção dele será válida, assim facilitando tanto o codigo quanto a vida do cliente!
    if adicionar_pedido == 'S':
        continue #caso ele opte pela opção S, o programa voltará ao inicio para que o cliente continue suas comprar!

    else:
        print('Valor total da compra: R${:.2f}'.format(Total)) #valor final da compra com todos os valores somados!
        print('Obrigado pela preferência, boa refeição!') #agradecimento ao cliente pela compra!
        break #encerra o programa ao final da compra, evitando que ele fique preso no looping de compra!