from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__)

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
        Phone = request.form['phone']
        Place = request.form['place']
        data = {'name':Name,'mail':Mail,'pwd':Pwd,'ph':Phone,'place':Place}
        if data['mail'] and data['pwd']:
            print(data['mail'], data['pwd'])
            return redirect(url_for('login',mail=data['mail'],pwd=data['pwd']))
        else:
            return render_template('register.html')
    return render_template('register.html')

@app.route('/login/<mail>/<pwd>',methods=['GET','POST'])
def login(mail,pwd):
    if request.method == 'POST':
        user = request.form['D@TT@']
        pwd = request.form['pwd']
        if mail == user:
            return [user,pwd]
        else:
            return redirect(url_for('register'))
    return render_template('login.html')

app.run(use_reloader=True,debug=True)