from os import system, startfile
import csv
from time import sleep
from sys import exit


clientes = {}
dadosClientes = []
produto = {}
tabelaProduto = []


def enviarDados(bdados):
    """
    Envia as informações dos clientes para o banco de dados
    """
    if bdados == 'CADASTRO_CLIENTES':
        bancoDados = open(f'{bdados}.csv', 'w', newline = '', encoding = 'utf8')
        criarBanco = csv.writer(bancoDados)
        for i in range(len(dadosClientes)):
            criarBanco.writerow([dadosClientes[i]['nom'], dadosClientes[i]['tel'], dadosClientes[i]['end'], dadosClientes[i]['ref']])
        bancoDados.close()


def menuOpcoes(* opcoes):
    """
    Escreve as opções do menu na tela.
    :param opcoes: São as opções que aparecem numeradas na tela.
    :return: Nenhum
    """
    cont = tam = 0
    for r in opcoes:   
        if len(r) > tam:
            tam = len(r)
    print('=' * (tam + 3))
    while True:
        print(f'{cont + 1}. {opcoes[cont]}')
        cont += 1
        if cont >= len(opcoes):
            break
    print('=' * (tam + 3))


def menuPrincipal():
    """
    Mostra o menu principal na tela, com as opções de funcionalidades e a logo.
    :return: Nenhum
    """
    system('cls')
    print('''
    
████████╗░█████╗░██████╗░  ██╗░░░░░░█████╗░███╗░░██╗░█████╗░██╗░░██╗███████╗░██████╗
╚══██╔══╝██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗████╗░██║██╔══██╗██║░░██║██╔════╝██╔════╝
░░░██║░░░██║░░██║██████╔╝  ██║░░░░░███████║██╔██╗██║██║░░╚═╝███████║█████╗░░╚█████╗░
░░░██║░░░██║░░██║██╔═══╝░  ██║░░░░░██╔══██║██║╚████║██║░░██╗██╔══██║██╔══╝░░░╚═══██╗
░░░██║░░░╚█████╔╝██║░░░░░  ███████╗██║░░██║██║░╚███║╚█████╔╝██║░░██║███████╗██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░░░░░  ╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
     
    ''')
    menuOpcoes('CLIENTES', 'PRODUTOS', 'FAZER PEDIDO', 'ENCERRAR PROGRAMA')
    while True:
        try:
            escolha = int(input('Selecione a opção [1-4]: '))
            while escolha < 1 or escolha > 4:
                print('\n\033[31mOpção inválida!\033[m')
                escolha = int(input('Selecione a opção [1-4]: '))
        except (ValueError, TypeError):
            print('\n\033[31mOpção inválida!\033[m')
            continue
        else:
            if escolha == 1:
                menuCliente()
            elif escolha == 2:
                menuProduto()
            elif escolha == 3:
                PDV()
            elif escolha == 4:
                exit()
            



def menuCliente():
    """
    Mostra o menu da parte de clientes, com as opções de cadastrar ou 
    alteração de cadastro de clientes.
    :return: nenhum
    """
    system('cls')
    print('''

▒█▀▀█ █░░ ░▀░ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀ 
▒█░░░ █░░ ▀█▀ █▀▀ █░░█ ░░█░░ █▀▀ ▀▀█ 
▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀
   ''')
    menuOpcoes('CADASTRO DE CLIENTE', 'ALTERAR CLIENTE', 'VOLTAR')
    while True:
        try:
            escolha = int(input('Selecione a opção [1 - 3]: '))
            while escolha < 1 or escolha > 3:
                print('\n\033[31mOpção inválida!\033[m')
                escolha = int(input('Selecione a opção [1 - 3]: '))
        except (ValueError, TypeError):
            print('\n\033[31mOpção inválida!\033[m')
            continue
        else:
            if escolha == 1:
                cadastroCliente()
            if escolha == 2:
                alteraCliente()
            if escolha == 3:
                menuPrincipal()


