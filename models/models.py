import json
import uuid
import datetime

#-----------------JSON-------------------------
def read_json(filename):
    content = None
    with open(filename, 'r') as f:
        content = json.load(f)
    return content

def write_json(filename, data):
    with open(filename, 'w') as f:
        json_obj = json.dumps(data, indent=4)
        f.write(json_obj)

    
#------------------------------------------------

def creatTime():
    creatTime = datetime.datetime.now()
    return str(creatTime)

def uuid_generater():
    json_id = uuid.uuid1()
    return str(json_id)

json_files_pathway = "C:/Users/murat/Documents/Projects/WebApplicationProject/files/users.json"
#------------------------------------------------

def findAllUser(data):
    print(data)

def findOneUser(data,id):
    for i in range(0,len(data)):
        if data[i]["id"] == id:
            print(data[i])
            
def addUser(name, password):
    newUser = {"id" : uuid_generater(), "username" : str(name), "password": str(password), "creat_on": creatTime()}
    with open(json_files_pathway) as file:
        data = json.load(file)
        data.append(newUser)
    with open(json_files_pathway, "w") as file:
        json.dump(data,file,indent=4)
#------------------------------------------------


write_json(json_files_pathway,
[{"id" : uuid_generater() ,"username" : "ali", "password": "12345", "creat_on": creatTime()},
 {"id" : uuid_generater(), "username" : "ahmet", "password": "456", "creat_on": creatTime()}])
data = read_json(json_files_pathway)


