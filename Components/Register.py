import sys
import base64
import bcrypt
import os
import json

# Detectar sistema operacional
if os.name == 'nt':  # Windows
    import msvcrt
else:  # Unix
    import tty
    import termios

# ---------------------- MASCARAR SENHA ----------------------
def mascarar_senha(prompt="Senha: ", mask="*"):
    print(prompt, end='', flush=True)
    senha = ""
    if os.name == 'nt':
        while True:
            ch = msvcrt.getch()
            if ch in {b'\r', b'\n'}:
                print()
                break
            elif ch == b'\x08':
                if len(senha) > 0:
                    senha = senha[:-1]
                    print('\b \b', end='', flush=True)
            elif ch == b'\x03':
                raise KeyboardInterrupt
            else:
                senha += ch.decode('utf-8')
                print(mask, end='', flush=True)
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in {'\r', '\n'}:
                    print()
                    break
                elif ch == '\x7f':
                    if len(senha) > 0:
                        senha = senha[:-1]
                        print('\b \b', end='', flush=True)
                elif ch == '\x03':
                    raise KeyboardInterrupt
                else:
                    senha += ch
                    print(mask, end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return senha

# ---------------------- HASH ----------------------
def gerar_hash_bcrypt(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash

def hash_para_base64(senha_hash):
    return base64.b64encode(senha_hash).decode('utf-8')

def verificar_senha(senha_digitada, senha_hash_base64):
    senha_hash = base64.b64decode(senha_hash_base64.encode('utf-8'))
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_hash)

# ---------------------- VERIFICAR OU CRIAR USUÁRIO ----------------------
def login_ou_cadastro():
    Nome = input("\nInsira seu Nome de Usuário: ")
    Email = input("Digite seu Email: ")

    try:
        with open("./Data/data.json", "r", encoding="utf-8") as arquivo:
            data = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    for usuario in data:
        if usuario["name"] == Nome and usuario["email"] == Email:
            print("\n🔐 Usuário encontrado. Faça login:")
            senha_digitada = mascarar_senha("Insira sua Senha: ")
            if verificar_senha(senha_digitada, usuario["password"]):
                print("\n✅ Login bem-sucedido!")
                return Nome
            else:
                print("\n❌ Senha incorreta!")
                exit()

    print("\n🆕 Usuário não encontrado. Criando novo cadastro...")
    SenhaUser = mascarar_senha("Insira uma Senha para ciração (será utilizado o Nome e o Email fornecido acima): ")
    senha_hash = gerar_hash_bcrypt(SenhaUser)
    senha_hash_base64 = hash_para_base64(senha_hash)

    novo_usuario = {
        "name": Nome,
        "email": Email,
        "password": senha_hash_base64
    }

    data.append(novo_usuario)

    with open("./Data/data.json", "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, ensure_ascii=False, indent=4)

    print("\n✅ Cadastro realizado com sucesso!")
    return Nome
