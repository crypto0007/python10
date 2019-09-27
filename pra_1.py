class String:
    def __init__(self):
        print("Default Constructor is called...");
        

    def __init__(self,str1,str2):
        print("Parameterized constructor is called...");
        self.str1=str1;
        self.str2=str2;

    def get_length(self):
        return len(self.str1);

    def join_string(self):
        return (str1+" "+str2);

    def compare(self):
        if(self.str1==self.str2):
            return True;
        else:
            return False;

    def reverse(self):
        return str1[::-1];

    def check_palindrom(self):
        temp=str1[::-1];
        if(temp==str1):
            return True;
        else:
            return False;

    def check_word(self):
        str=input("enter string:");
        word=input("Enter word u want to search:");
        if word in str:
            return True;
        else:
            return False;

    def menu(self):
        while(1):
            print("Menu:");
            print("\n 1.String length \n 2.Join string \n 3.compare string \n4.Reverse String \n5.Check palindrome \n6.check word in sentense \n 7.exit");
            c=int(input("Enter choice:"));
            if(c==1):
                print("Length of the String:",self.get_length());
            elif(c==2):
                print("join string: ",self.join_string());
            elif(c==3):
                print("compare strings: ",self.compare());
            elif(c==4):
                print("Reverse String: ",self.reverse());
            elif(c==5):
                print("palindrome: ",self.check_palindrom());
            elif(c==6):
                print("Word is available in sentense: ",self.check_word());
            else:
                break;
str1=input("Enter string 1:");
str2=input("Enter string 2:");
s1=String(str1,str2);
s1.menu();
