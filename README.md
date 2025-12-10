# PessoaApp — Gerenciador de Pessoas (CLI)

![status](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![build](https://img.shields.io/badge/build-PyInstaller-orange)

PessoaApp é uma aplicação de linha de comando desenvolvida em Python para gerenciar um registro de pessoas usando um arquivo `.txt`.  
O programa permite cadastrar, listar, editar, exibir e excluir pessoas de forma simples e eficiente, incluindo criação automática do arquivo e diretório necessários.

---
### **Menu Principal**
```bash
1 - Listar Pessoas
2 - Cadastrar Pessoa
3 - Editar Pessoa
4 - Apagar Pessoa
5 - Exibir Detalhes
6 - Sair
```

### **Cadastro**
```bash
Nome: João Silva
Idade: 28
Sexo [M/F]: M
Estado Civil: Solteiro
Altura: 1.75
Peso: 70
Nacionalidade: Brasileira
```

### **Edição**

Entrando em modo de edição.
Para manter o valor atual, pressione ENTER.
```bash
1) Nome: João Silva
2) Idade: 28
3) Peso: 70.0
(...)
```
### **Exclusão**
```bash
Você selecionou para apagar:
Nome: João Silva
Idade: 28
(...)
Confirmar Exclusão? (S/N):
```
---

## 🗂 Estrutura de Armazenamento

O programa cria automaticamente:
```bash
C:\Users<Usuário>\Documents\PessoaApp
│
└── pessoas.txt

Formato de cada linha:
Nome;Idade;Peso;Altura;Sexo;Estado Civil;Nacionalidade;
```
---

## 🚀 Como Executar via Python

Se estiver usando o código-fonte, execute:

```bash
python pplmanager.py
```

## 📦 Como Gerar o Executável (PyInstaller)
```bash
pyinstaller --onefile --console --name PessoaApp pplmanager.py
```
Após gerar:
```bash
dist/PessoaApp.exe
```
Ao abrir, ele criará automaticamente a pasta PessoaApp em Documents.

## 📁 Estrutura do Projeto
```bash
PessoaApp/
│
├── pplmanager.py          → Script principal
├── arquivo.py             → Funções de CRUD e manipulação de arquivos
└── pessoas.txt            → Criado automaticamente
```
## 🛠 Tecnologias Utilizadas
```bash
⦁	Python 3

⦁	PyInstaller

⦁	Manipulação de arquivos TXT

⦁	Cores ANSI no terminal
```
## ⚙️ Como Usar o Programa

### Menu
```bash
Digite o número da opção desejada.
```
### Cadastro
```bash
Digite todas as informações solicitadas.
Campos inválidos são rejeitados automaticamente.
```
### Editar
```bash
Selecione um ID → escolha um campo → altere.
Pressione ENTER para manter o valor atual.
```
### Excluir
```bash
Selecione um ID.
Confirme com "S" para apagar.
```
### Exibir
```bash
Mostra todos os dados da pessoa selecionada.
```
## 🔐 Tratamento de Erros

### Inclui:
```bash
⦁	Digitação incorreta no menu

⦁	Letras onde números deveriam estar

⦁	IDs fora do intervalo

⦁	Arquivo inexistente (criação automática)

⦁	Diretório inexistente (criação automática)

⦁	Campos numéricos inválidos

⦁	Valores vazios preservam o original
```
## 📄 Licença
```bash
Este projeto é distribuído sob a licença MIT.
```
## 🤝 Contribuições
```bash
Relatórios de bugs, sugestões e pull requests são bem-vindos.
```
## 📜 Changelog
v1.0.0
```bash
- Primeira versão estável
- CRUD completo
- Edição interativa
- Criação automática de diretório e arquivo
- Versão .exe funcional via PyInstaller
```
✨ Autor
```bash
Developed_By = {
    Lovesaynt.
}

```
