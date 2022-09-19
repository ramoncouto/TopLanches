from os import system, startfile
import csv
from time import sleep
from sys import exit


clientes = {}
dadosClientes = []
produto = {}
tabelaProduto = []


def retorno(origem, comando):
            """Reinicia a função, ou retorna para o menu anterior
            :param origem: Recebe a função que originou o chamado. É usado para saber qual a função deve ser chamada ao usar o comando voltar.
            :param comando: Recebe o nome da variável sendo usada no momento em que a função é chamada
            :return: Nenhum
            """
            if str(comando) in ('VOLTAR', 'VOLTA'):
                if origem == 'cadcli':
                    menuCliente()
                elif origem == 'altcli':
                    menuCliente()
                elif origem == 'cadpro':
                    menuProduto()
                elif origem == 'altpro':
                    menuProduto()
                elif origem == 'pdv':
                    menuPrincipal()
                
            if str(comando) in ('RESET'):
                if origem == 'cadcli':
                    cadastroCliente()
                elif origem == 'altcli':
                    alteraCliente()
                elif origem == 'cadpro':
                    cadastroProduto()
                elif origem == 'altpro':
                    alteraProduto()
                elif origem == 'pdv':
                    pdv()


def enviarDados(bdados):
    """
    Envia as informações para os bancos de dados
    :param bdados: recebe o nome do banco de dados para onde as informações devem ser enviadas.
    :return: Nenhum
    """
    if bdados == 'CADASTRO_CLIENTES':
        bancoDados = open(f'{bdados}.csv', 'w', newline = '', encoding = 'utf8')
        criarBanco = csv.writer(bancoDados)
        for i in range(len(dadosClientes)):
            criarBanco.writerow([dadosClientes[i]['nom'], dadosClientes[i]['tel'], dadosClientes[i]['end'], dadosClientes[i]['ref']])
        bancoDados.close()
    if bdados == 'CADASTRO_PRODUTOS':
        bancoDados = open('CADASTRO_PRODUTOS.csv', 'w', newline = '', encoding = 'utf8')
        criarBanco = csv.writer(bancoDados)
        for i in range(len(tabelaProduto)):
            criarBanco.writerow([tabelaProduto[i]['nom'], tabelaProduto[i]['pre']])
        bancoDados.close()


