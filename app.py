# We have to import Flask class from flask module. Following line adds the flask module.
from flask import Flask
from flask import render_template
from flask import url_for,redirect
from flask import request

# Import database module
import mysql.connector as connector

# connect with database
def dbconnection():
    connection = connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_school")
    print(connection)
    return connection


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


@app.route("/student/loginpage")
def loginPage():
    return render_template("loginpage.html")

@app.route("/student/login",methods=["GET","POST"])
def login():
    x = False
    if request.method=="POST":
        username = request.form['email']
        password = request.form['password']
        if username=="tushar@gmail.com" and password=="admin123":
            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('loginPage'))


# addition task

@app.route("/add/task")
def add():
    return render_template("task.html")


@app.route("/add/result",methods=["GET","POST"])
def add1():
    if request.method=="POST":
        input1 = request.form['input1']
        input2 = request.form['input2']        
        result = int(input1) + int(input2)
        return render_template('addition.html',fnum=input1,snum=input2,result=result)

@app.route("/signuppage")
def signuppage():
    return render_template('signup.html')

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":
        name = request.form['fullname']
        email = request.form['email']
        contactno = request.form['contactno']
        password = request.form['password']
        return render_template('userdata.html',name=name,email=email,contactno=contactno,password=password)
    return redirect(url_for('signuppage'))

@app.route("/evenodd",methods=['GET','POSt'])
def evenodd():
    return render_template('evenodd.html')

@app.route("/evenodd/result",methods=['GET','POST'])
def checkevenodd():
    if request.method == "POST":
        num = int(request.form['num'])
        if num%2==0:
            heading = "EVEN NUMBER"
            message = f"{num} is EVEN number"
            cls="success"
        else:
            heading = "ODD NUMBER"
            message = f"{num} is ODD number"
            cls="danger"
    return render_template('even-odd-result.html',message = message,cls=cls,heading=heading)

@app.route("/student/registration")
def studentregistration():
    return render_template("student-registration.html")

@app.route("/student/add",methods=['GET','POST'])
def studentadd():
    if request.method=='POST':
        name = request.form['fullname']
        city = request.form['city']
        dob = request.form['dob']
    else:
        name = request.args.get('fullname')
        city = request.args.get('city')
        dob = request.args.get('dob')

    connection = dbconnection()
    x = f"INSERT INTO tbl_student(studname,studcity,studdob) VALUES('{name}','{city}','{dob}');"
    cursor = connection.cursor()
    cursor.execute(x)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('studentregistration'))

# TASK

@app.route("/teacher/registration")
def teacherregistration():
    return render_template("teacher-registration.html")

@app.route("/teacher/add",methods=['GET','POST'])
def teacheradd():
    if request.method=='POST':
        tname = request.form['fullname']
        tcity = request.form['city']
        tdob = request.form['dob']
        salary = request.form['salary']
    else:
        "false"

    connection = dbconnection()
    sql = f"INSERT INTO teacher(tname,tcity,tdob,salary)VALUES('{tname}','{tcity}','{tdob}','{salary}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('teacherregistration'))