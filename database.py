from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, 
                      connect_args={
                        'ssl':{
                          'ssl_ca': "/etc/ssl/cert.pem"
                        }
                      })



def load_jobs_from_db():
  with engine.connect() as con:
    result = con.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as con:
    result = con.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    return rows[0]._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(f"""INSERT INTO applications (job_id, full_name, email, linkedin, education, resume_url, experience)
    VALUES ({job_id}, "{data['full_name']}", "{data['email']}", "{data['linkedin']}", "{data['education']}", "{data['resume_url']}", "{data['experience']}")""")
    conn.execute(query)