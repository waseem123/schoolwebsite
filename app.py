# We have to import Flask class from flask module. Following line adds the flask module.
from flask import Flask
from flask import render_template
from flask import url_for,redirect
from flask import request

# Initilaise the Flask Constructor
app = Flask(__name__)

# Create first URL. This first url is a root URL. And it will open the main page of your project.
# @app.route("/") - This line tells the homepage() function to open the ROOT URL. And homepage() function will return
# the string to be printed on the webpage
@app.route("/")
def homepage():
    # return "<h1>Welcome to Flask Tutorial</h1>"
    return render_template('home.html')

@app.route("/about")
def aboutpage():
    return render_template('about.html')
    # return "<b>About us page of Flask</b>"

@app.route("/services")
def servicespage():
    return render_template('services.html')
    # return "<b>About us page of Flask</b>"

@app.route('/data/<name>')
def displaydata(name):
    return f"This is data about {name}"

@app.route('/data')
def data():
    return redirect(url_for('displaydata',name='Attar'))

@app.route("/mydata/<name>")
def mydata(name):
    return render_template('mydata.html',username=name)



@app.route("/addition/<int:fnum>/<int:snum>")
def addition(fnum,snum):
    result = fnum + snum
    return render_template('addition.html',fnum = fnum,snum = snum,result = result)

@app.route("/userdetails",methods=['GET','POST'])
def userdetails():
    if request.method=="GET":
        data = request.args.get('fullname')
        mobileno = request.args.get('mobileno')
    return render_template('userdetails.html',fullname=data,mobileno=mobileno)

@app.route("/myform")
def myform():
    return render_template('myform.html')