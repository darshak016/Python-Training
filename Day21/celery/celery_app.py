from celery import Celery
import sqlalchemy as db
import requests

app = Celery("celery_app",
            broker="amqp://localhost/",
            backend="db+sqlite:///celery_app_data.db")

engine = db.create_engine("sqlite:///celery_app_data.db", echo=True)
connection = engine.connect()
meta_data = db.MetaData()


gala_coin_data = db.Table(

    "GALA",
    meta_data,
    db.Column("id", db.Integer, primary_key=True),
    db.Column("rank", db.Integer),
    db.Column("marketCapUsd", db.Float),
    db.Column("usd_price", db.String),
    db.Column("price_change_24_hr", db.String),
)
meta_data.create_all(engine)

app.conf.beat_schedule = {
    "get_galacoin_price-at-5-seconds": {
        "task": "celery_app.get_gala_price",
        "schedule": 5,
        "args": (),
    },
}

@app.task
def get_gala_price():
    coincap_url = r"http://api.coincap.io/v2/assets/gala" # name of cryptocurrency is gala
    res = requests.get(coincap_url)
    
    if res.status_code == 200:
        coin_data = res.json()
        try:
            c = gala_coin_data.insert().values(
                rank=coin_data["data"]["rank"],
                marketCapUsd=coin_data["data"]["marketCapUsd"],
                usd_price=coin_data["data"]["priceUsd"],
                price_change_24_hr=coin_data["data"]["changePercent24Hr"]
            )
            connection = engine.connect()
            result = connection.execute(c)
        except Exception as e:
            print(e)
        else:
            return result     
