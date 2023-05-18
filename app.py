from flask import Flask, render_template, jsonify
from database import load_data, ljfdb

app = Flask(__name__)


@app.route("/")
def hello_jovian():
    jobs = load_data()
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    jobs = load_data()
    return jsonify(jobs)


@app.route("/jobs/<id>")
def display(id):
    job = ljfdb(id)
    return (job)


if __name__ == '__main__':
    # noinspection FlaskDebugMode
    app.run(host='0.0.0.0', debug=True)
