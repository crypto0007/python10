class stringc:
    def __init__(self,str2,str3):
        self.str0=str2
        self.str1=str3
    
    def strlen(self):
        print("length of the string is:",len(self.str0))

    def compstr(self):
        if(self.str0==self.str1):
            print("euqal = true")
        else:
            print("equal = false")

    def revstr(self):
        print("Reverse String:",self.str0[::-1])

    def palin(self):
        temp=self.str0
        if(temp==self.str0):
            print("palindrom = true")
        else:
            print("palindrom = false");

    def chkwod(self):
        wd=input("Enter word you want:")
        if wd in self.str0:
            print("available")
        else:
            print("Not available")
        
s0=stringc("ishaan","patel")
s0.strlen()
s0.compstr()
s0.revstr()
s0.palin()
s0.chkwod()
