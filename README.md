# django-rest-api
Meu primeiro projeto Django utilizando rest-framework.

## Instalações
- Se você deseja executar o projeto, primeiro certifique-se de ter o python instalado globalmente em seu computador. Se não, você pode obter python [aqui](https://python.org.br/instalacao-windows/ "aqui").

- Depois de fazer isso, confirme se você também instalou o virtualenv globalmente. Caso contrário, execute este:

        $ pip install virtualenv
- Logo em seguida, Git clone este repositório para o seu PC

        $ git clone https://github.com/duduMonita/django-rest-api.git
## Depêndencias
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

## Executá-lo
1. Inicie o servidor usando este comando simples:

        $ python manage.py runserver
2. Agora você pode acessar o serviço API de arquivo em seu navegador usando:

        http://localhost:8000/

## Endpoints
Em um REST API, endpoints (URLs) definir a estrutura da API e como os usuários finais acessam os dados de nosso aplicativo usando os métodos HTTP - GET, POST, PUT, DELETE. 

Endpoint |HTTP | CRUD | Resultado
-- | -- |-- |--
`auth/login` | POST | CREATE | Cria um novo token para o usuário logado
`auth/user` | GET | READ | Seleciona o usuário logado
`auth/user` | PUT | UPDATE | Atualiza o usuário logado
`auth/logout` | POST | CREATE | Desabilita o token gerado para o usuário
`auth/auth/registration`| POST | CREATE | Cria um novo usuário(vendedor)
`lote/:pk` | PUT | UPDATE | Atualiza um nove lote
`lote/:pk` | DELETE | DELETE | Deleta um lote
`lote/?page=valor` | GET | READ | Seleciona todos os lotes
`lote/:pk` | GET | READ | Pega um único lote
`lote`| POST | CREATE | Cria um novo lote
`lote/:pk` | PUT | UPDATE | Atualiza um nove lote
`lote/:pk` | DELETE | DELETE | Deleta um lote
`item/?page=valor` | GET | READ | Seleciona todos os itens
`item-relat/?page=valor` | GET | READ | Seleciona todos os itens e suas respectivas relações detalhadas
`item/:pk` | GET | READ | Pega um único item
`item`| POST | CREATE | Cria um novo item
`item/:pk` | PUT | UPDATE | Atualiza um nove item
`item/:pk` | DELETE | DELETE | Deleta um item
`cliente/?page=valor` | GET | READ | Seleciona todos os clientes
`cliente/:pk` | GET | READ | Pega um único cliente
`cliente`| POST | CREATE | Cria um novo cliente
`cliente/:pk` | PUT | UPDATE | Atualiza um nove cliente
`cliente/:pk` | DELETE | DELETE | Deleta um cliente
`pedido/?page=valor` | GET | READ | Seleciona todos os pedidos
`pedido-relat/?page=valor` | GET | READ | Seleciona todos os pedidos e suas respectivas relações detalhadas
`pedido/:pk` | GET | READ | Pega um único pedido
`pedido`| POST | CREATE | Cria um novo pedido
`pedido/:pk` | PUT | UPDATE | Atualiza um nove pedido
`pedido/:pk` | DELETE | DELETE | Deleta um pedido
`relatorio/?page=valor` | GET | READ | Seleciona todos os pedidos e suas respectivas relações detalhadas
