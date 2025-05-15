# Projeto PIM 1° Semestre A.D.S UNIP

# Plataforma de Ensino - Terminal
Este projeto é um sistema baseado em Python executado no terminal, que oferece cursos sobre Programação em Python, Lógica de Programação e Infraestrutura Computacional.

# 📌 Funcionalidades

**Cadastro de Usuário:**

* Captura Nome, E-mail e Senha.

* Armazena a senha com hash seguro (bcrypt) e a converte para base64.

**Armazenamento de Dados:**

* Salva os usuários cadastrados em um arquivo JSON.

**Menu Interativo:**

* Permite escolher cursos em diversas áreas.

* Abre automaticamente os cursos no navegador.

* Limpeza do Terminal:

* Mantém a interface organizada ao longo da navegação.

# 🚀 Como Executar

**Clone o repositório**

```
git clone https://github.com/AlexandeOliveira12/ProjectONGTerminalSystem.git
cd ProjectONGTerminalSystem
```

**Instale as dependências**

```
pip install -r requirements.txt
```

**Execute o programa**

```
python Aplication.py
```

# 🔒 Segurança e LGPD

**Este sistema segue boas práticas de segurança:**

* ✅ Senhas criptografadas com bcrypt
* ✅ Armazenamento seguro em JSON
* ✅ Captura mínima de dados do usuário

# 🛠 Tecnologias Utilizadas

* Python 3.13.2

* bcrypt (criptografia)

* pwinput (entrada de senha segura)

* JSON (armazenamento de dados)