# ARQUIVOS
import os
import sys
import shutil
from time import sleep
from pathlib import Path

# Nome da pasta onde o arquivo gravável ficará em Documents
_APP_FOLDER_NAME = 'PessoaApp'  # você pode mudar para o nome que preferir
_ARCHIVE_NAME = 'pessoas.txt'

if getattr(sys, 'frozen', False):
    # rodando como .exe
    DIRETORIO_BASE = os.path.dirname(sys.executable)
else:
    # rodando como script .py
    DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))

def _get_bundle_base():
    """
    Retorna a pasta base onde recursos embutidos estão localizados.
    Funciona tanto no modo desenvolvimento quanto quando executado como exe PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def _ensure_documents_data_folder(app_folder_name=_APP_FOLDER_NAME):
    """
    Garante que exista uma pasta em Documents para armazenar arquivos graváveis do app.
    Retorna o caminho absoluto da pasta (string).
    """
    target_dir = Path.home() / 'Documents' / app_folder_name
    target_dir.mkdir(parents=True, exist_ok=True)
    return str(target_dir)

def _ensure_writable_archive():
    """
    Garante que exista uma cópia gravável de `_ARCHIVE_NAME` dentro de Documents/_APP_FOLDER_NAME.
    - Se o recurso estiver embutido no bundle (PyInstaller), copia do bundle para Documents.
    - Se estiver executando em modo script e não houver arquivo em Documents, cria um arquivo vazio lá.
    Retorna o caminho absoluto do arquivo gravável (string).
    """
    dest_dir = _ensure_documents_data_folder()
    dest_path = os.path.join(dest_dir, _ARCHIVE_NAME)

    # caminho do recurso no bundle ou no diretório do script
    src_base = _get_bundle_base()
    src_path = os.path.join(src_base, _ARCHIVE_NAME)

    # se ainda não existe a cópia em Documents, tente copiar do bundle/script
    if not os.path.isfile(dest_path):
        try:
            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
                sleep(0.5)
                print(f'\033[1;33;40m\nArquivo encontrado no bundle.\nCopiado para:\n{dest_path}\033[0m')
            else:
                # cria arquivo vazio em Documents se não houver fonte para copiar
                with open(dest_path, 'w', encoding='utf-8') as f:
                    pass
                sleep(0.5)
                print(f'\033[1;32mArquivo não encontrado no bundle.\nNovo arquivo criado em:\n{dest_path}\033[0m')
        except Exception as e:
            # se algo falhar, tenta criar um arquivo vazio mesmo assim
            try:
                with open(dest_path, 'w', encoding='utf-8') as f:
                    pass
                sleep(0.5)
                print(f'\033[1;32mNão foi possível copiar do bundle:\n{e}\nCriado novo arquivo em: {dest_path}\033[0m')
            except Exception as e2:
                # falha criando arquivo; informa o usuário e retorna caminho (vai falhar depois ao abrir)
                sleep(0.5)
                print(f'\033[1;37;41mERRO!\nAo criar arquivo em:\nDocuments: {e2}\033[0m')

    return dest_path

# Diretorio base alterado: agora aponta para a pasta em Documents/PessoaApp (gravável)
DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
try:
    # tenta definir DIRETORIO_BASE como a pasta em Documents onde o arquivo será gravado
    writable_archive = _ensure_writable_archive()
    DIRETORIO_BASE = os.path.dirname(os.path.abspath(writable_archive))
except Exception:
    # fallback: manter o comportamento antigo (pasta do script)
    DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))

def arquivoExiste(name):
    """
Check whether a file exists.

This function verifies if a given file name corresponds to an existing
file in the program's directory. It returns True if the file exists;
otherwise, it prints a warning message indicating that the file was not found.

Parameters
----------
name : str
    Name of the file to be checked.

Returns
-------
bool
    True if the file exists. False otherwise.

