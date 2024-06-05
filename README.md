# rasa

>dentro do venv

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download pt_core_news_sm
python -m rasa run --enable-api

##requisitos pip install
>python3 -m venv ./venv

>source ./venv/bin/activate

>pip install -r requirements.txt

>rasa train

>python -m rasa run --enable-api

acesse :http://localhost:5005/webhooks/rest/webhook utilizando :https://insomnia.rest/download

utilize:

{
    "sender": "Alysson",
    "message": "sad"
}

## comandos Alysson

docker compose build

docker compose up rasa