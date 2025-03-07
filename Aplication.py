import json
from Components.Register import *

# ------------------------------ INSERIR DADOS JSON ------------------------------

dados = {
    "name": Nome,
    "email": Email,
    "password": Senha_Hash,
    "language": idioma,
    "addressip": EnderecoIP
}
    
# Ler os dados existentes
try:
    with open("data.json", "r", encoding="utf-8") as arquivo:
        data = json.load(arquivo)  # Carregar a lista existente
except (FileNotFoundError, json.JSONDecodeError):
    data = []  # Criar uma nova lista se o arquivo estiver vazio ou não existir

# Adicionar o novo usuário
data.append(dados)

# Salvar de volta no arquivo
with open("data.json", "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, ensure_ascii=False, indent=4)
    
    
# ------------------------------ ############### ------------------------------