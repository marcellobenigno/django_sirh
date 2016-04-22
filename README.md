# SIRH

Exemplo de CRUD com o Django e Bootstrap

link da aplicação: https://sirh-marcellobenigno.herokuapp.com

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.0
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:marcellobenigno/django_sirh.git sirh_src
cd sirh_src
python -m venv .sirh
source .sirh/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Define DEBUG=False
5. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroky config:set DEBUG=False
git push heroku master --force
```