def cadastroCliente():
    """
    Faz o cadastro dos clientes, adicionando os dados ao dicionário clientes e à lista banco
    de dados.
    """

    def retorno(comando):
            """Reinicia o cadastro de clientes, ou retorna para o menu de clientes
            :param comando: Recebe o nome da variável sendo usada no momento em que a função é chamada"""
            if str(comando) in ('VOLTAR', 'VOLTA'):
                menuCliente()
            if str(comando) in ('RESET'):
                cadastroCliente()


    while True:        
        system('cls')
        print('''   

▒█▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 　 ▒█▀▀█ █░░ ░▀░ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ 
▒█░░░ █▄▄█ █░░█ █▄▄█ ▀▀█ ░░█░░ █▄▄▀ █░░█ 　 ▒█░░░ █░░ ▀█▀ █▀▀ █░░█ ░░█░░ █▀▀ 
▒█▄▄█ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀

*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O CADASTRO ***
''')
       

        '''****FAZ O CADASTRO DOS DADOS DOS CLIENTES  NO DICIONÁRIO clientes E MANDA ESSES DADOS
        PARA A LISTA dadosClientes****'''

        clientes['nom'] = str(input('Nome: ')).upper().strip()
        while clientes['nom'] == '':
            print('\033[31mPor favor, insira um nome válido.\033[m')
            clientes['nom'] = str(input('Nome: ')).upper().strip()
        retorno(clientes['nom'])
        clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
        while clientes['tel'] == '' or clientes['tel'].isnumeric() == False:
            if clientes['tel'] in ('VOLTAR', 'VOLTA', 'RESET'):
                retorno(clientes['tel'])
            print('\033[31mPor favor, insira um número de telefone válido.\033[m')
            clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()

        '''*** VERIFICA SE O NÚMERO DE TELEFONE TEM MENOS/MAIS DE NOVE NÚMEROS, QUE É O PADRÃO DE NÚMEROS
         DE CELULAR NO RIO DE JANEIRO ***'''

        while len(clientes['tel']) < 9 or len(clientes['tel']) > 9:
            if len(clientes['tel']) < 9:
                faltaNumero = str(input(f'Parece estar faltando alguns números no telefone {clientes["tel"]}. Deseja continuar assim mesmo?[S/N] ')).strip().upper()
                if faltaNumero == '':
                    faltaNumero = 'SIM'
                retorno(faltaNumero)
            elif len(clientes['tel']) > 9:
                faltaNumero = str(input(f'O telefone {clientes["tel"]} parece estar com números a mais. Deseja continuar assim mesmo?[S/N] ')).strip().upper()
                if faltaNumero == '':
                    faltaNumero = 'SIM'
                retorno(faltaNumero)
            if faltaNumero in ('N', 'NAO', 'NÃO'):
                clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
                while clientes['tel'] == '' or clientes['tel'].isnumeric() == False:
                    if clientes['tel'] in ('VOLTAR', 'VOLTA', 'RESET'):
                        retorno(clientes['tel'])
                    print('\033[31mPor favor, insira um número de telefone válido.\033[m')
                    clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
            else:
                break    

        '''****VERIFICA SE O TELEFONE CADASTRADO JÁ EXISTE NO BANCO DE DADOS E PEDE 
        UM NÚMERO AINDA NÃO CADASTRADO OU MANDA PARA A ALTERAÇÃO DE CADASTROS****'''

        for item in dadosClientes:
            while item['tel'] == clientes['tel']:
                print(f'\n\033[31mJá existe um cadastro com o telefone {clientes["tel"]}.\033[m')
                print('Por favor, insira um novo número ou digite \033[31mALTERAR\033[m para modificar o cadastro já existente.')
                clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
                while clientes['tel'] == '' or clientes['tel'].isnumeric() == False:
                    if clientes['tel'] in ('VOLTAR', 'VOLTA', 'RESET'):
                        retorno(clientes['tel'])
                    if clientes['tel'] in ('ALTERAR', 'ALTERA'):
                        alteraCliente()
                    print('\033[31mPor favor, insira um número válido.\033[m')
                    clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
        
        clientes['end'] = str(input('Endereço: ')).strip().upper()
        if clientes['end'] == '':
            clientes['end'] = 'Endereço não cadastrado'
        retorno(clientes['end'])
        clientes['ref'] = str(input('Ponto de referência: ')).upper().strip()
        if clientes['ref'] == '':
            clientes['ref'] = 'Ponto de referência não cadastrado'
        else:
            retorno(clientes['ref'])

        '''*** ADICIONA AS NOVAS INFORMAÇÕES AO BANCO DE DADOS ***'''
        dadosClientes.append(clientes.copy())
        print()
        print('Cadastrando cliente...')
        sleep(1.5)
        print()
        escolha = str(input('Cadastro realizado com sucesso! Deseja cadastrar mais um cliente? [S/N] ')).strip().upper()
        while escolha not in ('S', 'N', 'SIM', 'NAO', 'NÃO') or escolha == '':
            print('\nOpção inválida!')
            escolha = str(input('Deseja cadastrar mais um cliente? [S/N] ')).strip().upper()
        if escolha in ('NAO', 'NÃO', 'N'):
            break
    
    enviarDados('CADASTRO_CLIENTES')
    
    menuPrincipal()

