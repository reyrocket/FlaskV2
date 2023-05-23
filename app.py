from flask import Flask, render_template, jsonify, request
from database import load_data, ljfdb, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_jovian():
    jobs = load_data()
    return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    jobs = load_data()
    return jsonify(jobs)


@app.route("/jobs/<id>")
def display(id):
    job = ljfdb(id)
    if not job:
        return "Not Found", 404

    return render_template('jobpage.html', job=job, isinstance=isinstance)


@app.route("/job/<id>/apply", methods=['post'])
def apply(id):
    data = request.form
    job = ljfdb(id)
    add_application_to_db(id, data)
    return render_template('submit.html', application=data, job=job)


if __name__ == '__main__':
    # noinspection FlaskDebugMode
    app.run(host='0.0.0.0', debug=True)
