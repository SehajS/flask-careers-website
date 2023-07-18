from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Vancouver, BC',
    'salary': '90,000 CAD'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Vancouver, BC',
    # 'salary': '110,000 CAD'
  },
  {
    'id': 3,
    'title': 'Frontend Developer',
    'location': 'Winnipeg, MB',
    'salary': '75,000 CAD'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)