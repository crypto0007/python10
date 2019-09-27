class Student:
    count=0;
    def __init__(self):
        self.name="saloni";
        Student.count=Student.count+1;

    def show(self):
        print("name: ",self.name);
        print("Count: ",Student.count);

s1=Student();
s1.show();
s1.name="Khantil";
Student.count=5;
s1.show();
