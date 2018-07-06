from flask import Flask, request, render_template, redirect, url_for

test = []
app = Flask(__name__)
number = 12

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    test.append(request.form['Player1'])
    test.append(request.form['Player2'])
    test.append(request.form['Player3'])
    test.append(request.form['Player4'])
    test.append(request.form['Player5'])
    test.append(request.form['Player6'])
    test.append(request.form['Player7'])
    test.append(request.form['Player8'])
    test.append(request.form['Player9'])
    test.append(request.form['Player10'])
    #processed_text = text
    #text = 'dog'
    return redirect(url_for("hello"));

@app.route('/Result', methods=['GET'])
def hello():
    print(test);
    return render_template('result.html',number = number)

@app.route('/Result')
def back():
    return redirect(url_for("my_form"));




app.run(debug = True)
#print (my_form_post())