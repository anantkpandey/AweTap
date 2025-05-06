from flask import Flask, render_template, request
from database import init_db, search_definitions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form.get('query')
        results = search_definitions(query)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)