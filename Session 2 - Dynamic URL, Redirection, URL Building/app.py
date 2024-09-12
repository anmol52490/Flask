from flask import Flask, redirect, url_for, request


app =  Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the HomePage!</h1>"



#DYNAMIC URLS
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hi {name.title()}, Welcome to the Page!</h1>"



#REDIRECTING URLS
@app.route("/score/<name>/<int:marks>")
def score(name,marks):
    if marks > 40:
        #redirect user to page 'pass'
        return redirect(url_for("passed",name=name))
    else:
        #redirect user to page 'fail'
        return redirect(url_for("failed",name=name))
    

@app.route('/pass')
def passed():
    name = request.args.get('name', 'Student')
    return f"<h1>Congratulations, {name.title()}! You have passed the test!</h1>"


@app.route('/fail')
def failed():
    name = request.args.get('name', 'Student')
    return f"<h1>Sorry, {name.title()}! You have failed!</h1>"



#URL BUILDING

@app.route("/Uscore/<name>/<int:marks>")
def Uscore(name,marks):
    if marks > 40:
        #redirect user to page 'pass'
        return redirect(url_for("Upassed",sname=name, smarks=marks))
    else:
        #redirect user to page 'fail'
        return redirect(url_for("Ufailed",sname=name, smarks=marks))
    

@app.route('/Upass/<sname>/<int:smarks>')
def Upassed(sname, smarks):
    return f"<h1>Congratulations, {sname.title()}! You have passed the test {smarks} marks!</h1>"


@app.route('/Ufail/<sname>/<int:smarks>')
def Ufailed(sname, smarks):
    return f"<h1>Sorry, {sname.title()}! You have failed with {smarks} marks!</h1>"