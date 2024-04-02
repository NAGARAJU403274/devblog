from flask import Flask,request,render_template,redirect,url_for
import mysql.connector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

mydb = mysql.connector.connect(host='localhost',user='root',password='admin',database='user')

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        Name = request.form['name']
        Mail = request.form['email']
        Pwd = request.form['password']
        pwd = bcrypt.generate_password_hash(Pwd)
        Phone = request.form['phone']
        Place = request.form['place']
        cursor = mydb.cursor(buffered=True)
        cursor.execute('insert into user(Name,Email,pwd,phno,place) values(%s,%s,%s,%s,%s)',
        [Name,Mail,pwd,Phone,Place])
        mydb.commit()
        cursor.execute('select * from user')
        sql = cursor.fetchall()
        print('sql sotred data-----------',sql)
        data = {'name':Name,'mail':Mail,'pwd':Pwd,'ph':Phone,'place':Place}
        if data['mail'] and data['pwd']:
            print(data['mail'], data['pwd'])
            return redirect(url_for('login',mail=data['mail'],pwd=data['pwd']))
        else:
            return render_template('register.html')
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['D@TT@']
        pwd = request.form['pwd']
        cursor = mydb.cursor(buffered=True)
        cursor.execute('select Email,pwd from user where Email=%s',[email])
        e_mail,passwrd = cursor.fetchone()
        if email == e_mail and bcrypt.check_password_hash(passwrd,pwd)== True:
            return [e_mail,pwd]
        else:
            return redirect(url_for('register'))
    return render_template('login.html')

app.run(use_reloader=True,debug=True)