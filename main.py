from flask import Flask, render_template, redirect, request, json, jsonify, url_for

app = Flask(__name__)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if (request.method == 'POST'):
        name = request.form.get('name')
        address = request.form.get('address')
        number = request.form.get('number')
        dateandtime = request.form.get('datetime')
        lead = (name, number, address, dateandtime)
    return ''

if __name__=='__main__':
    app.run(debug=True)
