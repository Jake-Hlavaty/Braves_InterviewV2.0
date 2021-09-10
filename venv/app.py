from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dash():
    return render_template('dashboard.html', title = 'Dashboard')

@app.route('/charts', methods=['GET'])
def charting():
    return render_template('charting.html', title = 'Charting')

@app.route('/tendencies', methods=['GET'])
def tendencies():
    return render_template('tendencies.html', title = 'Tendencies')

@app.route('/match-ups', methods=['GET'])
def summary():
    return render_template('match_ups.html', title = 'Summary')
@app.route('/test', methods=['GET'])
def Height_v_Side():
    return render_template('test.html', title = 'Height v Side')
if __name__ == '__main__':
    app.run(debug=True)
