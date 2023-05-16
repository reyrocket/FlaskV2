from sqlalchemy import create_engine, text

conn = 'mysql+pymysql://42t1ov2hnzvlxk4bs2po:pscale_pw_GO2CGKkxeqZXBMnUsqMuKk09nIcLgVXwP8TLLgj2PrE@aws.connect.psdb.cloud/flaskv2'

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

