from flask import Flask, render_template, jsonify
from database import load_data

app = Flask(__name__)





@app.route("/")
def hello_jovian():
    jobs = load_data()
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_data())


if __name__ == '__main__':
    # noinspection FlaskDebugMode
    app.run(host='0.0.0.0', debug=True)