def alteraCliente():
    """
    Faz alterações no cadastro dos clientes.
    """
    
    while True:
        system('cls')
        print('''

░█▀▀█ █░░ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀█ 　 ▒█▀▀█ █░░ ░▀░ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ 
▒█▄▄█ █░░ ░░█░░ █▀▀ █▄▄▀ █▄▄█ █▄▄▀ 　 ▒█░░░ █░░ ▀█▀ █▀▀ █░░█ ░░█░░ █▀▀ 
▒█░▒█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░▀▀ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀
        
*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O CADASTRO ***
        ''')

        '''***FAZ A BUSCA DO CADASTRO DO CLIENTE ATRAVÉS DO NÚMERO DE TELEFONE***'''
        busca = str(input('Digite o número de telefone do cliente: ')).strip().upper()
        while busca.isnumeric() == False or busca == '':
            if busca in ('VOLTAR', 'VOLTA'):
                menuCliente()
            print('\033[31mDigite um numero de telefone válido.\033[m')
            busca = str(input('Digite o número de telefone do cliente: ')).strip()
        cont = 0
        for item in dadosClientes:
            if item['tel'] == busca:
                print()
                print('=' * 50)
                print('DADOS DO CLIENTE')
                print('=' * 50)
                for k, v in item.items():
                    print(f'{k}: {v}') 
                    clientes[k] = v
                print('=' * 50)
                sleep(1)
                
                '''***FAZ ALTERAÇÕES NO CADASTRO DO CLIENTE***'''
                while True:
                    alterar = str(input('\nDeseja alterar qual campo? [NOME/TELEFONE/ENDEREÇO/REFERENCIA]: ')).strip().lower()[:3]
                    while alterar not in ('nom', 'tel', 'end', 'ref', 'vol', 'res') or alterar == '':
                        print('\033[31mOpção inválida.\033[m')
                        alterar = str(input('Deseja alterar qual campo? [NOME/TELEFONE/ENDEREÇO/REFERENCIA]: ')).strip().lower()[:3]
                    if alterar in ('res'):
                        alteraCliente()
                    elif alterar in ('vol'):
                        menuCliente()
                    clientes[alterar] = str(input('Insira o novo valor: ')).upper().strip()
                    if clientes[alterar] in ('RESET'):
                        alteraCliente()
                    elif clientes[alterar] in ('VOLTAR', 'VOLTA'):
                        menuCliente()
                    while alterar == 'nom' and clientes[alterar].isnumeric():
                        print('\033[31mPor favor, digite um nome válido.\033[m')
                        clientes[alterar] = str(input('Insira o novo valor: ')).upper().strip()
                    while alterar == 'tel' and clientes[alterar].isnumeric() == False:
                        if clientes[alterar] in ('RESET'):
                            alteraCliente()
                        elif clientes[alterar] in ('VOLTAR', 'VOLTA'):
                            menuCliente()
                        print('Por favor, digite um número de telefone válido.')
                        clientes[alterar] = str(input('Insira o novo valor: '))
                    continuar = str(input('Deseja fazer mais alguma alteração? ')).strip().upper()
                    while continuar not in ('S', 'N', 'SIM', 'NAO', 'NÃO', 'RESET', 'VOLTAR', 'VOLTA'):
                        print('\033[31mOpção inválida.\033[m')
                        continuar = str(input('Deseja fazer mais alguma alteração? ')).strip().upper()
                    if continuar in ('RESET'):
                        alteraCliente()
                    elif continuar in ('VOLTAR', 'VOLTA'):
                        menuCliente()
                    elif continuar in ('N', 'NÃO', 'NAO'):
                        break
                if clientes != dadosClientes[cont]:
                        print()
                        print('=' * 50)
                        print('DADOS DO CLIENTE')
                        print('=' * 50)
                        for k, v in clientes.items():
                            print(f'{k}: {v}') 
                        print('=' * 50)
                        sleep(1)
                        salvar = str(input('Deseja salvar essas alterações? [S/N] ')).strip()[0]
                        while salvar not in 'SsNn':
                            print('\033[31mOpção inválida.\033[m')
                            salvar = str(input('Deseja salvar essas alterações? [S/N] ')).strip()[0]
                        if salvar in 'sS':
                            print('Alterando cadastro...')
                            sleep(1)
                            del dadosClientes[cont]
                            dadosClientes.insert(cont, clientes.copy())
                            print('Cadastro alterado com sucesso!')
                        enviarDados('CADASTRO_CLIENTES')
                        escolha = str(input('Deseja alterar mais algum cadastro? [S/N] ')).strip()[0]
                        while escolha not in 'SsNn':
                            print('\033[31mOpção inválida.\033[m')
                            escolha = str(input('Deseja alterar mais algum cadastro? [S/N] ')).strip()[0]
                        if escolha in 'Ss':
                            alteraCliente()  
                        else:
                            break      
            else:
                cont += 1
                if cont >= len(dadosClientes):
                    print()
                    print('Número não encontrado.')
                    sleep(1)
                    escolha = str(input('Deseja fazer uma nova busca? [S/N] ')).strip()[0]
                    while escolha not in 'SsNn':
                        print('Opção inválida.')
                        escolha = str(input('Deseja fazer uma nova busca? [S/N] ')).strip()[0]
                    if escolha in 'Ss':
                        alteraCliente()
        break
    menuPrincipal()

            
