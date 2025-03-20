import locale
import bcrypt
import pwinput
import base64

# ------------------------------ PEGAR DADOS BASICOS/TRANSFORMAR SENHA EM HASH/PEGAR IDIOMA ------------------------------

Nome = input("\nInsira seu Nome de Usuario: ")
Email = input("Digite se Email: ")
SenhaUser = pwinput.pwinput("Insira uma Senha: ",  mask="*")

def gerar_hash_bcrypt(SenhaUser):
    # Gera o salt aleatorio
    salt = bcrypt.gensalt()
    
    # Gera o hash da senha com o salt
    senha_hash = bcrypt.hashpw(SenhaUser.encode('utf-8'), salt) 
    
    return senha_hash

# Função para converter o hash para base64
def hash_para_base64(senha_hash):
    return base64.b64encode(senha_hash).decode('utf-8')

senha_hash = gerar_hash_bcrypt(SenhaUser)
senha_hash_base64 = hash_para_base64(senha_hash)

idioma, _ = locale.getlocale()