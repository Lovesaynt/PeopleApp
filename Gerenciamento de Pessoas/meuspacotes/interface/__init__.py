# INTERFACE

def cabeçalho(name):
    '''
    Docstring [CABEÇALHO]
    
    Name: Recebe o Título do Cabeçalho
    '''
    linhas = '\033[1;35;40m=\033[0m' * 60
    print(f'{linhas}\n{name}\n{linhas}')



def menu(options):
    '''
    Docstring [MENU]
    
    Options: Recebe uma Lista com textos para opções no menu.
    '''
    painel = []
    painel.append(options)
    cabeçalho(f'{'\033[1;32mGERENCIAMENTO DE PESSOAS':^60}')

    for pos, opcs in enumerate (painel[0]):
        print(f'{pos+1}) {opcs}', flush=True)
        if pos+1 == len(painel[0]):
            print('\033[1;35;40m=\033[0m' * 60)
