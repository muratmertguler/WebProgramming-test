from cmath import log
from unicodedata import name
from flask import Flask , redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "my firs web application"

@app.route('/admin')
def admin():
   log_txt = open("log.txt","a")
   log_txt.write("admin kullanicisi girisi yaptı \n")
   log_txt.close()
   #log_txt = open("log.txt","r")
   #print(log_txt.read())
   return "admin"

@app.route('/guest/<guest>')
def guest(guest):
   log_txt = open("log.txt","a")
   log_txt.write("guest : " + guest + "\n" )
   log_txt.close()
   #log_txt = open("log.txt","r")
   #print(log_txt.read())
   return "guest : %s" % guest 


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('admin'))
   else:
       return redirect(url_for('guest',guest = name)) 


if __name__ == '__main__':
   app.run(debug = True)




# http://localhost:5000/admin
# venv\Scripts\activate -> venv activetion



#---------------------------------------------------------#
"""
a1 = "asdas"
log_txt = open("log.txt","a")
log_txt.write("admin kullanicisi girisi yaptı \n" + a1)
log_txt.close()

log_txt = open("log.txt","r")
print(log_txt.read())
"""