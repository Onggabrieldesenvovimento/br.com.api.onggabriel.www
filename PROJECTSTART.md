<h1 align="center">💻 BACKEND ONG GABRIEL:</h1>
<p align="center">
  Esta API foi desenvolvida para gerenciar os dados relacionados aos posts, comentários, avaliações de voluntários e participantes do projeto, promovendo o bem-estar mental e prevenção ao suicídio. O framework Django foi utilizado para controlar o fluxo de dados e garantir que a plataforma tenha uma estrutura robusta e escalável. Com essa integração, a ONG Gabriel pode manter um canal eficiente de comunicação, além de fornecer um espaço seguro de interação e apoio para jovens em situação de vulnerabilidade social.
</p>
<br/>
<h2 align="center">TECNÓLOGIAS UTILIZADAS</h2>
<div align="center">

 ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
</div>
<br/>   
<br/>
<h2 align="center">COMO UTILIZAR O PROJETO</h2>

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em seu sistema:

1. [Python](https://www.python.org/downloads/) (Python3++).
2. [Git](https://git-scm.com/downloads) (Controle de versão)
3. Instale o **VirtualEnv** para criar ambientes virtuais no seu projeto:
   ```bash
   # Em seu PowerShell digite o seguinte comando para baixar o virtualenv:
    pip install virtualenv
   
  4. Após instalar o (virtualenv) é importante configurar o powershell para poder ativar o ambiente virtual
 ```bash
   # No seu powershell digite o seguinte comando
     Set-ExecutionPolicy Unrestricted -Scope Process -Force
   ```
### ⚙️🖥️ Configurando o Projeto em sua máquina

1. Clone este repositório em uma pasta na sua máquina localmente:
   ```bash
   # Crie uma pasta em seu computador, você pode chama-la de (ProjetoOngGabriel),
   com o click direito do mouse abra essa pasta utilizando o git bash, ao abrir o git bash cole este código!
   
     https://github.com/Onggabrieldesenvovimento/br.com.api.onggabriel.www.git
   
   ```
2. Certifique-se que o processo de clonagem do reporitório deu certo e entre na pasta do projeto:
    ```bash
    # 1- Verifique se o projeto foi clonado corretamente:
    # Resultado esperado ( br.com.api.onggabriel.www.git/ )
    
      ls

    # 2- Entre na pasta do projeto
    
      cd br.com.api.onggabriel.www.git/

    # 3- Se preferir você pode optar por abrir o vscode direto no projeto

      code .
    
   ```
3. Com o projeto aberto no VSCODE, você pode ativar/criar o ambiente virtual:
   - Para Windons:
No seu terminal do vscode, rode os seguintes códigos no terminal:
    ```bash
    #Utilizando Prompt de comando (CMD)
    
    #1- Criar a VENV
    python -m venv venv
    
    #2- Ativar a VENV
    .\venv\Scripts\activate.bat
    
    #3- Atualizar o pip
    python -m pip install --upgrade pip


    #Utilizando o PowerShell

    #1- Criar a VENV
    python -m venv venv

    #2- Ativar a VENV
    .\venv\Scripts\activate ou .\venv\Scripts\activate.ps1

    #3- Atualizar o pip
    python -m pip install --upgrade pip
    
   ```
   - Para linux:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash
    #1- Criar a VENV 
    python3 -m venv venv

    #2- Ativar a VENV
    ./venv/bin/activate

    #3- Atualizar o pip
    python -m pip install --upgrade pip
    
   ```
   - Para Mac:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash

    #1- Criar a VENV
    python -m venv venv

    #2- Ativar a VENV
    ./venv/bin/activate

    #3- Atualizar o pip
    python -m pip install --upgrade pip
        
   ```
    
### 🚩 Iniciando o Servidor local
1. Após fazer os passos anteriores e ativar a (virtualenv). No terminal do projeto execute o comando para baixar todas as dependências do projeto:
   ```text
   
   pip install -r requirements.txt
   
   ```
2. Baixe as migrações do banco de dados:
   ```bash
   # Certificar-se de que está no diretório do projeto Django onde o arquivo manage.py está localizado
   
   python manage.py migrate
   
   ```
3. Você poderá criar um Super Usuário:
   ```bash
      # Essa é uma parte opcional mas é importante criar para ter acesso a parte de admin do django
     
      python manage.py createsuperuser
  
      # logo após esse comando vai ser preciso colocar um nome de usuario, email, cpf e senha.
  
   ```
3. Você poderá iniciar o servidor:
   ```bash
     
      python manage.py runserver 8000
  
   ```
  O servidor estará acessível em: [http://localhost:8000/](http://localhost:8000/ap1/v1/user) 
  
  
 ### 🚩💻 Endpoints
 *Atenção*: O Framework Django disponibiliza uma interface que facilita os testes de api
  - Criar ou listar usuários: http://localhost:8000/api/v1/user/
  - Utilizando Swagger: http://localhost:8000/swagger/
  - Utilizando Redoc: http://localhost:8000/redoc/

<br/>

#### Exemplos de requisições:

  ```bash
      # METODO POST para cadastrar um usuário (http://localhost:8000/api/v1/user/)
      {
          "name": string,
          "email": string,
          "cpf": string,
          "password": string
      }
```

<h1 align="center">MUITO OBRIGADO PELA VISITA!</h1>