Raises
------
None
    """

    caminho = os.path.join(DIRETORIO_BASE, name)
    if os.path.isfile(caminho):
        return True
    else:
        print('Arquivo não Encontrado!\nIniciando Criação...')


def criarArquivo(name):
    """
Create a new text file in the program's directory.

This function attempts to create an empty `.txt` file with the given name.
If the file already exists, it will be overwritten. If creation fails,
an error message is displayed.

Parameters
----------
name : str
    Name of the file to be created.

Returns
-------
None
    The function does not return a value; it only creates the file.

Raises
------
OSError
    If the file cannot be created or written.
    """

    caminho = os.path.join(DIRETORIO_BASE, name)
    try:
        with open (caminho,'w') as a:
            pass
    except Exception as e:
        print(f'Erro ao criar o Arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!')


def lerArquivo(name):
    """
Read and display a formatted list of registered people.

This function opens the specified `.txt` file, reads all stored entries,
and prints each person's ID, name, and age in a structured format.
It does not modify the file’s content.

Parameters
----------
name : str
    Name of the `.txt` file to be read.

Returns
-------
None
    This function does not return a value; it only prints formatted output.

Raises
------
OSError
    If the file cannot be opened or read.
    """

    caminho = os.path.join(DIRETORIO_BASE, name)
    try:
        with open (caminho,'r') as arquivo:
            conteudo = arquivo.readlines()
    except Exception as e:
        sleep(0.5)
        print(f'Erro ao Ler o Arquivo {e}!')
    else:
        pos = 0
        for linha in conteudo:
            pos += 1
            dado = linha.split(';')
            sleep(0.5)
            print(f'\033[1;37m{pos:<5}{dado[0]:<20}{dado[1]:>5}\033[0m', flush=True)
        print()
    

def cadastrarPessoa(archive,
                     name='Desconhecido',
                       idade=0,
                         peso=0,
                           altura=0,
                             nacionalidade='Não Informada',
                               sexo='Não Informado',
                                 civil='Não Informado'):
    """
Register Person

Parameters
----------
archive : str
    Name of the `.txt` file where the data will be written.
name : str
    Name of the registered user.
idade : int
    User's age as an integer value.
peso : float
    User's weight as a decimal value.
altura : float
    User's height as a decimal value.
nacionalidade : str
    User's nationality.
sexo : str
    User's sex.
civil : str
    User's marital status.

Returns
-------
None
    This function does not return a value; it only writes the data to the specified file.
    """

    caminho = os.path.join(DIRETORIO_BASE, archive)
    try:
        a = open(caminho,'at')
    except:
        sleep(0.5)
        print('Erro na Abertura do Arquivo!')
    else:
        try:
            a.write(f'{name};{idade};{peso};{altura};{sexo};{civil};{nacionalidade};\n')
        except:
            sleep(0.5)
            print('Erro ao Cadastrar a Pessoa!')
        else:
            sleep(0.5)
            print(f'\033[1;33;40m{name} foi Adicionado a Lista com Sucesso!\033[0m')


FIELDS = ['Nome', 'Idade', 'Peso', 'Altura', 'Sexo', 'Estado Civíl', 'Nacionalidade']


def _load_people(archive):
    """
Load all registered people from a text file.

This function reads each line of the specified `.txt` file, splits the fields,
and returns a list of people, where each person is represented as a list of values.

Parameters
----------
archive : str
    Name of the `.txt` file to be read.

Returns
-------
list of list of str
    A list containing all people stored in the file. Each inner list represents
    a single person and contains their respective data fields.

Raises
------
OSError
    If the file cannot be opened or read.
    """
    caminho = os.path.join(DIRETORIO_BASE, archive)
    people = []

    with open(caminho, 'r', encoding='utf-8') as f:
        for line in (l.strip() for l in f):
            if not line:
                continue
            parts = line.split(';')
            if parts and parts[-1] == '':
                parts = parts[:-1]
            if len(parts) < len(FIELDS):
                parts += [''] * (len(FIELDS) - len(parts))
            people.append(parts[:len(FIELDS)])
    return people


def _save_people(archive, people):
    """
