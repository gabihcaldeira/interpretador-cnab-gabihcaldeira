# CNAB_Parser

- API de interpretação de arquivos CNAB.

## Instruções

1. faça o clone do repositório;
2. crie o arquivo .env e configure com as variáveis de acordo com o .env.example;
3. entre na pasta do projeto;<br>
   `cd interpretador-cnab-gabihcaldeira`<br>

- Com Docker: <br>

  3. com o docker instalado basta usar o seguinte comando: <br>
     `docker-compose up --build`

- Sem Docker: <br>

  3. com o python instalado, use os seguintes comandos para criar e entrar no ambiente virtual:<br>

     - Linux/MacOs

       `python -m venv venv`<br>
       `source venv/bin/activate`

     - Windows

       `python -m venv venv`<br>
       `.\venv\Scripts\activate`

  4. depois é só instalar as dependências e rodar a api:<br>
     `pip install -r requirements.txt`<br>
     `TEST=TEST ./manage.py migrate`<br>
     `TEST=TEST ./manage.py runserver`

- Com a API rodando basta acessar a rota api/docs/ no navegador para ver a documentação.
  > para fazer o upload do arquivo cnab pelo docs, na rota api/parser/, é necessário escolher o tipo de 'request body' como 'multipart/form-data'.
- Se preferir, no repositório também hà o arquivo do insomnia em formato json, com as rotas configuradas. Note que hà ambiente de docker e para sqlite3.

## Rotas

| Rotas                    | Descrição                                | Autenticação       |
| ------------------------ | ---------------------------------------- | ------------------ |
| api/users/               | criação de usuário                       | :x:                |
| api/users/               | listagem de usuário                      | :white_check_mark: |
| api/users/usuário_id/    | atualização e deleção de usuário         | :white_check_mark: |
| api/parser/              | upload de arquivo cnab                   | :white_check_mark: |
| api/transactions/        | listagem das transações do usuário       | :white_check_mark: |
| api/stores/transactions/ | listagem dos saldos das lojas do usuário | :white_check_mark: |
| api/transaction/types/   | listagem dos tipos de transação          | :white_check_mark: |
| api/docs/                | documentação da api                      | :x:                |
