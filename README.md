# PeopleApp — Gerenciador de Pessoas (CLI)

![status](https://badgen.net/badge/status/active/green?)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![build](https://img.shields.io/badge/build-PyInstaller-orange)

PeopleApp é uma aplicação de linha de comando desenvolvida em Python para gerenciar um registro de pessoas usando um arquivo `.txt`.  
O programa permite cadastrar, listar, editar, exibir e excluir pessoas de forma simples e eficiente, incluindo criação automática do arquivo.

## Um pequeno projeto feito no primórdio do meu aprendizado em Python!
Sei que tem muitas imperfeições, porém irei manter assim como uma memória do meu começo.

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
## 📁 Estrutura do Projeto
```bash
PessoaApp/
│
├── pplmanager.py          → Script principal
├── arquivos               → Funções de CRUD e manipulação de arquivos
└── pessoas.txt            → Criado automaticamente
```
## 🛠 Tecnologias Utilizadas
```bash
⦁	Python 3

⦁	PyInstaller

⦁	Manipulação de arquivos TXT
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
```bash
Developed_By = {
    Lovesaynt.
}

```
