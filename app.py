from flask  import Flask, render_template , request, jsonify
from models import models 

app = Flask(__name__)

@app.route('/')
def index():
   return "main page"

@app.route('/users/<user_id>', methods = ["POST"])
def getUser(user_id):
   data = request.json
   data = models.readJson(models.json_files_path)
   for i in range(0,len(data)):
      if data[i]["id"] == user_id:
         print(data[i])
         break
      
      else:
         print("There is no user with this ID")
         break
   return jsonify(data), 200

@app.route('/newuser', methods=["POST"])
def newUser():
   data = request.json
   print(data["name"],data["password"])
   models.addUser(data["name"],data["password"])
   return jsonify(data), 200

@app.route('/readUser', methods=["POST"])
def postTest():
   data = models.readJson(models.json_files_path)
   print(data)
   return jsonify(data), 200

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

@app.route('/login', methods = ["GET","POST"])
def login():
   username = request.form.get("username")
   password = request.form.get("password")
   print("save new user name:{} password:{}".format(username,password))
   models.addUser(username,password)
   return render_template("login.html")

if __name__ == '__main__':
   app.run(debug = True)

#------------------------------------------------------#
# http://localhost:5000/admin
# venv\Scripts\activate 
# source ./venv/bin/activate
