from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="gec")
@app.route('/', methods=['POST'])
def process_form():
    if request.method =='POST':
        print(request.form)
        name = request.form['name']
        email = request.form['email']
        data={'name':name,'email':email}
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into naga(name,email) values (%s,%s)',[name,email])
        mydb.commit()
        cursor.execute('select * from naga')
        sql=cursor.fetchall()
        print("stored ----",sql)
        cursor.close()
    return render_template('index.html',name=data)

if __name__ == '__main__':
    app.run(debug=True)