Save all people to a text file.

This function receives a list of people (each person represented as a list of
data fields) and overwrites the target file with the updated content.

Parameters
----------
archive : str
    Name of the `.txt` file where the data will be written.
people : list of list of str
    The updated list of people to be saved. Each inner list contains the
    data fields of a single person.

Returns
-------
None
    This function does not return a value; it writes the updated data to the file.

Raises
------
OSError
    If the file cannot be created or written.
    """

    caminho = os.path.join(DIRETORIO_BASE, archive)
    with open(caminho, 'w', encoding='utf-8') as f:
        for p in people:
            p_fixed = list(p)
            while len(p_fixed) < len(FIELDS):
                p_fixed.append('')
            p_fixed = p_fixed[:len(FIELDS)]
            p_fixed = [str(x) for x in p_fixed]
            f.write(f'{p_fixed[0]};{p_fixed[1]};{p_fixed[2]};{p_fixed[3]};{p_fixed[4]};{p_fixed[5]};{p_fixed[6]};\n')

def editarPessoa(archive, id):
    """
Edit an existing person in the registry.

This function allows modifying one or more fields of a person identified by
their position (ID) in the file. The function loads the people list, updates
the selected entry, and then saves the modified list.

Parameters
----------
archive : str
    Name of the `.txt` file where the data is stored.
id : int
    The position (1-based index) of the person to be edited.

Returns
-------
None
    This function does not return a value; it updates the file with the edited data.

Raises
------
ValueError
    If the provided ID is not a valid integer or does not match any entry.
OSError
    If the file cannot be read or written.
    """

    try:
        idx = int(id)
    except Exception:
        sleep(0.5)
        print('\033[1;37;41mID inválido.\033[0m')
        return

    people = _load_people(archive)
    if not people:
        sleep(0.5)
        print('\033[1;37;41mNenhuma pessoa cadastrada ou arquivo não existe.\033[0m')
        return

    if idx < 1 or idx > len(people):
        sleep(0.5)
        print('\033[1;37;41mPosição fora do intervalo.\033[0m')
        return

    person = people[idx - 1]

    tipos = {
        'idade': int,
        'peso': float,
        'altura': float,
        'name': str,
        'sexo': str,
        'civil': str,
        'nacionalidade': str
    }
    sleep(0.5)
    print('\033[1;35mEntrando em modo de edição.\nPara manter o valor atual, pressione ENTER.\033[0m')
    while True:
        sleep(0.5)
        print(f'\033[1;37;45m{'Dados Atuais':-^60}\033[0m')
        for i, field in enumerate(FIELDS, start=1):
            sleep(0.5)
            print(f'\033[1;37m{i}) {field}: {person[i-1]}\033[0m', flush=True)
        sleep(0.5)
        print(f'\033[1;37;45m{'-' * 60}\033[0m')
        sleep(0.5)
        escolha = input('\033[1;32;40mDigite o número do campo que deseja alterar!\033[0m\n\033[1;31m[Sair = 0]: \033[0m').strip()
        if escolha == '0':
            break
        try:
            campo_idx = int(escolha) - 1
        except ValueError:
            sleep(0.5)
            print('\033[1;37;41mEscolha inválida.\033[0m')
            continue
        if campo_idx < 0 or campo_idx >= len(FIELDS):
            sleep(0.5)
            print('\033[1;37;41mCampo inválido.\033[0m')
            continue

        campo = FIELDS[campo_idx]
        sleep(0.5)
        novo = input(f"\033[1;33mNovo valor para: {campo}\033[0m\n\033[1;31m(Vazio Para Manter '{person[campo_idx]}'): \033[0m").strip()
        if novo == '':
            sleep(0.5)
            print('Mantendo valor atual.')
            continue

        tipo_esperado = tipos.get(campo, str)
        try:
            if tipo_esperado is int:
                convertido = int(novo)
            elif tipo_esperado is float:
                convertido = float(novo)
            else:
                convertido = novo
        except ValueError:
            sleep(0.5)
            print(f'\033[1;31mValor inválido para o campo {campo}.\nEsperado tipo: {tipo_esperado.__name__}.\nAlteração ignorada.\033[0m')
            continue

        person[campo_idx] = str(convertido)
        sleep(0.5)
        print(f"\033[1;32m{campo} Atualizado para: {person[campo_idx]}")

    people[idx - 1] = person
    _save_people(archive, people)
    sleep(0.5)
    print('Alterações salvas.')


def apagarPessoa(archive, id):
    """
