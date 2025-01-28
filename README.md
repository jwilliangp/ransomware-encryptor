# Encrypter & Decrypter

Este projeto consiste em dois scripts Python para criptografar e descriptografar arquivos de texto utilizando o algoritmo AES no modo CTR. É ideal para quem deseja entender como criptografar arquivos de forma simples, implementando suas próprias chaves de criptografia.

## 🚀 Funcionalidade

**Encrypter (encrypter.py)**: Criptografa arquivos .txt no diretório atual, gerando uma versão criptografada com a extensão .txt.ransomware.

**Decrypter (decrypter.py)**: Descriptografa arquivos .txt.ransomware, restaurando os arquivos originais.

## 🔐 Como Funciona

Ambos os scripts utilizam o algoritmo AES com a chave fixa `testeransomwares` no modo CTR.

- O **encrypter** lê arquivos .txt, criptografa seu conteúdo, salva como um novo arquivo .ransomware e exclui o arquivo original.
- O **decrypter** lê arquivos .ransomware, descriptografa e restaura os arquivos para o formato .txt.

## 🚀 Como Rodar

### Pré-requisitos:
- Python 3.x
- Biblioteca `pyaes`

### Passos para rodar:

1. Clone este repositório:

    ```bash
    git clone https://github.com/usuario/nome-do-repositorio.git
    ```

2. Instale a dependência `pyaes`:

    ```bash
    pip install pyaes
    ```

3. Execute os scripts:

    Para criptografar os arquivos de teste:

    ```bash
    python encrypter.py
    ```

    Para descriptografar os arquivos:

    ```bash
    python decrypter.py
    ```

Os arquivos de teste serão criados automaticamente pelo script `test_files` em .txt. Depois de rodar o `encrypter.py`, os arquivos criptografados terão a extensão `.txt.ransomware` e poderão ser restaurados com o `decrypter.py`.

## 🛠️ Tecnologias

- **Python 3.x**: Linguagem de programação utilizada para desenvolver o projeto.
- **pyaes**: Biblioteca Python para criptografia AES.

## 📚 Projeto do Santander Cibersegurança Bootcamp

Este projeto foi desenvolvido como parte do curso **Santander Cibersegurança Bootcamp**, com o objetivo de aplicar conceitos de criptografia e segurança em arquivos de forma prática.

## ⚠️ Aviso Importante

Este é um código de exemplo de como criptografar e descriptografar arquivos, não é recomendado para uso em produção sem validações adicionais de segurança e gerenciamento de chaves. O uso desse tipo de criptografia em dados sensíveis deve ser feito com precaução e com o uso de boas práticas de segurança.
