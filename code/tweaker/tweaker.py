from collections import OrderedDict
from flask import Flask, render_template, jsonify, request, abort


test_data = OrderedDict([
  (u'dodgeChanceSlope', 0.01),
  (u'dodgeChanceOffset', 0),
  (u'hitChanceSlope', 0.02),
  (u'hitChanceOffset', 0.4),
  (u'critChanceSlope', 5.0000000000000001E-3),
  (u'critChanceOffset', 0),
  (u'antiCritChanceSlope', 0.01),
  (u'antiCritChanceOffset', 0),
  (u'damageReductionSlope', 0.01),
  (u'damageReductionOffset', 0),
  (u'maximumHealthSlope', 2),
  (u'maximumHealthOffset', 10),
])

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/get')
def get_data():
    return jsonify(test_data)

@app.route('/api/set', methods=['POST'])
def set_data():
    propertyName = request.form['propertyName']
    if propertyName in test_data:
        test_data[propertyName] = float(request.form['newValue'])
        return ""
    else:
        abort(401)


app.debug = True
app.run()
