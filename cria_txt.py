import os

test_files = {
    "senhas.txt": "Senha1: abc123\nSenha2: 12345\nSenha3: qwerty\nSenha4: senha_segura123",
    "contas_bancarias.txt": "Banco: ABC\nConta: 12345-6\nAgência: 7890\nSaldo: R$ 12.345,67",
    "notas.txt": "Nota 1: Comprar pão\nNota 2: Estudar Python\nNota 3: Pagar contas",
    "informacoes_pessoais.txt": "Nome: José da Silva\nCPF: 123.456.789-00\nEndereço: Rua Fictícia, 123",
    "emails.txt": "Email 1: jose@gmail.com\nEmail 2: maria@yahoo.com\nEmail 3: teste@empresa.com"
}

for file_name, content in test_files.items():
    with open(file_name, "w") as file:
        file.write(content)

print("Arquivos de teste criados com sucesso!")
