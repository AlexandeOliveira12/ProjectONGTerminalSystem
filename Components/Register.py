import locale
from hashlib import sha256
import socket
import pwinput

#Pega dados basicos
Nome = input("\nInsira seu Nome de Usuario: ")
Email = input("Digite se Email: ")
SenhaUser = pwinput.pwinput("Insira uma Senha: ",  mask="*")

#Transforma a senha em Hash
sha256_hash = sha256()
sha256_hash.update(SenhaUser.encode('utf-8'))
Senha_Hash = sha256_hash.hexdigest()

#Pega o Idioma
idioma, _ = locale.getlocale()

#Pegar IP
def pegar_ip():
    try:
        # Cria um socket para obter o endereço IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        # Conecta-se a um servidor qualquer (não importa o endereço ou a porta)
        s.connect(('8.8.8.8', 80))
    
        # Obtém o endereço IP do socket
        ip_address = s.getsockname()[0]

        s.close()
        
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")
        ip_address = None
        
    finally:
        # Fecha o socket para liberar recursos
        s.close()
    
    return ip_address

EnderecoIP = pegar_ip()