Delete a person from the registry.

This function removes the person located at the specified ID (1-based index)
from the list of people and then overwrites the file with the remaining entries.

Parameters
----------
archive : str
    Name of the `.txt` file where the data is stored.
id : int
    The position (1-based index) of the person to be removed.

Returns
-------
None
    This function does not return a value; it updates the file after deleting the entry.

Raises
------
ValueError
    If the provided ID is invalid or does not correspond to any stored person.
OSError
    If the file cannot be accessed or written.
    """

    try:
        idx = int(id)
    except Exception:
        sleep(0.5)
        print('ID inválido.')
        return

    people = _load_people(archive)
    if not people:
        sleep(0.5)
        print('Nenhuma pessoa cadastrada ou arquivo não existe.')
        return

    if idx < 1 or idx > len(people):
        sleep(0.5)
        print('Posição fora do intervalo.')
        return

    person = people[idx - 1]
    sleep(0.5)
    print('\033[1;31mVocê selecionou para apagar:\033[0m')
    for f, v in zip(FIELDS, person):
        sleep(0.5)
        print(f'\033[1;37;40m{f}: {v}\033[0m', flush=True)
    sleep(0.5)
    confirm = input('\033[1;33mConfirmar Exclusão? (S/N): \033[0m').strip().lower()
    if confirm != 's':
        sleep(0.5)
        print('\033[1;31mExclusão Cancelada.\033[0m')
        return

    del people[idx - 1]
    _save_people(archive, people)
    sleep(0.5)
    print('\033[1;32mPessoa Apagada com Sucesso.\033[0m')


def exibirPessoa(archive, id):
    """
Display detailed information of a selected person.

This function retrieves a person from the registry using their ID
(1-based index) and prints all stored fields in a formatted layout.

Parameters
----------
archive : str
    Name of the `.txt` file where the data is stored.
id : int
    The position (1-based index) of the person to be displayed.

Returns
-------
None
    This function does not return a value; it only prints the selected
    person's information to the console.

Raises
------
ValueError
    If the provided ID is invalid or outside the range of registered people.
OSError
    If the file cannot be read.
    """

    pessoas = _load_people(archive)
    if not pessoas:
        sleep(0.5)
        print('\033[1;31mNenhuma Pessoa Cadastrada.\033[0m')
        return

    try:
        idx = int(id)
    except:
        sleep(0.5)
        print('\033[1;31mID inválido.\033[0m')
        return

    if idx < 1 or idx > len(pessoas):
        sleep(0.5)
        print('\033[1;31mPosição fora do intervalo.\033[0m')
        return

    p = pessoas[idx - 1]

    labels = ['Nome', 'Idade', 'Peso', 'Altura', 'Sexo', 'Estado Civil', 'Nacionalidade']

    print(f'\033[1;37m\nDetalhes da Pessoa #{idx}:')
    print(f'\033[1;37;40m{'-' * 60}\033[0m')
    for label, value in zip(labels, p):
        sleep(0.5)
        print(f'\033[1;37m{label}: {value}\033[0m', flush=True)
    print(f'\033[1;37;40m{'-' * 60}\033[0m')
