import math 
class calculator:
    def __init__(self,fnum,lnum):
        self.fnum=fnum
        self.lnum=lnum
    def add(self):
        return "SUM:{}".format(self.fnum+self.lnum)
    def sub(self):
        return "SUBSTRACTION:{}".format(self.fnum-self.lnum)
    def mul(self):
        return "MULTIPLICATION:{}".format(self.fnum*self.lnum)
    def div(self):
        return "DIVISION:{}".format(self.fnum/self.lnum)
    def sr(self):
        print("square root of {} is {} ".format(self.fnum,math.sqrt(self.fnum)))
        return "square root of {} is {} ".format(self.lnum,math.sqrt(self.lnum))
    def fact(self):
        print("factorial {} is {}".format(self.fnum,math.factorial(self.fnum)))
        return "factorial {} is {}".format(self.lnum,math.factorial(self.lnum))
    def sine(self):
        print("sin value {} is {}".format(self.fnum,math.sin(self.fnum)))
        return "sin value {} is {}".format(self.lnum,math.sin(self.lnum))
    def cosin(self):
        print("cos value {} is {}".format(self.fnum,math.cos(self.fnum)))
        return "cos value {} is {}".format(self.lnum,math.cos(self.lnum))
    def tan(self):
        print("tan value {} is {}".format(self.fnum,math.cos(self.fnum)))
        return "tan value {} is {}".format(self.lnum,math.cos(self.lnum))
    def power(self):
        return "{} to the power {} is {}".format(self.fnum,self.lnum,math.pow(self.fnum,self.lnum))
    
if __name__ == '__main__':
    name=input("Enter Your Name")
    print("!Welcome")
    print("enter the following operation you wants to Perform")
    d=calculator(int(input("Enter the 1st Number")),int(input("Enter the 2nd Number")))
    print("1:add\n2:sunstraction\n3:multiplication\n4:division\n5:square root\n6:factorial\n7:sin value\n8:cos value\n9:tan value\n10:power")
    x=int(input())
    if x==1:
        print(d.add())
    elif x==2:
        print(d.sub())
    elif x==3:
        print(d.mul())
    elif x==4:
        print(d.div())
    elif x==5:
        print(d.sr())
    elif x==6:
        print(d.fact())
    elif x==7:
        print(d.sine())
    elif x==8:
        print(d.cosin())
    elif x==9:
        print(d.tan())
    elif x==10:
        print(d.power())
    else:
        print("!NO OPERATION FOUND")
print("THANK YOU USING THIS CALCULATOR {}!".format(name))
        
        
   
