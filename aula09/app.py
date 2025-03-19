from flask import Flask

app = Flask(__name__)

@app.route('/devedora')
def pague():
  return "<h1>Quem não deve, não teme</h1>"

app.run()