from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'titulo': 'Analista Dados',
    'salario': 'R$ 5.000',
    'localidade': 'SC, Brasil'
  },
  {
    'id': 2,
    'titulo': 'Dev Web com Flask',
    'salario': 'R$ 3.000',
    'localidade': 'PR, Brasil'
  },
  {
    'id': 3,
    'titulo': 'Cientista de Dados',
    'salario': 'R$ 3.500',
    'localidade': 'SP, Brasil'
  },
  {
    'id': 4,
    'titulo': 'Engenheiro Backend',
    'salario': 'R$ 5.500',
    'localidade': 'SP, Brasil'
  },
  {
    'id': 5,
    'titulo': 'Estatístico',
    'salario': 'R$ 2.500',
    'localidade': 'RJ, Brasil'
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def lista_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
