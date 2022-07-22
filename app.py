from flask import Flask , redirect, url_for, request, render_template
from datetime import datetime, date, time, timezone
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/admin')
def admin():
   log_txt = open("log.txt","a")
   log_txt.write("admin kullanicisi girisi yaptı \n")
   log_txt.close()
   return "admin"

@app.route('/guest/<guest>')
def guest(guest):
   log_txt = open("log.txt","a")
   log_txt.write("guest : " + guest + "\n" )
   log_txt.close()
   return "guest : %s" % guest 

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('admin'))
   else:
       return redirect(url_for('guest',guest = name)) 

@app.route('/users', methods = ["POST", "GET"])
def users():
   if request.method == 'POST':

      name = request.form.get('name')
      surname = request.form.get('surname')
      username = request.form.get('username')
      password = request.form.get('password')
      return render_template("users.html",name=name, surname=surname, username=username, password=password)
   else:
      return render_template("users.html",hata="hata oluştu")

if __name__ == '__main__':
   app.run(debug = True)

#---------------------------------------------------------#
# http://localhost:5000/admin
# venv\Scripts\activate 

