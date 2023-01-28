# CNAB_Parser

- API de interpretação de arquivos CNAB.

## Instruções

- Com Docker: <br>

  1. faça o clone do repositório;
  2. configure o arquivo .env com a variáveis corretamente;
  3. com o docker instalado basta usar o seguinte comando, dentro da pasta do repositório:<br>
     `docker-compose up --build`

- Sem Docker: <br>

  1. faça o clone do repositório;
  2. com o python instalado, dentro da pasta do repositório, use os seguintes comandos para criar e entrar no ambiente virtual:<br>

  - Linux/MacOs

  `python -m venv venv`<br>
  `source venv/bin/activate`

  - Windows

  `python -m venv venv`<br>
  `.\venv\Scripts\activate`

  3. depois é só instalar as dependências e rodar a api:

  `pip install -r requirements.txt`
  `TEST=TEST ./manage.py migrate`<br>
  `TEST=TEST .manage.py runserver`

- Com a API rodando basta acessar a rota api/docs/ no navegador para ver a documentação.

## Rotas

| Rotas                    | Descrição                                |
| ------------------------ | ---------------------------------------- |
| api/users/               | criação e listagem de usuário            |
| api/users/usuário_id/    | atualização e deleção de usuário         |
| api/parser/              | upload de arquivo cnab                   |
| api/transactions/        | listagem das transações do usuário       |
| api/stores/transactions/ | listagem dos saldos das lojas do usuário |
| api/transaction/types/   | listagem dos tipos de transação          |
| api/docs/                | documentação da api                      |
