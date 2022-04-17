# orm-talk-intmed
This repo contains the code base used in a talk about Django ORM at Intmed Software.

## Como rodar o projeto

Execute: os seguintes comandos


```
$ pip install -r requirements.txt
$ python manage.py migrate
```

Para popular o banco com N registros em cada tabela utilize o comando


```
$ python manage.py populatedb N
```

Para rodar os testes:

```
$ python manage.py test
```

e para rodar o servidor:

```
$ python manage.py runserver
```

# Desafio:

Você deve ajustar as duas rotas (/medicos e /clinicas) para passar nos testes de regressão. 

Os requisitos funcionais das rotas já estão sendo cumpridos, então basta você popular o banco para visualizar
o retorno de cada um dos endpoints.

Na rota de médicos você deve retornar os médicos e as clinicas nas quais ele atende.

Na rota de clínicas, você deve retornar a clínica, as informações juridicas da clinica, o número de medicos ativos na clinica e 
o número total de médicos
