# Projeto Final - Inova.Ação Afro (C.E.S.A.R / Share RH)

### Sobre o Inova.Ação Afro
É um programa de formação e capacitação desenvolvido entre a Share RH e o CESAR A iniciativa oferecerá 84h de imersão na linguagem de programação Python e, ao final das aulas, será realizado um processo seletivo para vagas no CESAR.

[Leia mais](https://conteudo.sharerh.com/inova-acao-afro-cesar)

### Setup com docker
1. [Garanta que o Docker e o Docker Compose estão instalados em seu ambiente](https://stack.desenvolvedor.expert/appendix/docker/instalacao.html)
2. Na raiz do projeto, execute os seguintes comandos
```shell
docker-compose run --rm app python manage.py createsuperuser # Para criar um superusuário
docker-compose run --rm app python manage.py populate_db # Para pré-popular o banco de dados com dados iniciais de cartórios Brasileiros
```

### Setup sem docker
1. [Você deve ter o Python 3.8 instalado configurado em seu ambiente](https://www.w3computing.com/python/installing-python-windows-macos-linux/)
2. Instale e configure o PostgreSQL 13: [Linux](https://www.devmedia.com.br/instalacao-e-configuracao-do-servidor-postgresql-no-linux/26184) | [Windows](https://fabridata.com/como-instalar-postgresql-13-no-windows/) | [MacOS](https://www.robinwieruch.de/postgres-sql-macos-setup)
3. Edite o arquivo config/settings.py e re-escreva a config DATABASES de acordo com as configurações do seu banco de dados
4. Na raiz do projeto, execute os segintes comandos:
```shell
python manage.py createsuperuser # Para criar um superusuário
```

### Desafio

1. Registre os modelos **cartorios**, **adressess** e **contact_information** no Django Admin
2. Implemente o comando `populate_db`, lembre-se. Este comando tem a finalidade de carregar os dados do arquivo .csv e popular as tabelas no banco de dados. Caso tenham dúvidas, implementamos algo muito semelhante em uma das aulas de sábado, dia 09/10/21.
3. Implemente os seguintes endpoints:

| Endpoint  |  Método  |  Ação  |
| ------------------- | ------------------- | ------------------- |
|  /cartorios |  GET |  Retorna lista de cartórios paginadas de 50 em 50 |
|  /cartorios/{uf} |  GET |  Retorna a lista de cartórios da UF paginadas de 50 em 50 |
|  /cartorios/{id} |  GET |  Retorna os detalhes de um cartório |
|  /cartorios |  POST |  Adiciona um novo cartório à base de dados |
|  /cartorios/{id} |  PUT |  Atualização completa de um cartório |
|  /cartorios/{id} |  PATCH |  Atualização Parcial de um cartório |
|  /cartorios/{id} |  DELETE |  Remove um cartório da base de dados |
