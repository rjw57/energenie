from flask import Flask, render_template
from energenie import switch_on, switch_off

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on/')
def on():
    switch_on()
    return render_template('index.html')

@app.route('/off/')
def off():
    switch_off()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
