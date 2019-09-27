class Person:
    def __init__(self):
        print("Person Constructor called..");

    def get(self):
        self.name=input("Enter ur name:");
        self.age=int(input("Enter ur age:"));
        self.bdate=input("Enter ur birth date:");
        self.gender=input("Enter gender (m/f):");

    def show(self):
        print("Name: ",self.name);
        print("Age: ",self.age);
        print("Birth date: ",self.bdate);
        print("Gender: ",self.gender);

class Student(Person):
    def __init__(self):
        super().__init__();
        print("Student Constructor called..");

    def get(self):
        super().get();
        self.sem=input("Enter semester:");
        self.py_marks=int(input("Enter python marks:"));
        self.j_marks=int(input("Enter java marks:"));
        self.php_marks=int(input("Enter php marks:"));

    def calc_total(self):
        self.total=self.py_marks+self.j_marks+self.php_marks;

    def calc_percentage(self):
        self.per=self.total*100/300;

    def calc_grade(self):
        if(self.per <99 and self.per >=70):
            self.grade='A';
        elif(self.per <70 and self.per >=60):
            self.grade='B';
        elif(self.per <60 and self.per >=50):
            self.grade='C';
        elif(self.per <50 and self.per >=40):
            self.grade='D';
        else:
            self.grade='F';

    def show(self):
        super().show();
        print("Semester: ",self.sem);
        print("Python marks: ",self.py_marks);
        print("Java Marks: ",self.j_marks);
        print("Php marks: ",self.php_marks);
        print("Total: ",self.total);
        print("Percentage: ",self.per);
        print("Grade: ",self.grade);

class Employee(Person):
    def __init__(self):
        super().__init__();
        print("Employee constructor called..");

    def get(self):
        super().get();
        self.bs=int(input("Enter Basic salary:"));

    def calc_da(self):
        if(self.gender == 'f' or self.gender == 'F'):
            self.da=self.bs*100/70;
        elif(self.gender == 'm' or self.gender == 'M'):
            self.da=self.bs*100/80;

    def calc_hra(self):
        if(self.gender == 'f' or self.gender == 'F'):
            self.hra=self.bs*100/15;
        elif(self.gender == 'm' or self.gender == 'M'):
            self.hra=self.bs*100/10;

    def calc_gs(self):
        if(self.age >40):
            self.bonus=(bs/2)*2/100;
            self.gs=self.bs+self.ds+self.hra+self.bonus;
        else:
             self.gs=self.bs+self.da+self.hra;

    def calc_ns(self):
        self.ns=self.gs;

    def show(self):
        super().show();
        print("Basic salary: ",self.bs);
        print("Gross salary: ",self.gs);
        print("Net salary: ",self.ns);
        
print('\n 1.Student \n 2.Employee');
c=int(input("Enter ur profession:"));
if(c==1):
    s1=Student();
    s1.get();
    s1.calc_total();
    s1.calc_percentage();
    s1.calc_grade();
    s1.show();
else:
    e1=Employee();
    e1.get();
    e1.calc_da();
    e1.calc_hra();
    e1.calc_gs();
    e1.calc_ns();
    e1.show();
