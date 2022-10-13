import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/no')
def no():
  return render_template('no.html')


@app.route('/result', methods = ["POST", "GET"])
def result():
  output = request.form.to_dict()
  name = output["name"]
  msg = gay_calculator(name)
  return render_template("result.html", msg)



if __name__ == '__main__':
  app.run(debug=True)

def gay_calculator(name):
  i = random.randint(0, 100)
  if i > 50: return name + " you are " + str(i) +"%" + " gay, stop lying"
  else: return name + " you are " + str(i) +"%" + " gay, amen"