def menuOpcoes(* opcoes):
    """
    Escreve as opções dos menus na tela.
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
    menuOpcoes('CLIENTES', 'PRODUTOS', 'FAZER PEDIDO')
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
                pdv()
            



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
    while True:        
        system('cls')
        print('''   

▒█▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 　 ▒█▀▀█ █░░ ░▀░ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ 
▒█░░░ █▄▄█ █░░█ █▄▄█ ▀▀█ ░░█░░ █▄▄▀ █░░█ 　 ▒█░░░ █░░ ▀█▀ █▀▀ █░░█ ░░█░░ █▀▀ 
▒█▄▄█ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀

*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O CADASTRO ***
''')
       

        #****FAZ O CADASTRO DOS DADOS DOS CLIENTES  NO DICIONÁRIO clientes E MANDA ESSES DADOS PARA A LISTA dadosClientes****

        clientes['nom'] = str(input('Nome: ')).upper().strip()
        while clientes['nom'] == '':
            print('\033[31mPor favor, insira um nome válido.\033[m')
            clientes['nom'] = str(input('Nome: ')).upper().strip()
        retorno('cadcli', clientes['nom'])
        clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
        while clientes['tel'] == '' or clientes['tel'].isnumeric() == False:
            if clientes['tel'] in ('VOLTAR', 'VOLTA', 'RESET'):
                retorno('cadcli', clientes['tel'])
            print('\033[31mPor favor, insira um número de telefone válido.\033[m')
            clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()

        #*** VERIFICA SE O NÚMERO DE TELEFONE TEM MENOS/MAIS DE NOVE NÚMEROS, QUE É O PADRÃO DE NÚMEROS DE CELULAR NO RIO DE JANEIRO ***

        while len(clientes['tel']) < 9 or len(clientes['tel']) > 9:
            if len(clientes['tel']) < 9:
                faltaNumero = str(input(f'Parece estar faltando alguns números no telefone {clientes["tel"]}. Deseja continuar assim mesmo?[S/N] ')).strip().upper()
                if faltaNumero == '':
                    faltaNumero = 'SIM'
                retorno('cadcli', faltaNumero)
            elif len(clientes['tel']) > 9:
                faltaNumero = str(input(f'O telefone {clientes["tel"]} parece estar com números a mais. Deseja continuar assim mesmo?[S/N] ')).strip().upper()
                if faltaNumero == '':
                    faltaNumero = 'SIM'
                retorno('cadcli', faltaNumero)
            if faltaNumero in ('N', 'NAO', 'NÃO'):
                clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
                while clientes['tel'] == '' or clientes['tel'].isnumeric() == False:
                    if clientes['tel'] in ('VOLTAR', 'VOLTA', 'RESET'):
                        retorno('cadcli', clientes['tel'])
                    print('\033[31mPor favor, insira um número de telefone válido.\033[m')
                    clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
            else:
                break    

        #****VERIFICA SE O TELEFONE CADASTRADO JÁ EXISTE NO BANCO DE DADOS E PEDE UM NÚMERO AINDA NÃO CADASTRADO OU MANDA PARA A ALTERAÇÃO DE CADASTROS****'''

        for item in dadosClientes:
            while item['tel'] == clientes['tel']:
                print(f'\n\033[31mJá existe um cadastro com o telefone {clientes["tel"]}.\033[m')
                print('Por favor, insira um novo número ou digite \033[31mALTERAR\033[m para modificar o cadastro já existente.')
                clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
                while clientes['tel'] == '' or clientes['tel'].isnumeric() == False:
                    if clientes['tel'] in ('VOLTAR', 'VOLTA', 'RESET'):
                        retorno('cadcli', clientes['tel'])
                    if clientes['tel'] in ('ALTERAR', 'ALTERA'):
                        alteraCliente()
                    print('\033[31mPor favor, insira um número válido.\033[m')
                    clientes['tel'] = str(input('Telefone (apenas números): ')).upper().strip()
        
        clientes['end'] = str(input('Endereço: ')).strip().upper()
        if clientes['end'] == '':
            clientes['end'] = 'Endereço não cadastrado'
        retorno('cadcli', clientes['end'])
        clientes['ref'] = str(input('Ponto de referência: ')).upper().strip()
        if clientes['ref'] == '':
            clientes['ref'] = 'Ponto de referência não cadastrado'
        else:
            retorno('cadcli', clientes['ref'])

        #*** ADICIONA AS NOVAS INFORMAÇÕES AO BANCO DE DADOS ***
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

        #***FAZ A BUSCA DO CADASTRO DO CLIENTE ATRAVÉS DO NÚMERO DE TELEFONE***
        busca = str(input('Digite o número de telefone do cliente: ')).strip().upper()
        while busca.isnumeric() == False or busca == '':
            if busca in ('VOLTAR', 'VOLTA', 'RESET'):
                retorno('altcli', busca)
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
                
                #***FAZ ALTERAÇÕES NO CADASTRO DO CLIENTE***
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
                    if clientes[alterar] in ('RESET', 'VOLTAR', 'VOLTA'):
                        retorno('altcli', clientes[alterar])
                    while alterar == 'nom' and clientes[alterar].isnumeric():
                        print('\033[31mPor favor, digite um nome válido.\033[m')
                        clientes[alterar] = str(input('Insira o novo valor: ')).upper().strip()
                    while alterar == 'tel' and clientes[alterar].isnumeric() == False:
                        if clientes[alterar] in ('RESET', 'VOLTAR', 'VOLTA'):
                            retorno('altcli', clientes[alterar])
                        print('Por favor, digite um número de telefone válido.')
                        clientes[alterar] = str(input('Insira o novo valor: '))
                    continuar = str(input('Deseja fazer mais alguma alteração? ')).strip().upper()
                    while continuar not in ('S', 'N', 'SIM', 'NAO', 'NÃO', 'RESET', 'VOLTAR', 'VOLTA'):
                        print('\033[31mOpção inválida.\033[m')
                        continuar = str(input('Deseja fazer mais alguma alteração? ')).strip().upper()
                    if continuar in ('RESET', 'VOLTAR', 'VOLTA'):
                        retorno('altcli', continuar)
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
    # *** OFERECE FAZER UMA NOVA BUSCA CASO O NÚMERO NÃO INSERIDO NÃO EXISTA NO CADASTRO ***
            else:
                cont += 1
                if cont >= len(dadosClientes):
                    print()
                    print('\033[31mNúmero não encontrado.\033[m')
                    sleep(1)
                    escolha = str(input('Deseja fazer uma nova busca? [S/N] ')).strip()[0]
                    while escolha not in 'SsNn':
                        print('\033[31mOpção inválida.\033[m')
                        escolha = str(input('Deseja fazer uma nova busca? [S/N] ')).strip()[0]
                    if escolha in 'Ss':
                        alteraCliente()
        break
    menuPrincipal()

            
def menuProduto():
    """Mostra o menu da parte de produtos, com as opções de cadastrar, alterar o cadastro ou ver uma lista dos produtos já cadastrados."""
    system('cls')
    print('''

▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ ▀▀█▀▀ █▀▀█ █▀▀ 
▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ ░░█░░ █░░█ ▀▀█ 
▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀▀ ▀▀▀
    ''')
    menuOpcoes('CADASTRO DE PRODUTOS', 'ALTERAÇÃO DE CADASTRO', 'LISTA DE PRODUTOS', 'VOLTAR')
    escolha = str(input('Selecione a opção [1/4]: '))
    while escolha not in ('1', '2', '3', '4') or escolha == '':
        print('\033[31mOpção inválida!\033[m')
        escolha = str(input('Selecione a opção [1/4]: '))
    if escolha == '1':
        cadastroProduto()
    if escolha == '2':
        alteraProduto()
    if escolha == '3':
        mostrarProduto()
    if escolha == '4':
        menuPrincipal()


def cadastroProduto():
    """Cadastra produtos novos no banco de dados"""
    while True:
        system('cls')
        print('''    

▒█▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ ▀▀█▀▀ █▀▀█ █▀▀ 
▒█░░░ █▄▄█ █░░█ █▄▄█ ▀▀█ ░░█░░ █▄▄▀ █░░█ 　 ▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ ░░█░░ █░░█ ▀▀█ 
▒█▄▄█ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ 　 ▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀▀ ▀▀▀

*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O CADASTRO ***''')
        print()
        produto['nom'] = str(input('Nome do produto: ')).strip().upper()
        while produto['nom'] == '':
            print('\033[31mOpção inválida!\033[m')
            produto['nom'] = str(input('Por favor, digite o nome do produto: ')).strip().upper()
        if produto['nom'] in ('RESET', 'VOLTAR', 'VOLTA'):
            retorno('cadpro', produto['nom'])
        produto['pre'] = str(input('Preço: R$ ')).strip()
        while produto['pre'] == '' or produto['pre'].find(',') != -1 or produto['pre'].count('.') > 1 or produto['pre'].isalpha() == True:
            if produto['nom'] in ('RESET', 'VOLTAR', 'VOLTA'):
                retorno('cadpro', produto['nom'])
            if produto['pre'].find(',') != -1:
                produto['pre'] = produto['pre'].replace(',', '.')
            else:
                print('\033[31mOpção inválida!\033[m')
                produto['pre'] = str(input('Por favor, digite o preço: R$ ')).strip()
        #***MOSTRA NA TELA O PRODUTO QUE FOI CADASTRADO***
        verificaProduto = (f'| {produto["nom"]}    R$ {produto["pre"]} |')
        print('\nO produto cadastrado foi:\n')
        print('-' * len(verificaProduto))
        print(verificaProduto)
        print('-' * len(verificaProduto))
        confirma = str(input('Deseja confirmar? [S/N]: ')).strip().upper()
        while confirma not in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            if confirma in ('RESET', 'VOLTAR', 'VOLTA'):
                retorno('cadpro', confirma)
            print('\033[31mOpção inválida!\033[m')
            confirma = str(input('Deseja confirmar? [S/N]: ')).strip().upper()
        if confirma in ('N', 'NAO', 'NÃO'):
            cadastroProduto()
        print()
        print('Cadastrando...')
        sleep(1.5)
        tabelaProduto.append(produto.copy())
        enviarDados('CADASTRO_PRODUTOS')
        print()
        escolha = str(input(f'O produto {produto["nom"]} foi cadastrado no código {len(tabelaProduto)}! Deseja cadastrar mais um produto? [S/N] ')).strip()[0]
        while escolha not in 'sSnN':
            print('\033[31mOpção inválida!\033[m')
            escolha = str(input('Deseja cadastrar mais um produto? [S/N] ')).strip()[0]
        if escolha in 'Nn':
            break
    menuPrincipal()
    

def alteraProduto():
    """Faz alterações nos preços e nomes dos produtos já cadastrados"""

    
    while True:
        system('cls')
        print('''
        
░█▀▀█ █░░ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀█ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ ▀▀█▀▀ █▀▀█ 
▒█▄▄█ █░░ ░░█░░ █▀▀ █▄▄▀ █▄▄█ █▄▄▀ 　 ▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ ░░█░░ █░░█ 
▒█░▒█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░▀▀ 　 ▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀▀
             
*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O CADASTRO ***
''')
        busca = str(input('Código do produto: ')).upper()
        while busca == '' or busca.isnumeric() == False:    
            if busca in ('VOLTAR', 'VOLTA', 'RESET'):
                retorno('altpro', busca)
            print('\033[31mOpção inválida!\033[m')
            busca = str(input('Código do produto: ')).upper()
        print('Buscando...')
        busca = int(busca)
        sleep(1)
        print()
        print('=' * 50)
        print(f'Nome: {tabelaProduto[busca - 1]["nom"]}\nPreço: R$ {float(tabelaProduto[busca - 1]["pre"]):.2f}')
        print('=' * 50)
        produto['nom'] = tabelaProduto[busca - 1]['nom']
        produto['pre'] = tabelaProduto[busca - 1]['pre']
        sleep(1)
        while True:
            alterar = str(input('\nDeseja alterar qual campo? [NOME/PREÇO] ')).strip().lower()[:3]
            print()
            if alterar == 'vol':
                alterar = 'VOLTA'
                retorno('altpro', alterar)
            elif alterar == 'res':
                alterar = 'RESET'
                retorno('altpro', alterar)               
            elif alterar == 'pre':
                produto[alterar] = str(input('Digite o novo preço: R$ ')).strip().upper()
                while produto[alterar] == '' or produto[alterar].find(',') != -1 or produto[alterar].count('.') > 1 or produto[alterar].isalpha() == True:
                    if produto[alterar] in ('VOLTAR', 'VOLTA', 'RESET'):
                        retorno('altpro', produto[alterar])
                    if produto[alterar].find(',') != -1:
                        produto['pre'] = produto['pre'].replace(',', '.')
                    else:
                        print('\033[31mOpção inválida!\033[m')
                        produto[alterar] = str(input('Por favor, digite o preço: R$ ')).strip()
            elif alterar == 'nom':
                produto[alterar] = str(input('Digite o novo nome do produto: ')).strip().upper()
                while produto[alterar].isnumeric() == True:
                    print('\033[31mOpção inválida!\033[m')
                    produto[alterar] = str(input('Por favor, digite um nome válido: R$ ')).strip()
                if produto[alterar] in ('VOLTAR', 'VOLTA', 'RESET'):
                    retorno('altpro', produto[alterar])
            encerrar = str(input('Deseja fazer mais alguma alteração? [S/N]: ')).strip().upper()
            while encerrar not in 'SN':
                if encerrar in ('VOLTAR', 'VOLTA', 'RESET'):
                    retorno('altpro', encerrar)
                print('\033[31mOpção inválida!\033[m')
                encerrar = str(input('Deseja fazer mais alguma alteração? [S/N]: ')).strip().upper()
                if encerrar in 'N':
                    break
        print('=' * 50)
        print(f'Nome: {produto["nom"]}\nPreço: R$ {float(produto["pre"]):.2f}')
        print('=' * 50)
        salvar = str(input('\nDeseja salvar essas alterações? [S/N] ')).strip().upper()[0]
        while salvar not in 'SN':
            if salvar in ('VOLTAR', 'VOLTA', 'RESET'):
                retorno('altpro', salvar)
            print('\033[31mOpção inválida!\033[m')
            escolha = str(input('Deseja salvar essas alterações? [S/N] ')).strip().upper()[0]
        if salvar in 'sS':
            del tabelaProduto[busca - 1]
            tabelaProduto.insert(busca - 1, produto.copy())
            enviarDados('CADASTRO_PRODUTOS')
        escolha = str(input('Deseja alterar mais algum produto? ')).strip().upper()[0]
        while escolha not in 'SN':
            print('\033[31mOpção inválida!\033[m')
            escolha = str(input('Deseja alterar mais algum produto? ')).strip().upper()[0]
        if escolha in 'Nn':
            menuPrincipal()


def mostrarProduto():
    """Mostra uma tabela com os nomes, preços e códigos dos produtos já cadastrados"""
    
    
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
    


def pdv():
    """Faz as operações de vendas e impressão dos pedidos"""

    #*** IMPRIME O PREDIDO NA TELA, COM QUANTIDADE, NOME DOS PRODUTOS E VALOR, TOTAL E INDIVIDUAL ***
    def imprimir():
        """Imprime o pedido"""


        imprimir = str(input('Deseja imprimir? [S/N] ')).strip().upper()
        while imprimir not in ('S', 'SIM', 'N', 'NAO', 'NÃO') or imprimir == '':
            if imprimir in ('RESET', 'VOLTAR', 'VOLTA'):
                retorno('pdv', imprimir)
            print('\033[31mOpção inválida!\033[m')
            imprimir = str(input('Deseja imprimir? [S/N] ')).strip().upper()
        if imprimir in ('S', 'SIM'):
            startfile(r'C:\Users\ramon\Desktop\RAMON\DEV\Python\TOPLANCHES\NOTA_PEDIDO.txt', 'print')
    
    def notaFiscal(entrega = False):
        """Cria o arquivo usado para a impressão do pedido
        :Param entrega: Verifica se o pedido é para entrega, adicionando o valor da taxa de entrega"""


        bancoDados = open('NOTA_PEDIDO.txt', 'w', newline = '', encoding = 'utf8')
        criarBanco = csv.writer(bancoDados)
        criarBanco.writerow([f'{"QUANT":<6} {" ITEM"} {"PREÇO":>61}'])
        for pos, itens in enumerate(pedidos):
            criarBanco.writerow([f' {quantidadeLista[pos]:^6} {tabelaProduto[itens - 1]["nom"]:.<60} {(float(tabelaProduto[itens - 1]["pre"]) * int(quantidadeLista[pos])):.2f}'])
        criarBanco.writerow([])
        if entrega == False:
            criarBanco.writerow([f'{"        TOTAL":.<65} R$ {(total + float(taxaEntrega)):.2f}'])
            criarBanco.writerow([])
        else:
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
    
    def mostraPedido(entrega = False):
        """Mostra o pedido na tela
        :Param entrega: Verifica se o pedido é para entrega, adicionando o valor da taxa de entrega"""


        system('cls')
        print('''
            
▒█▀▀█ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ █▀▀ 
▒█▄▄█ █▀▀ █░░█ ▀█▀ █░░█ █░░█ ▀▀█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀░ ▀▀▀▀ ▀▀▀
             
*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O CADASTRO ***
''')   
        print()
        print()
        print('=' * 75)
        print(cabecalho)
        print('=' * 75)
        print()
        for pos, itens in enumerate(pedidos):
                print(f'{quantidadeLista[pos]:^6}  {tabelaProduto[itens - 1]["nom"]:.<60} {(float(tabelaProduto[itens - 1]["pre"]) * int(quantidadeLista[pos])):.2f}')
        print()
        if entrega == False:
            print(f'{"        TOTAL":.<65} R$ {(total + float(taxaEntrega)):.2f}')
        if entrega == True:
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
        print()
        

    pedidos = []
    quantidadeLista = []
    taxaEntrega = contador = total = 0
    cabecalho = f'{"QUANT":<6} {" ITEM"} {"PREÇO":>61}'
    verificaTel = False
    
    system('cls')
    print('''     
▒█▀▀█ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ █▀▀ 
▒█▄▄█ █▀▀ █░░█ ▀█▀ █░░█ █░░█ ▀▀█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀░ ▀▀▀▀ ▀▀▀
             
*** DIGITE \033[31mVOLTAR\033[m PARA RETORNAR AO MENU ANTERIOR ***
*** DIGITE \033[31mRESET\033[m PARA RECOMEÇAR O PEDIDO ***
''')   
    while True:
        try:
            codigo = str(input('Código [999 PARA FECHAR O PEDIDO]: ')).upper().strip()
            if codigo in ('RESET', 'VOLTAR', 'VOLTA'):
                retorno('pdv', codigo)
            
            #*** ERRO CASO CÓDIGO SEJA MAIOR QUE A QUANTIDADE DE PRODUTOS ***
            while int(codigo) > len(tabelaProduto) or int(codigo) <= 0:
                if int(codigo) == 999 and len(pedidos) > 0:
                    break
                elif int(codigo) == 999 and len(pedidos) == 0:
                    print('\033[31mVocê deve adicionar itens antes de fechar o pedido.\033[m')
                else:
                    print('\033[31mCódigo não cadastrado.\033[m')
                codigo = str(input('Código [999 PARA FECHAR O PEDIDO]: ')).strip().upper()
                if codigo in ('RESET', 'VOLTAR', 'VOLTA'):
                    retorno('pdv', codigo)
            
            #*** FECHAMENTO DO PEDIDO ***

            if int(codigo) == 999:
                escolha = str(input('Deseja fechar esse pedido? [S/N] ')).strip().upper()
                while escolha not in ('SIM', 'NÃO', 'NAO'):
                    if escolha in ('RESET', 'VOLTAR', 'VOLTA'):
                        retorno('pdv', escolha)
                    print('\033[31mOpção inválida!\033[m')
                    escolha = str(input('Deseja fechar esse pedido? [S/N] ')).strip().upper()
                if escolha in ('NAO', 'NÃO'):
                    continue
                else:
                    entrega = str(input('Entrega? [S/N] ')).strip().upper()
                    while entrega not in ('SIM', 'NAO', 'NÃO'):
                        if entrega in ('RESET', 'VOLTAR', 'VOLTA'):
                            retorno('pdv', entrega)
                        print('\033[31mOpção inválida!\033[m')
                        entrega = str(input('Entrega? [S/N] ')).strip().upper()
                    if entrega in 'SIM':
                        taxaEntrega = str(input('Taxa de entrega: R$ ')).strip().upper()
                        while taxaEntrega == '' or taxaEntrega.isnumeric() == False:
                            if taxaEntrega in ('RESET', 'VOLTAR', 'VOLTA'):
                                retorno('pdv', taxaEntrega)
                            print('\033[31mOpção inválida!\033[m')
                            taxaEntrega = str(input('Taxa de entrega: R$ ')).strip().upper()
                        buscaCliente = str(input('Digite o número de telefone do cliente: ')).strip().upper()
                        while not verificaTel:
                            if buscaCliente in ('RESET', 'VOLTAR', 'VOLTA'):
                                retorno('pdv', buscaCliente)                            
                            for numero in dadosClientes:
                                if numero['tel'] != buscaCliente:
                                    contador += 1
                                if contador > len(dadosClientes):
                                    print('\033[31mNúmero inexistente!\033[m')
                                    buscaCliente = str(input('Digite o número de telefone do cliente: ')).strip().upper()
                                    contador = 0
                                if numero['tel'] == buscaCliente:
                                    verificaTel = True
                        mostraPedido(entrega = True)
                        notaFiscal(entrega = True)
                        imprimir()
                    else:
                        notaFiscal()
                        imprimir()
                        break
                    break
            while True:
                try:
                    quantidade = str(input('Quantidade: ')).strip().upper()
                    if quantidade in ('RESET', 'VOLTAR', 'VOLTA'):
                        retorno('pdv', quantidade)
                    else:
                        quantidade = int(quantidade)
                except (TypeError, ValueError):
                    print('\033[31mInsira uma quantidade válida.\033[m')
                    continue
                else:
                    break
            quantidadeLista.append(quantidade)
            pedidos.append(int(codigo))
            total += float(tabelaProduto[int(codigo) - 1]['pre']) * quantidade
            mostraPedido()
        except:
            print('\033[31mComando não reconhecido. Insira um comando válido!\033[m')
            continue
    pdv()


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
menuPrincipal()

