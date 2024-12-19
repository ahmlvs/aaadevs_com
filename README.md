# aaadevs_com

1. how to create (env) and install requirements

```
python3 -m venv env
source env/bin/activate
```

install requirements

```
pip install -r requirements.txt
```

deactivate (env) if needed

```
deactivate
```

2. add .env variables

`PRODUCTION` -- "prod" or "dev"

`ALLOWED_ORIGINS` -- for dev for example "http://localhost,http://127.0.0.1"

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
