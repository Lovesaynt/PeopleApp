from meuspacotes.interface import *
from meuspacotes.arquivos import *
from time import sleep

# Arquivo Principal, Mude-o para o nome que achar melhor!
arch = "Pessoas.txt"

if not arquivoExiste(arch):
    criarArquivo(arch)

# Menu principal de opções.
options = ['\033[1;33mExibir Pessoas Cadastradas\033[0m',
           '\033[1;33mCadastrar Nova Pessoa\033[0m',
           '\033[1;33mEditar Pessoa Cadastrada\033[0m',
           '\033[1;33mApagar Pessoa Cadastrada\033[0m',
           '\033[1;33mExibir Detalhes da Pessoa\033[0m',
           '\033[1;31mSair\033[0m']

# Programa Principal
while True:
    menu(options)
    sleep(0.5)
    while True:
        try:
            escolha = int(input('\033[1;33mOpção: \033[0m'))
        except Exception:
            print('\033[1;37;41mERRO! Valor Inválido.\033[0m')
            continue
        if not 1 <= escolha <= len(options):
            sleep(0.5)
            print('\033[1;37;41mOpção Inválida!\033[0m')
            continue
        else:
            break

    if escolha == 1:
        sleep(0.5)
        cabeçalho(f'\033[1;32m{'PESSOAS CADASTRADAS\033[0m':^60}')
        sleep(0.5)
        print(f'{'\033[1;36;40mID':<14}|{'NOME':<20}|{'IDADE':>5}|\033[0m')
        lerArquivo(arch)

    if escolha == 2:
        sleep(0.5)
        cabeçalho(f'\033[1;32m{'CADASTRAR NOVA PESSOA\033[0m':^60}')

        sleep(0.5)
        while True:
            nome = str(input('\033[1;32mNome: \033[0m')).strip().title()
            if nome == '':
                print('\033[1;37;41mERRO! Campo Vazio.\033[0m')
                continue

            if not all(c.isalpha() or c.isspace() for c in nome):
                print('\033[1;37;41mERRO! Nome Inválido.\033[0m')
                continue
            break

        sleep(0.5)
        while True:
            try:
                idade_raw = input('\033[1;32mIdade: \033[0m').strip()
                idade = int(idade_raw)
                if idade < 0:
                    print('\033[1;37;41mErro: idade deve ser >= 0.\033[0m')
                    continue
                break
            except ValueError:
                print('\033[1;37;41mErro! Idade inválida. Digite um número inteiro.\033[0m')
                continue

        sleep(0.5)
        while True:
            sexo = str(input('\033[1;32mSexo [M/F]: \033[0m')).strip().upper()[0]
            if sexo not in ('M', 'F',''):
                print('\033[1;37;41mERRO! Insira um Sexo Válido.\n(Vazio para Outros)\033[0m')
                continue
            break

        sleep(0.5)
        while True:
            civil_raw = input('\033[1;32mEstado Civíl: \033[0m').strip()
            if civil_raw == '':
                civil = 'Não Informado'
                break
            civil = civil_raw.title()
            if not all(c.isalpha() or c.isspace() for c in civil):
                print('\033[1;37;41mERRO! Entrada Inválida.\033[0m')
                continue
            break
        sleep(0.5)
        while True:
            try:
                altura_raw = input('\033[1;32mAltura: \033[0m').strip()
                altura = float(altura_raw)
                if altura < 0:
                    print('\033[1;37;41mErro: altura deve ser >= 0.\033[0m')
                    continue
                break
            except ValueError:
                print('\033[1;37;41mErro! Altura inválida. Use ponto como separador decimal.\033[0m')
                continue

        sleep(0.5)
        while True:
            try:
                peso_raw = input('\033[1;32mPeso: \033[0m').strip()
                peso = float(peso_raw)
                if peso < 0:
                    print('\033[1;37;41mERRO! Peso Inválido.\033[0m')
                    continue
                break
            except ValueError:
                print('\033[1;37;41mERRO! Valor Inváliido.\033[0m')
                continue

        sleep(0.5)
        while True:
            nac_raw = input('\033[1;32mNacionalidade: \033[0m').strip()
            if nac_raw == '':
                nacionalidade = 'Não Informada'
                break
            nacionalidade = nac_raw.title()
            if not all(c.isalpha() or c.isspace() for c in nacionalidade):
                print('\033[1;37;41mERRO! Entrada Inválida.\033[0m')
                continue
            break

        cadastrarPessoa(arch, nome, idade, peso, altura, nacionalidade, sexo, civil)

    if escolha == 3:
        sleep(0.5)
        cabeçalho(f'\033[1;32m{'EDITAR PESSOA CADASTRADA':^60}\033[0m')
        sleep(0.5)

        try:
            select_raw = input('\033[1;33mID da Pessoa: \033[0m').strip()
            select = int(select_raw)
        except ValueError:
            print('\033[1;37;41mERRO! ID inválido.\033[0m')
        else:
            editarPessoa(arch, select)

    if escolha == 4:
        sleep(0.5)
        cabeçalho(f'\033[1;32m{'APAGAR PESSOA CADASTRADA':^60}\033[0m')
        sleep(0.5)

        try:
            select_raw = input('\033[1;33mID da Pessoa: \033[0m').strip()
            select = int(select_raw)
        except ValueError:
            print('\033[1;37;41mERRO! ID inválido.\033[0m')
        else:
            apagarPessoa(arch, select)
    
    if escolha == 5:
        sleep(0.5)
        cabeçalho(f'\033[1;32m{'EXIBIR PESSOA CADASTRADA':^60}\033[0m')
        sleep(0.5)

        try:
            select_raw = input('\033[1;33mID da Pessoa: \033[0m').strip()
            select = int(select_raw)
        except ValueError:
            print('\033[1;37;41mERRO! ID inválido.\033[0m')
        else:
            exibirPessoa(arch, select)

    if escolha == 6:
        f = f'\033[1;31m{'Fechando o Programa!'}\033[0m'
        for w in f:
            sleep(0.2)
            print(w, end='', flush=True)
        break