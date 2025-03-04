import json
from Components.Register import *

dados = {
    "nome": Nome,
    "email": Email,
    "senha": Senha_Hash,
    "enderecoip": Endereco_IP,
    "idioma": idioma
}

with open("data.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)