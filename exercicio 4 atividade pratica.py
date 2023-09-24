listar_produto = [] #Utilizado para criar a lista.
codigo_produto = 0 #Contador utilizado para que seja possível identificar o código dos produtos.

def cadastrarPeca(codigo): #utilizado para criar o código do cadastro das peças, e poder chamá-lo no programa principal.
    print('Seja bem vindo ao menu de cadastro!')
    print('código do produto: {}'.format(codigo)) #usado para o cliente saber qual o código que ele escolheu, e assim não houver engano.
    nome = input('Digite o nome da peça que deseja cadastrar: ') #utilizado para o cliente inserir os dados da sua peça.
    fabricante = input('Digite o nome do fabricante da peça à ser cadastrada: ') #utilizado para o cliente inserir os dados da sua peça.
    valor = int(input('Digite o valor (R$) da peça que está sendo cadastrada: ')) #utilizado para o cliente inserir os dados da sua peça, também foi utilizado "int" para que ele use números inteiros.
    dicionario_produto = {'codigo':      codigo,  #Usado para criar o dicionário do código, e assim poder incluir as peças na lista.
                          'nome':        nome,
                          'fabricante':  fabricante,
                          'valor':       valor}
    listar_produto.append(dicionario_produto.copy()) #utilizado para inserir o dicionário na lista e assim poder ter acesso a todos os dados.
def consultarPeca(): #utilizado para criar o código de consulta as peças, e poder chamá-lo no programa principal.
    print('Seja bem vindo ao menu de consulta!')
    while True:
        consulta_cliente = input('Selecione a opção desejada para consulta:\n' #opções para o cliente escolher
                                 '1-Consultar Todas as peças:\n'
                                 '2-Consultar peças pelo código\n'
                                 '3-Consultar peças pelo seu fabricante\n'
                                 '4-Retornar ao menu inicial\n'
                                 '>>')
        if consulta_cliente == '1': #caso o cliente escolha essa opção irá levá-lo a todos os dados existentes.
            print('Consultar todos os itens selecionado:')
            for pecas in listar_produto: #"for" foi utilizado para que possamos puxar os itens contidos na lista.
                print('__________') #utilizado para separar as peças, facilitando a visualização do cliente.
                for key, value in pecas.items(): #utilizado para que o programa puxe os itens selecionados(todos).
                    print('{}: {}'.format(key,value))
            print('__________')

        elif consulta_cliente == '2': #caso o cliente escolha essa opção irá leva-lo a todos os dados existentes apenas do código escolhido.
            print('Consultar itens por código selecionado!')
            codigo_desejado = int(input('Digite o código do produto que está procurando:')) #foi utilizado o "int" para que o cliente so utilize números inteiros.
            for codigo in listar_produto: #"for" foi utilizado para que possamos puxar os itens contidos na lista.
                print('__________') #utilizado para separar as peças, facilitando a visualização do cliente.
                if codigo['codigo'] == codigo_desejado: #utilizado para que o programa puxe apenas os itens selecionados pelo código.
                    for key, value in codigo.items():
                        print('{}: {}'.format(key,value))
            print('__________')

        elif consulta_cliente == '3': #caso o cliente escolha essa opção irá levá-lo a todos os dados existentes apenas do fabricante escolhido.
            print('Consultar itens pelo fabricante selecionado!')
            codigo_desejado = input('Digite o nome do fabricante da sua peça:')
            for fabricante in listar_produto: #"for" foi utilizado para que possamos puxar os itens contidos na lista.
                print('__________') #utilizado para separar as peças, facilitando a visualização do cliente.
                if fabricante['fabricante'] == codigo_desejado: #utilizado para que o programa puxe apenas os itens selecionados pelo fabricante.
                    for key, value in fabricante.items():
                        print('{}: {}'.format(key,value))
            print('__________')

        elif consulta_cliente == '4': #caso o cliente escolha essa opção ele retorna ao menu inicial do programa principal.
            return
            print('opção retornar ao menu selecionado!')


        else: #caso o cliente escolha uma opção não existente, isso ira levá-lo ele ao inicio da "def consultarPeca()".
            print('Opção não existente, tente novamente!')
            continue
def removerPeca(): #utilizado para criar o código de remover a peça e poder chamá-lo no programa principal.
    print('Seja bem vindo ao menu de remoção de peças! CUIDADO')
    codigo_produto = int(input('Digite o código da peça que deseja remover de seu menu: ')) #foi utilizado o "int" para que o cliente so utilize números inteiros.
    for produto in listar_produto: #"for" foi utilizado para que possamos puxar os itens contidos na lista.
        if produto ['codigo'] == codigo_produto: #utilizado para que o programa puxe apenas os itens selecionados pelo código.
            listar_produto.remove(produto) #Utilizado para remover os itens da lista.
            print('Produto removido com sucesso!')


#programa principal
print('Seja bem vindo a bicicletaria do Willian de Lara Reginato Maba') #identificador pessoal

while True:
    menu_principal = int(input('Escolha a opção desejada:\n' #foi utilizado o "int" para que o cliente só utilize números inteiros.
                           '1-Cadastrar peça\n'
                           '2-Consultar peça\n'
                           '3-Remover peça\n'
                           '4-Sair\n'
                           '>>'))

    if menu_principal == 1: #ao selecionar essa opção o cliente chama a variável "def cadastrarPeca()".
        codigo_produto = codigo_produto + 1 #contador para que o programa consiga distribuir os codigos sem repeti-los.
        cadastrarPeca(codigo_produto) #variável "def cadastrarPeca()".

    elif menu_principal == 2: #ao selecionar essa opção o cliente chama a variável "def consultarPeca()".
        consultarPeca() #variável "def consultarPeca()".

    elif menu_principal == 3: #ao selecionar essa opção o cliente chama a variável "def removerPeca()".
        removerPeca() #variável "def removerPeca()".

    elif menu_principal == 4: #encerra o programa.
        print('Agradecemos sua visita, volte sempre!')
        break

    else: #caso o cliente digite uma opção não existente, levará ele ao inicio do programa.
        print('Digite apenas opções válidas!')
        continue

