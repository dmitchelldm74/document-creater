from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main', methods = ['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    elif request.method == 'POST':
        filename = request.form['SaveAs']
        return render_template('New-Document.html', info={'dld': filename})     
           
@app.route('/new-document', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('New-Document.html', info={'download': 'Untitled'})
    elif request.method == 'POST':
        filename = request.form['SaveAs']
        content = request.form['blog']
        return render_template('New-Document.html', info={'download': 'Untitled'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000, debug=True)
