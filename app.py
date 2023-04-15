from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def process_form():
    link = request.form['link']
    email = request.form['email']
    if link.find('amazon') > -1:
        app='amazon'
        subprocess.run(['python3', 'amazon.py', link, email,app])
    else:
        app='flipkart'
        subprocess.run(['python3', 'flipkart.py', link, email,app])
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)