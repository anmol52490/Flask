from flask import Flask

app= Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to the Home Page! </h1>"


@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hi {name.title()}, Welcome to the Page!</h1>"

@app.route('/addition_two/<int:num1>/<int:num2>')
def addition_two(num1,num2):
    return f"<h1>The number {num1} is added to {num2} and the answer is {num1+num2}</h1>"

@app.route('/addition/<int:num>')
def addition(num):
    return f"<h1>The number {num} is added to 10 and the answer is {num+10}</h1>"

@app.route("/about")

def about():
    return "<h1>Welcome to the About Page! </h1>"

if __name__ == "main":
    app.run(debug=True)