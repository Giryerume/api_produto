# API Flask para Gerenciamento de Produtos

Este é um projeto de exemplo que demonstra como criar uma API Flask simples para gerenciar produtos em um banco de dados MySQL. A API permite realizar operações CRUD (Create, Read, Update, Delete) em uma entidade de Produto.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Giryerume/api-produto.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd api-produto
   ```

3. Crie e inicie os contêineres Docker usando o Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Uso

A API estará disponível em `http://localhost:5000`.

## Rotas

- `GET /produtos`: Retorna todos os produtos.
- `GET /produtos/<id>`: Retorna um produto específico pelo ID.
- `POST /produtos`: Cria um novo produto.
- `PUT /produtos/<id>`: Atualiza um produto existente pelo ID.
- `DELETE /produtos/<id>`: Exclui um produto existente pelo ID.

## Autenticação

Para acessar as rotas protegidas da API, é necessário autenticar-se e obter um token JWT válido. Use a rota `POST /login` para obter um token de acesso e de atualização. Use a rota `POST /register` para registrar um novo usuário. Use a rota `POST /refresh` para obter um novo token de acesso válido.

## Exemplos

Aqui estão alguns exemplos de como usar a API:

- **Obter todos os produtos**:

  ```bash
  curl -H "Authorization: Bearer SEU_TOKEN_DE_ACESSO" http://localhost:5000/produtos
  ```

- **Criar um novo produto**:

  ```bash
  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer SEU_TOKEN_DE_ACESSO" -d '{"nome": "Produto 1", "descricao": "Descrição do produto 1", "preco": 19.99}' http://localhost:5000/produtos
  ```

- **Atualizar um produto existente**:

  ```bash
  curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer SEU_TOKEN_DE_ACESSO" -d '{"nome": "Produto Atualizado", "descricao": "Descrição atualizada", "preco": 29.99}' http://localhost:5000/produtos/<id>
  ```

- **Excluir um produto existente**:

  ```bash
  curl -X DELETE -H "Authorization: Bearer SEU_TOKEN_DE_ACESSO" http://localhost:5000/produtos/<id>
  ```

## Contribuição

Contribuições são bem-vindas! Se você encontrar um problema ou tiver uma sugestão, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
