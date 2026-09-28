from flask import Flask,render_template,request,jsonify
#from connector import connect
#import _mysql_connector
from mystudent import student
import os
from dotenv import load_dotenv
from mystudent import Student

load_dotenv()
base_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(base_dir,'frontend')

server = Flask(__name__,template_folder=frontend_dir)
#if connect.is_connected():
    #print("connected succefully")

@server.route("/")
def HOME():
    return render_template("index.html")

@server.route("/add_student/<name>/<age>/<city>", methods=["POST","GET"])
def add_student(name,age,city):
    student = Student(name,age,city)
    #student.save()
    return jsonify({'res':201}), 201
    
if __name__ == "__main__":
    server.run(debug=True)