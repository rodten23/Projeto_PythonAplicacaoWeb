Para deploy no Heroku

curl https://cli-assets.heroku.com/install.sh | sh

pip install gunicorn psycopg2

heroku login -i

heroku create <nome-da-aplicação>

heroku addons:create heroku-postgresql:hobby-dev --app blog-python-rat

heroku config --app blog-python-rat

git add .

git commit -m "<sua mensagem de commit>"

git push

git push heroku main
