from flask import Flask,request,render_template,redirect,url_for,flash
import mysql.connector
from flask_session import Session
from flask_bcrypt import Bcrypt
from dmail import sendmail
from stoken import token
from itsdangerous import URLSafeTimedSerializer
from key import secret_key,salt1,salt2
#kzxw bjoj lapa zjev

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = secret_key
app.config['SESSION_TYPE']='filesystem'

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
        cursor.execute('select * from user where Email=%s',[Mail])
        count = cursor.fetchone()
        cursor.close()
        print(count)
        if count == 1:
            flash('Email Already In use')
            return render_template('register.html')
        userinfo = {'name':Name,'mail':Mail,'pwd':Pwd,'ph':Phone,'place':Place}
        subject='Email Authentication & Confirmation'        
        body=f"Thanks for signing up\n\nfollow this link for further steps-{url_for('confirm',token=token(userinfo),_external=True)}"
        sendmail(to=Mail,subject=subject,body=body)
        flash('Confirmation link sent to ur registred mail')
        return render_template('register.html')
    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm(token):
    try :
        datta = URLSafeTimedSerializer(secret_key)
        userinfo = datta.loads(token,salt=salt1,max_age=60)
    except Exception as e:
        #print(e)
        return 'sorry this link expiredddd plz register after somettime Have a Good Day'
    else:
        cursor = mydb.cursor(buffered=True)
        cursor.execute('insert into user(Name,Email,pwd,phno,place) values(%s,%s,%s,%s,%s)',[userinfo['name'],userinfo['mail'],userinfo['pwd'],userinfo['ph'],userinfo['place']])
        mydb.commit()
    return redirect(url_for('login'))


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