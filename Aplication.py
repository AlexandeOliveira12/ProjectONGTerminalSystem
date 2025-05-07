import json
import os
import webbrowser
from Components.Register import *

# ------------------------------ INSERIR DADOS JSON ------------------------------

dados = {
    "name": Nome,
    "email": Email,
    "password": senha_hash_base64
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

# LIMPAR TERMINAL
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# SISTEMA DE ESCOLHAS DE CURSOS
def menu_escolha():
        print(f"\n 🧠olá {Nome} Seja Bem vindo ao Menu do Estudante\n")
        print("1️⃣  - Cursos Python")
        print("2️⃣  - Logica Programção")
        print("3️⃣  - Infraestrutura Computacional - Hardware")
        print("4️⃣  - Sair")
        escolha = int(input("Escolha alguma das opções acima (somente numeros): "))

        # SISTEMA DE CURSOS PYTHON
        if escolha == 1:
            clear_screen()
            print("\n📚 Qual curso quer assistir?\n")
            print("1️⃣  - Curso em Video - Python")
            print("2️⃣  - Curso Gratuito de Python - Pietro Martins")
            print("3️⃣  - Python for Beginners - (Curso em Inglês)")
            print("4️⃣  - Voltar para o Menu")
            print("5️⃣  - Sair")
            EscCurso = int(input("Escolha um curso (somente numeros): "))
            if  EscCurso == 1:
                CursoEmVideo = "https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0"
                webbrowser.open(CursoEmVideo)
            elif EscCurso == 2:
                CursoPietroMartins = "https://www.youtube.com/watch?v=wC_mwNUT48s&list=PLpaKFn4Q4GMN1A4J1FnhW_anOGt8ug8ip"
                webbrowser.open(CursoPietroMartins)
            elif EscCurso == 3:
                CursoForBeginners = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
                webbrowser.open(CursoForBeginners)
            elif EscCurso == 4:
                clear_screen()
                menu_escolha()
            elif EscCurso == 5:
                clear_screen()
                return
            else:
                print("")
        
        # SISTEMA DE LOGICA DE PROGRAMAÇÃO
        if escolha == 2:
            clear_screen()
            print("\n📚 Qual curso quer assistir? ")
            print("1️⃣  - Curso em Video - Logica Programação")
            print("2️⃣  - Curso Logica Prog. Jhonatan Souza")
            print("3️⃣  - Curso Logica Prog. Victor Lima")
            print("4️⃣  - Voltar para o Menu")
            print("5️⃣  - Sair")
            EscCursoLogicProg = int(input("Escolha um curso (somente numeros): "))
            if EscCursoLogicProg == 1:
                CursoEmVideoLogicProg = "https://www.youtube.com/watch?v=8mei6uVttho&list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV"
                webbrowser.open(CursoEmVideoLogicProg)
            elif EscCursoLogicProg == 2:
                CursoLogicJhonatanSouza = "https://www.youtube.com/watch?v=iF2MdbrTiBM"
                webbrowser.open(CursoLogicJhonatanSouza)
            elif EscCursoLogicProg == 3:
                CursoLogicaAlgoritimos = "https://www.youtube.com/watch?v=6OxA9er9VFo"
                webbrowser.open(CursoLogicaAlgoritimos)     
            elif EscCursoLogicProg == 4:
                clear_screen()
                menu_escolha()
            elif EscCursoLogicProg == 5:
                clear_screen()
                return
        
        # SISTEMA DE INFRAESTRUTURA COMPUTACIONAL
        if escolha == 3:
            clear_screen()
            print("\n📚 Qual curso quer assistir? ")
            print("1️⃣  - Curso em Video - Hardware")
            print("2️⃣  - Curso de Hardware - Welington Tutoriais")
            print("3️⃣  - Curso de Hardware - MW Informatica")
            print("4️⃣  - Voltar para o Menu")
            print("5️⃣  - Sair")
            EscCursoInfraComp = int(input("Escolha um curso (somente numeros): "))
            if EscCursoInfraComp == 1:
                CursoEmInfraComp = "https://www.youtube.com/watch?v=iT6E92Kt38o&list=PLHz_AreHm4dn1JHgN9wpbIUhzZmycYQXW"
                webbrowser.open(CursoEmInfraComp)
            elif EscCursoInfraComp == 2:
                CursoWelingtonTutoriais = "https://www.youtube.com/watch?v=vlcIldrz7Yg&list=PLSXPpZCNu-ejEcox8r9MtLmcn_PHAVsIw"
                webbrowser.open(CursoWelingtonTutoriais)
            elif EscCursoInfraComp == 3:
                CursoMwInforamtica = "https://www.youtube.com/watch?v=YLBSMJ13ZqI&list=PL968TMGoACSuEiD44jNGIbvQfJo4Lwf3-"
                webbrowser.open(CursoMwInforamtica)     
            elif EscCursoInfraComp == 4:
                clear_screen()
                menu_escolha()
            elif EscCursoInfraComp == 5:
                clear_screen()
                return
        elif escolha == 4:
            return
        else:
            print("")
        
        return 
    
menu_escolha()

        

