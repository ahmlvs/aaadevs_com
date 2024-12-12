# aaadevs_com

1. install req

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. add .env variables

`PRODUCTION` -- "prod" or "dev"

`PRODUCTION_DB_URL` -- Production Database URL string

3. run the app

locally

```
python3 main.py
```

in production

```
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```
