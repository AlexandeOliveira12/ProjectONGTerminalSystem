import os
import webbrowser
from Components.Register import login_ou_cadastro

# LIMPAR TERMINAL
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# SISTEMA DE ESCOLHAS DE CURSOS
def menu_escolha(nome):
    while True:
        print(f"\n🧠 Olá {nome}, seja bem-vindo ao Menu do Estudante\n")
        print("1️⃣  - Cursos Python")
        print("2️⃣  - Lógica de Programação")
        print("3️⃣  - Infraestrutura Computacional - Hardware")
        print("4️⃣  - Sair")
        escolha = int(input("Escolha uma das opções acima: "))

        if escolha == 1:
            clear_screen()
            print("\n📚 Qual curso quer assistir?\n")
            print("1️⃣  - Curso em Vídeo - Python")
            print("2️⃣  - Curso Gratuito - Pietro Martins")
            print("3️⃣  - Python for Beginners (Inglês)")
            print("4️⃣  - Voltar ao Menu")
            print("5️⃣  - Sair")
            curso = int(input("Escolha um curso: "))
            links = [
                "https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0",
                "https://www.youtube.com/watch?v=wC_mwNUT48s&list=PLpaKFn4Q4GMN1A4J1FnhW_anOGt8ug8ip",
                "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
            ]
            if 1 <= curso <= 3:
                webbrowser.open(links[curso - 1])
            elif curso == 4:
                clear_screen()
                continue
            else:
                break

        elif escolha == 2:
            clear_screen()
            print("\n📚 Cursos de Lógica de Programação:")
            print("1️⃣  - Curso em Vídeo")
            print("2️⃣  - Jhonatan Souza")
            print("3️⃣  - Victor Lima")
            print("4️⃣  - Voltar")
            print("5️⃣  - Sair")
            curso = int(input("Escolha um curso: "))
            links = [
                "https://www.youtube.com/watch?v=8mei6uVttho&list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV",
                "https://www.youtube.com/watch?v=iF2MdbrTiBM",
                "https://www.youtube.com/watch?v=6OxA9er9VFo"
            ]
            if 1 <= curso <= 3:
                webbrowser.open(links[curso - 1])
            elif curso == 4:
                clear_screen()
                continue
            else:
                break

        elif escolha == 3:
            clear_screen()
            print("\n📚 Cursos de Infraestrutura:")
            print("1️⃣  - Curso em Vídeo - Hardware")
            print("2️⃣  - Welington Tutoriais")
            print("3️⃣  - MW Informática")
            print("4️⃣  - Voltar")
            print("5️⃣  - Sair")
            curso = int(input("Escolha um curso: "))
            links = [
                "https://www.youtube.com/watch?v=iT6E92Kt38o&list=PLHz_AreHm4dn1JHgN9wpbIUhzZmycYQXW",
                "https://www.youtube.com/watch?v=vlcIldrz7Yg&list=PLSXPpZCNu-ejEcox8r9MtLmcn_PHAVsIw",
                "https://www.youtube.com/watch?v=YLBSMJ13ZqI&list=PL968TMGoACSuEiD44jNGIbvQfJo4Lwf3-"
            ]
            if 1 <= curso <= 3:
                webbrowser.open(links[curso - 1])
            elif curso == 4:
                clear_screen()
                continue
            else:
                break

        elif escolha == 4:
            print("\n👋 Saindo...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# INICIAR PROGRAMA
usuario_nome = login_ou_cadastro()
menu_escolha(usuario_nome)
