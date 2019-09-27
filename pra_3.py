class Person:
    count=0;

    def __init__(self):
        self.name="saloni";
        
    def show(self):
        Person.count=Person.count+1;
        print("Name: ",self.name);
        print("Count: ",Person.count);

    @staticmethod
    def showStatic():
        Person.count=Person.count+1;
        #print("Name: ",self.name);
        print("Count: ",Person.count);
p1=Person();
p1.show();
Person.showStatic();