def menuProduto():
    system('cls')
    print('''

▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ ▀▀█▀▀ █▀▀█ █▀▀ 
▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ ░░█░░ █░░█ ▀▀█ 
▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀▀ ▀▀▀
    ''')
    menuOpcoes('CADASTRO DE PRODUTOS', 'ALTERAÇÃO DE CADASTRO', 'LISTA DE PRODUTOS', 'VOLTAR')
    escolha = str(input('Selecione a opção [1/4]: '))
    while escolha not in ('1', '2', '3', '4') or escolha == '':
        print('Opção inválida!')
        escolha = str(input('Selecione a opção [1/3]: '))
    if escolha == '1':
        cadastroProduto()
    if escolha == '2':
        alteraProduto()
    if escolha == '3':
        mostrarProduto()
    if escolha == '4':
        menuPrincipal()


def cadastroProduto():
    while True:
        system('cls')
        print('''    

▒█▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ ▀▀█▀▀ █▀▀█ █▀▀ 
▒█░░░ █▄▄█ █░░█ █▄▄█ ▀▀█ ░░█░░ █▄▄▀ █░░█ 　 ▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ ░░█░░ █░░█ ▀▀█ 
▒█▄▄█ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ 　 ▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀▀ ▀▀▀
    ''')
        print()
        produto['nom'] = str(input('Nome do produto: ')).strip().upper()
        while produto['nom'] == '':
            print('\nOpção inválida!')
            produto['nom'] = str(input('Por favor, digite o nome do produto: ')).strip().upper()
        produto['pre'] = str(input('Preço: R$ ')).strip()
        while produto['pre'] == '' or produto['pre'].find(',') != -1 or produto['pre'].count('.') > 1:
            if produto['pre'].find(',') != -1:
                produto['pre'] = produto['pre'].replace(',', '.')
            else:
                print('\nOpção inválida!')
                produto['pre'] = str(input('Por favor, digite o preço: R$ ')).strip()
        tabelaProduto.append(produto.copy())
        print()
        print('Cadastrando...')
        sleep(1.5)
        print()
        escolha = str(input(f'O produto {produto["nom"]} foi cadastrado no código {len(tabelaProduto)}! Deseja cadastrar mais um produto? [S/N] ')).strip()[0]
        while escolha not in 'sSnN':
            print('\nOpção inválida')
            escolha = str(input('Deseja cadastrar mais um produto? [S/N] ')).strip()[0]
        if escolha in 'Nn':
            break
    bancoDados = open('CADASTRO_PRODUTOS.csv', 'w', newline = '', encoding = 'utf8')
    criarBanco = csv.writer(bancoDados)
    for i in range(len(tabelaProduto)):
        criarBanco.writerow([tabelaProduto[i]['nom'], tabelaProduto[i]['pre']])
    bancoDados.close()
    menuPrincipal()
    

