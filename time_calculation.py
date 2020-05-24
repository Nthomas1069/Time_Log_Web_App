from flask import Flask, render_template, request # , redirect
import calculate_time

app = Flask(__name__)

# @app.route('/')
# def index() -> '302':
#   return redirect('/entry')

@app.route('/time_calc', methods=['POST'])
def calculate() -> 'html':
  in1 = request.form['in1']
  out1 = request.form['out1']
  in2 = request.form['in2']
  out2 = request.form['out2']
  in3 = request.form['in3']
  out3 = request.form['out3']
  title = 'Time Calculation Complete'
  results = str(calculate_time.calculate_times(in1, out1, in2, out2, in3, out3))
  return render_template('tlresult.html', the_title=title, results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
  return render_template('entry.html', the_title='Time Log Calculator')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)