from creds import USERNAME, PASSWORD
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
# from sqlalchemy import exc
# from sqlalchemy import event
# from sqlalchemy import select

conn = f'mysql+pymysql://{USERNAME}:{PASSWORD}@aws.connect.psdb.cloud/flaskv2'
some_engine = create_engine(conn, echo_pool=True, pool_size=7200, pool_recycle=3600, connect_args={
    'ssl': {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})


def configure():
    load_dotenv()


configure()


# @event.listens_for(some_engine, "engine_connect")
# def ping_connection(connection, branch):
#     if branch:
#         return
#     try:
#         connection.scalar(select(1))
#     except exc.DBAPIError as err:
#         if err.connection_invalidated:
#             connection.scalar(select(1))
#         else:
#             raise


def load_data():
    with some_engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))

        jobs = []
        for idd, title, location, salary, currency, responsibilities, requirements in result.all():
            jobs.append(dict(id=idd, title=title, location=location, salary=salary, currency=currency, responsibilities=responsibilities, requirements=requirements))

        return jobs


def ljfdb(id):
    with some_engine.connect() as connection:
        # noinspection PyArgumentList,SqlInjection
        result = connection.execute(
            text
            (f"select * from jobs where id = :val"),
            val=id)

    rows = result.all()
    if len(rows) == 0:
        return None
    else:
        return dict(rows[0])