def alteraProduto():
    while True:
        system('cls')
        print('''
        
    ░█▀▀█ █░░ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀█ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ ▀▀█▀▀ █▀▀█ 
    ▒█▄▄█ █░░ ░░█░░ █▀▀ █▄▄▀ █▄▄█ █▄▄▀ 　 ▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ ░░█░░ █░░█ 
    ▒█░▒█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░▀▀ 　 ▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀▀
        ''')
        print()
        busca = int(input('Código do produto: '))
        print()
        print('=' * 50)
        print(f'Nome: {tabelaProduto[busca - 1]["nom"]}\nPreço: R$ {float(tabelaProduto[busca - 1]["pre"]):.2f}')
        print('=' * 50)
        produto['nom'] = tabelaProduto[busca - 1]['nom']
        produto['pre'] = tabelaProduto[busca - 1]['pre']
        sleep(1)
        while True:
            alterar = str(input('\nDeseja alterar qual campo? [NOME/PREÇO/SAIR para sair] ')).strip()[:3]
            print()
            if alterar == 'sai':
                break
            elif alterar == 'pre':
                produto[alterar] = str(input('Digite o novo preço: R$ ')).strip()
                while produto[alterar] == '' or produto[alterar].find(',') != -1 or produto[alterar].count('.') > 1:
                    print('\nOpção inválida!')
                    if produto[alterar].find(',') != -1:
                        print('Por favor, não use vírgula para separar os centavos.\n')
                    produto[alterar] = str(input('Por favor, digite o preço: R$ ')).strip()
            elif alterar == 'nom':
                produto[alterar] = str(input('Digite o novo nome do produto: ')).strip().upper()
        print('=' * 50)
        print(f'Nome: {produto["nom"]}\nPreço: R$ {float(produto["pre"]):.2f}')
        print('=' * 50)
        salvar = str(input('\nDeseja salvar essas alterações? [S/N] ')).strip()[0]
        while salvar not in 'SsNn':
            print('Opção inválida.')
            escolha = str(input('Deseja salvar essas alterações? [S/N] ')).strip()[0]
        if salvar in 'sS':
            del tabelaProduto[busca - 1]
            tabelaProduto.insert(busca - 1, produto.copy())
            bancoDados = open('CADASTRO_PRODUTOS.csv', 'w', newline = '', encoding = 'utf8')
            criarBanco = csv.writer(bancoDados)
            for i in range(len(tabelaProduto)):
                criarBanco.writerow([tabelaProduto[i]['nom'], tabelaProduto[i]['pre']])
            bancoDados.close()
        escolha = str(input('Deseja alterar mais algum produto? ')).strip()[0]
        while escolha not in 'SsNn':
            print('\nOpção inválida')
            escolha = str(input('Deseja alterar mais algum produto? ')).strip()[0]
        if escolha in 'Nn':
            menuPrincipal()


def mostrarProduto():
    system('cls')
    print('=' * 50)
    print(f'{"COD":<4} {"PRODUTO":<35} {"PREÇO":<20}')
    print('=' * 50)
    for i, p in enumerate(tabelaProduto):
        print(f'{i + 1:<4} {p["nom"]:<35} R$ {float(p["pre"]):<20.2f}')
    print('=' * 50)
    sair = str(input('Aperte ENTER para sair ')).strip()
    if sair == '':
        menuPrincipal()
    menuPrincipal()


