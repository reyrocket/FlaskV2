from creds import USERNAME, PASSWORD
from sqlalchemy import create_engine, text

conn = f'mysql+pymysql://{USERNAME}:{PASSWORD}@aws.connect.psdb.cloud/flaskv2'
some_engine = create_engine(conn, echo_pool=True, pool_size=7200, pool_recycle=3600, connect_args={
    'ssl': {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})


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
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}
        )
        rows = result.all()
        for idd, title, location, salary, currency, responsibilities, requirements in rows:
            if len(rows) == 0:
                return None
            else:
                return dict(id=idd, title=title, location=location, salary=salary, currency=currency, responsibilities=responsibilities, requirements=requirements)


def add_application_to_db(job_id, data):
    with some_engine.connect() as connection:
        query = text("insert into applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        connection.execute(query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin_url": data['linkedin_url'],
            "education": data['education'],
            "work_experience": data['work_experience'],
            "resume_url": data['resume_url']
        })


