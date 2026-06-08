# API P2

## Como executar 
Para facilitar a execução, a aplicação foi configurada com Docker.

### Pré-requisitos
Ter o Docker Desktop instalado na máquina.

### Passos para executar
1. Clone este repositório ou baixe o arquivo `docker-compose.yml`.
2. Abra um terminal na pasta do projeto.
3. Execute o comando abaixo:

```bash
docker compose up -d
```

4. Após a inicialização dos containers, acesse a API em:

```
http://localhost:8000/api/series/
```

## Imagem Docker

A imagem utilizada no projeto está disponível no Docker Hub:

https://hub.docker.com/r/nani77/api-series