def PDV():
    pedidos = []
    quantidadeLista = []
    taxaEntrega = contador = total = 0
    cabecalho = f'{"QUANT":<6} {" ITEM"} {"PREÇO":>61}'
    verificaTel = False
    
    system('cls')
    print('''     
▒█▀▀█ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ █▀▀ 
▒█▄▄█ █▀▀ █░░█ ▀█▀ █░░█ █░░█ ▀▀█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀░ ▀▀▀▀ ▀▀▀''')   
    while True:
        print()
        codigo = int(input('Código [999 para encerrar]: '))
        while codigo > len(tabelaProduto) or codigo <= 0:
            if codigo == 999:
                break
            print('Código não cadastrado.')
            codigo = int(input('Código [999 para encerrar]: '))
        while codigo == 999:
            escolha = str(input('Deseja fechar esse pedido? [S/N] ')).strip()[0]
            while escolha not in 'SsNn':
                print('Opção inválida!')
                escolha = str(input('Deseja fechar esse pedido? [S/N] ')).strip()[0]
            if escolha in 'Nn':
                codigo = int(input('Código [999 para encerrar]: '))
            else:
                entrega = str(input('Entrega? [S/N] '))
                while entrega not in 'SsNn':
                    print('Opção inválida!')
                    entrega = str(input('Entrega? [S/N] '))
                if entrega in 'Ss':
                    taxaEntrega = str(input('Taxa de entrega: R$ ')).strip()
                    while taxaEntrega == '' or taxaEntrega.isnumeric() == False:
                        print('Opção inválida!')
                        taxaEntrega = str(input('Taxa de entrega: R$ ')).strip()
                    buscaCliente = str(input('Digite o número de telefone do cliente: ')).strip()
                    while not verificaTel:
                        for numero in dadosClientes:
                            if numero['tel'] != buscaCliente:
                                contador += 1
                            if contador > len(dadosClientes):
                                print('Número inexistente!')
                                buscaCliente = str(input('Digite o número de telefone do cliente: ')).strip()
                                contador = 0
                            if numero['tel'] == buscaCliente:
                                verificaTel = True
                else:
                    break
                break
        if codigo == 999:
            break
        quantidade = str(input('Quantidade: '))
        if quantidade == '':
            quantidade = '1'
        while quantidade.isnumeric() == False:
            print('Insira uma quantidade válida!')
            quantidade = str(input('Quantidade: '))
            if quantidade == '':
                quantidade = '1'
        quantidadeLista.append(quantidade)
        pedidos.append(codigo)
        total += float(tabelaProduto[codigo - 1]['pre']) * int(quantidade)
        system('cls')
        print('''
            
▒█▀▀█ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ █▀▀ 
▒█▄▄█ █▀▀ █░░█ ▀█▀ █░░█ █░░█ ▀▀█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀░ ▀▀▀▀ ▀▀▀''')   
        print()
        print()
        print('=' * 75)
        print(cabecalho)
        print('=' * 75)
        print()
        for pos, itens in enumerate(pedidos):
                print(f'{quantidadeLista[pos]:^6}  {tabelaProduto[itens - 1]["nom"]:.<60} {(float(tabelaProduto[itens - 1]["pre"]) * int(quantidadeLista[pos])):.2f}')
        print()
        print(f'{"        TOTAL":.<65} R$ {total:.2f}')
    if len(pedidos) == 0:
        menuPrincipal()
    system('cls')
    print('''
            
▒█▀▀█ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ █▀▀ 
▒█▄▄█ █▀▀ █░░█ ▀█▀ █░░█ █░░█ ▀▀█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀░ ▀▀▀▀ ▀▀▀''')   
    print()
    print()
    print('=' * 75)
    print(cabecalho)
    print('=' * 75)
    print()
    for pos, itens in enumerate(pedidos):
        print(f'{quantidadeLista[pos]:^6}  {tabelaProduto[itens - 1]["nom"]:.<60} {(float(tabelaProduto[itens - 1]["pre"]) * int(quantidadeLista[pos])):.2f}')
    if float(taxaEntrega) > 0:
        print()
        print(f'{"        ENTREGA":.<65} R$ {float(taxaEntrega):.2f} ')
        print()
        print(f'{"        TOTAL":.<65} R$ {(total + float(taxaEntrega)):.2f}')
        print()
        print('DADOS DO CLIENTE:')
        print()
        for numero in dadosClientes:
            for k, v in numero.items():
                if numero['tel'] == buscaCliente:
                    print(f'{k}: {v}')
        bancoDados = open('NOTA_PEDIDO.txt', 'w', newline = '', encoding = 'utf8')
        criarBanco = csv.writer(bancoDados)
        criarBanco.writerow([cabecalho])
        for pos, itens in enumerate(pedidos):
            criarBanco.writerow([f' {quantidadeLista[pos]:^6} {tabelaProduto[itens - 1]["nom"]:.<60} {(float(tabelaProduto[itens - 1]["pre"]) * int(quantidadeLista[pos])):.2f}'])
        criarBanco.writerow([])
        criarBanco.writerow([f'{"        ENTREGA":.<65} R$ {float(taxaEntrega):.2f} '])
        criarBanco.writerow([f'{"        TOTAL":.<65} R$ {(total + float(taxaEntrega)):.2f}'])
        criarBanco.writerow([])
        criarBanco.writerow(['DADOS DO CLIENTE: '])
        criarBanco.writerow([])
        for numero in dadosClientes:
            for k, v in numero.items():
                if numero['tel'] == buscaCliente:
                    criarBanco.writerow([f'{k}: {v}'])
        bancoDados.close()
        imprimir = str(input('Deseja imprimir? [S/N] ')).strip().upper()
        while imprimir not in ('S', 'SIM', 'N', 'NAO', 'NÃO') or imprimir == '':
            print('Opção inválida!')
            imprimir = str(input('Deseja imprimir? [S/N] ')).strip()
        if imprimir in ('S', 'SIM'):
            startfile(r'C:\Users\ramon\Desktop\DEV\Python\TOPLANCHES\NOTA_PEDIDO.txt', 'print')
        escolha = str(input('Deseja fazer um novo pedido? [S/N] ')).strip().upper()
        while escolha not in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            print('Opção inválida.')
            escolha = str(input('Deseja fazer um novo pedido? [S/N] ')).strip().upper()
        if escolha in ('S', 'SIM'):
            PDV()
        menuPrincipal()
    else:
        print()
        print(f'{"        TOTAL":.<65} R$ {(total + float(taxaEntrega)):.2f}')
        bancoDados = open('NOTA_PEDIDO.txt', 'w', newline = '', encoding = 'utf8')
        criarBanco = csv.writer(bancoDados)
        criarBanco.writerow([cabecalho])
        for pos, itens in enumerate(pedidos):
            criarBanco.writerow([f' {quantidadeLista[pos]:^6} {tabelaProduto[itens - 1]["nom"]:.<60} {(float(tabelaProduto[itens - 1]["pre"]) * int(quantidadeLista[pos])):.2f}'])
        criarBanco.writerow([])
        criarBanco.writerow([f'{"        TOTAL":.<65} R$ {(total + float(taxaEntrega)):.2f}'])
        bancoDados.close()
        print()
        imprimir = str(input('Deseja imprimir? [S/N] ')).strip().upper()
        while imprimir not in ('S', 'SIM', 'N', 'NAO', 'NÃO') or imprimir == '':
            print('Opção inválida!')
            imprimir = str(input('Deseja imprimir? [S/N] ')).strip().upper()
        if imprimir in ('S', 'SIM'):
            startfile(r'C:\Users\ramon\Desktop\DEV\Python\TOPLANCHES\NOTA_PEDIDO.txt', 'print')
        escolha = str(input('Deseja fazer um novo pedido? [S/N] ')).strip().upper()
        while escolha not in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            print('Opção inválida.')
            escolha = str(input('Deseja fazer um novo pedido? [S/N] ')).strip().upper()
        if escolha in ('S', 'SIM'):
            PDV()
        menuPrincipal()

        
        




#Programa Principal

with open('CADASTRO_CLIENTES.csv', encoding = 'utf-8') as lerDadosClientes:
    leitorCliente = csv.reader(lerDadosClientes, delimiter = ',')
    for linha in leitorCliente:
        clientes['nom'] = linha[0]
        clientes['tel'] = linha[1]
        clientes['end'] = linha[2]
        clientes['ref'] = linha[3]
        dadosClientes.append(clientes.copy())
with open('CADASTRO_PRODUTOS.csv', encoding = 'utf-8') as lerDadosProdutos:
    leitorProduto = csv.reader(lerDadosProdutos, delimiter = ',')
    for linha in leitorProduto:
        produto['nom'] = linha[0]
        produto['pre'] = linha[1]
        tabelaProduto.append(produto.copy())

#print(dadosClientes)
#print(tabelaProduto)

#if 'pre' in tabelaProduto[0]:
    #print('bolado')

#d = {"key1": 10, "key2": 23}

#if "" in d:
    #print("this will execute")

#if "nonexistent key" in d:
    #print("this will not")
menuPrincipal()
