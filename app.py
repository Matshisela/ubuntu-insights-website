from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/careers')
def careers():
    return render_template('careers.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Remote',
    'deadline': '31 January, 2024'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'deadline': '31 January, 2024'
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Remote',
    'deadline': '31 January, 2024'
}]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
