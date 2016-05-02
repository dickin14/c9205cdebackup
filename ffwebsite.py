from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')
    
@app.route('/classes')
def classes():
    return render_template('classes.html')
    
@app.route('/uldah')
def uldah():
    return render_template('uldah.html')
    
@app.route('/gridania')
def gridania():
    return render_template('gridania.html')
    
@app.route('/limsa')
def limds():
    return render_template('limsa.html')
    
    
if __name__ == '__main__':
    Bootstrap(app)
    app.run(port=8080, host='0.0.0.0', debug=True)