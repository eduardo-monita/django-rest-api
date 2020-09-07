# django-rest-api
Meu primeiro projeto Django utilizando rest-framework.

# Instalações
- Se você deseja executar o projeto, primeiro certifique-se de ter o python instalado globalmente em seu computador. Se não, você pode obter python [aqui](https://python.org.br/instalacao-windows/ "aqui").

- Depois de fazer isso, confirme se você também instalou o virtualenv globalmente. Caso contrário, execute este:

        $ pip install virtualenv
- Logo em seguida, Git clone este repositório para o seu PC

        $ git clone https://github.com/duduMonita/django-rest-api.git
- # Depêndencias
1.  Cd em seu repositório clonado como tal:

        $ cd django-rest-api
2. Crie e ative seu ambiente virtual:

        $ virtualenv env -p python3
    
        $ source env/Scripts/Activate
3. Instale as dependências necessárias para executar o aplicativo:

        $ pip install -r requirements.txt
4.  Cd no projeto Dajngo como tal:

        $ cd huai       
5. Faça essas migrações funcionarem:

        $ python manage.py migrate

- # Executá-lo
1. Inicie o servidor usando este comando simples:

        $ python manage.py runserver
2. Agora você pode acessar o serviço API de arquivo em seu navegador usando:

        http://localhost:8000/
