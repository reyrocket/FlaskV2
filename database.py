import os

from sqlalchemy import create_engine, text
from dotenv import load_dotenv


def configure():
    load_dotenv()


configure()
conn = f'mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@aws.connect.psdb.cloud/flaskv2'

engine = create_engine(conn, connect_args={
    'ssl': {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})


def load_data():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))

        jobs = []
        for idd, title, location, salary, currency, responsibilities, requirements in result.all():
            jobs.append(dict(id=idd, title=title, location=location, salary=salary, currency=currency, responsibilities=responsibilities, requirements=requirements))

        return jobs
