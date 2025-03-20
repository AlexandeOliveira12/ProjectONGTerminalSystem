import json
from Components.Register import *

# ------------------------------ INSERIR DADOS JSON ------------------------------

dados = {
    "name": Nome,
    "email": Email,
    "password": senha_hash_base64,
    "language": idioma
}
    
# Ler os dados existentes
try:
    with open("./Data/data.json", "r", encoding="utf-8") as arquivo:
        data = json.load(arquivo)  # Carregar a lista existente
except (FileNotFoundError, json.JSONDecodeError):
    data = []  # Criar uma nova lista se o arquivo estiver vazio ou não existir

# Adicionar o novo usuário
data.append(dados)

# Salvar de volta no arquivo
with open("./Data/data.json", "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, ensure_ascii=False, indent=4)
    
    
# ------------------------------ ############### ------------------------------