import sys
import locale
import base64
import bcrypt

# Detecta sistema operacional
import os
if os.name == 'nt':  # Windows
    import msvcrt
else:  # Unix (Linux/Mac)
    import tty
    import termios

# ------------------------------ FUNÇÃO PARA MASCARAR A SENHA ------------------------------
def mascarar_senha(prompt="Senha: ", mask="*"):
    print(prompt, end='', flush=True)
    senha = ""
    if os.name == 'nt':  # Windows
        while True:
            ch = msvcrt.getch()
            if ch in {b'\r', b'\n'}:
                print()
                break
            elif ch == b'\x08':  # Backspace
                if len(senha) > 0:
                    senha = senha[:-1]
                    print('\b \b', end='', flush=True)
            elif ch == b'\x03':  # Ctrl+C
                raise KeyboardInterrupt
            else:
                senha += ch.decode('utf-8')
                print(mask, end='', flush=True)
    else:  # Unix (Linux/Mac)
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                ch = sys.stdin.read(1)
                if ch in {'\r', '\n'}:
                    print()
                    break
                elif ch == '\x7f':  # Backspace
                    if len(senha) > 0:
                        senha = senha[:-1]
                        print('\b \b', end='', flush=True)
                elif ch == '\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                else:
                    senha += ch
                    print(mask, end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return senha

# ------------------------------ PEGAR DADOS BASICOS ------------------------------
Nome = input("\nInsira seu Nome de Usuario: ")
Email = input("Digite seu Email: ")
SenhaUser = mascarar_senha("Insira uma Senha: ", mask="*")

# ------------------------------ CRIAR HASH COM BCRYPT ------------------------------
def gerar_hash_bcrypt(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash

def hash_para_base64(senha_hash):
    return base64.b64encode(senha_hash).decode('utf-8')

senha_hash = gerar_hash_bcrypt(SenhaUser)
senha_hash_base64 = hash_para_base64(senha_hash)
