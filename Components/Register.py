import locale
from hashlib import sha256
import socket
import pwinput

# ------------------------------ PEGAR DADOS BASICOS/TRANSFORMAR SENHA EM HASH/PEGAR IDIOMA ------------------------------

Nome = input("\nInsira seu Nome de Usuario: ")
Email = input("Digite se Email: ")
SenhaUser = pwinput.pwinput("Insira uma Senha: ",  mask="*")

sha256_hash = sha256()
sha256_hash.update(SenhaUser.encode('utf-8'))
Senha_Hash = sha256_hash.hexdigest()

idioma, _ = locale.getlocale()

# ------------------------------ PEGAR IP DA MAQUINA ------------------------------

#Pegar IP
def pegar_ip():
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        # Conecta-se a um servidor qualquer
        s.connect(('8.8.8.8', 80))
    
        # Obtém o endereço IP do socket
        ip_address = s.getsockname()[0]

        s.close()
        
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")
        ip_address = None
        
    finally:
        # Fecha o socket
        s.close()
    
    return ip_address

EnderecoIP = pegar_ip()




