from connector import connect

cursor = connect.cursor()

class Student():
    def __init__(self,name,age,city):
        self.name = name 
        self.age = age 
        self.city = city 
    def save(self):
        if student.validate():
            cursor.execute("INSERT INTO BIONCHINES_STUDENTS (name,age,city) values (%s,%s,%s);",(self.name,self.age,self.city))
            connect.commit()
        else:
            print("ERROR")

    def validate(self):
        if not isinstance(self.name,str):
            return False
        if not isinstance(self.age,int):
            return False
        if not isinstance(self.city,str):
            return False
        return True

student = Student("YOUSSEF",13,"AGADIR")
print(student.validate())
if connect.is_connected():
    print("CONNECTED")