def  dimensoesObjeto(): #função utilizada para determinar a dimensão do objeto, com base nas opções do cliente, e retornando seu valor escolhido.
    print('|-----dimensões(cm³)-------|valor(R$)--|')
    print('|----volume < 1000---------|--10-------|')
    print('|--1000 <= volume < 10000--|--20-------|')
    print('|--10000 <= volume < 30000-|--30-------|')
    print('|--30000 <= volume < 100000|--50-------|')
    print('|--volume >=100000---------|-----------|')
    while True: #enquanto a função for correta ela continua.
        try: #utilizado para evitar que os erros ocorram caso o cliente digite algum valor não numérico, retornando assim para o começo da função.
            global volumeE #utilizado para que a função possa ser usada fora da "def".
            alturaE = int(input('Digite a altura da encomenda (cm): ')) #foi utilizado o "int" para que não seja possível digitar valores decimais.
            comprimentoE = int(input('Digite o comprimento da encomenda (cm): ')) #foi utilizado o "int" para que não seja possível digitar valores decimais.
            larguraE = int(input('Digite a largura da encomenda (cm): ')) #foi utilizado o "int" para que não seja possível digitar valores decimais.
            volumeE = alturaE * larguraE * comprimentoE #Calculo para que seja possível ter o valor final da dimensão.
            print('Valor final da dimensão (cm³): {:.2f}'.format(volumeE))  #utilizado para que o cliente saiba qual foi o valor final escolhido.

            if volumeE< 1000: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do if.
                return 10 #multiplicador do volumeE

            elif volumeE <= 1000  or volumeE < 10000: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do elif.
                return 20 #multiplicador do volumeE

            elif volumeE <= 10000 or volumeE < 30000: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do elif.
                return 30 #multiplicador do volumeE

            elif volumeE <= 30000  or volumeE < 100000: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do elif.
                return 50 #multiplicador do volumeE

            else: volumeE >= 100000 #caso escolha um valor acima do descrito ou não existente, recebe uma mensagem e retorna ao inicio da função.
            print('Digite apenas valores aceitos pela empresa! não aceitamos mais que a dimensão total de 100000')

        except ValueError: #utilizado para quando o cliente colocar valor não numérico, fazendo assim voltar ao try no começo da função.
            print('Digite apenas valores aceitos pela empresa! não aceitamos valores não númericos!')
            continue #volta para o inicio da função.

def pesoObjeto(): #função utilizada para determinar o peso do objeto, com base nas opções do cliente, e retornando seu valor escolhido.
    print('|------peso(kg)------|---multiplicador------|')
    print('|----peso <= 0.1-----|---------1------------|')
    print('|----0.1 <= peso < 1-|--------1.5-----------|')
    print('|----1 <= peso <10---|---------2------------|')
    print('|----10 <= peso < 30-|---------3------------|')
    print('|----peso>=30--------|----Não é aceito------|')
    while True: #enquanto a função for correta ela continua.
        try: #utilizado para evitar que os erros ocorram caso o cliente digite algum valor não numérico, retornando assim para o começo da função.
            global pesoE #utilizado para que a função possa ser usada fora da "def".
            pesoE = float(input('Digite o peso desejado (kg): ')) #foi utilizado o "float" para que seja possível digitar valores decimais.
            print('Valor final do peso: {}'.format(pesoE)) #utilizado para que o cliente saiba qual foi o valor final escolhido.

            if pesoE <= 0.1: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do if.
                return 1 #multiplicador do pesoE

            elif 0.1 <= pesoE < 1: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do elif.
                return 1.5 #multiplicador do pesoE

            elif 1 <= pesoE < 10: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do elif.
                return 2 #multiplicador do pesoE

            elif 10<= pesoE < 30: #Caso o valor esteja dentro do escolhido, ele retornará o multiplicador do elif.
                return  3 #multiplicador do pesoE

            else: 30 <= pesoE #caso escolha um valor acima do descrito ou não existente, recebe uma mensagem e retorna ao inicio da função.
            print('Peso Inválido. Digite apenas pesagem trabalhada pela empresa!')
        except ValueError: #utilizado para quando o cliente colocar valor não numérico, fazendo assim voltar ao try no começo da função.
            print('Digite apenas valores indicados, não aceitamos valores não númericos!')
            continue #volta para o inicio da função.

def rotaObjeto(): #função utilizada para determinar a rota a ser percorrida pelo objeto, com base nas opções do cliente.
    print('---rota---')
    while True: #enquanto a função for correta ela continua.
        global rotaE #utilizado para que a função possa ser usada fora da "def".
        rotaE = input('Escolha a opção de viagem a ser percorrida \n +'
                            'RS-De Rio de Janeiro até São Paulo \n +'
                            'SR-De São Paulo até Rio de Janeiro \n +'
                            'PS-De Paraná até São Paulo \n +'
                            'SP-De São Paulo até Paraná \n +'
                            'PR-De Paraná até Rio de Janeiro \n +'
                            'RP-De Rio de Janeiro até Paraná\n +'
                            '>>')
        print('Destino escolhido:{}'.format(rotaE)) #utilizado para que o cliente saiba qual foi o destino final escolhido.
        if rotaE.upper() == 'RS': #Caso o destino esteja dentro do escolhido, ele retornará o multiplicador do elif.
            return  1 #multiplicador da rotaE

        elif rotaE.upper() == 'SR': #Caso o destino esteja dentro do escolhido, ele retornará o multiplicador do elif.
            return  1 #multiplicador da rotaE

        elif rotaE.upper() == 'PS': #Caso o destino esteja dentro do escolhido, ele retornará o multiplicador do elif.
            return  1.2 #multiplicador da rotaE

        elif rotaE.upper() == 'SP': #Caso o destino esteja dentro do escolhido, ele retornará o multiplicador do elif.
            return  1.2 #multiplicador da rotaE

        elif rotaE.upper() == 'PR': #Caso o destino esteja dentro do escolhido, ele retornará o multiplicador do elif.
            return  1.5 #multiplicador da rotaE

        elif rotaE.upper() == 'RP': #Caso o destino esteja dentro do escolhido, ele retornará o multiplicador do elif.
            return  1.5 #multiplicador da rotaE

        else: #caso escolha uma opção não existente, recebe uma mensagem e retorna ao inicio da função.
            print('Digite apenas o destino indicado, não aceitamos valores númericos ou outras opções!')
            continue #volta para o inicio da função.

        #Foi utilizado o "uper()" para que o cliente consiga escolher a opção independente se for letra minúscula ou maiúscula.

#programa principal
print('Bem vindo à empresa de logística do Willian de Lara Reginato Maba') #Identificador pessoal

volume = dimensoesObjeto() #variável utilizada para a função poder ser mostrada no programa principal.
peso = pesoObjeto() #variável utilizada para a função poder ser mostrada no programa principal.
rota = rotaObjeto() #variável utilizada para a função poder ser mostrada no programa principal.
total = volume * peso * rota #variável utilizada para que seja possível ser feito o calculo final da compra.

print('Total a pagar: R${:.2f}(dimensão:{} * peso:{} * rota:{})'.format(total,volume,peso,rota)) #variável utilizada para que seja possível mostrar ao cliente o valor final de sua compra e o multiplicador de cada item escolhido.

