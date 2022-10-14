import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
  return render_template('index.html')


@app.route('/r', methods = ["GET", "POST"])
def r():
  if request.method == 'POST':
    name = request.form
    return render_template("result.html", name)



if __name__ == '__main__':
  app.run(debug=True)
