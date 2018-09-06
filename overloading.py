class complex:
    'class containt the real and imaginary part.'
    def __init__ (self,r=0.0,i=0.0):
        self.real=r;
        self.imag=i;
    def input(self):
        self.real=float(input("enter real part: "));
        self.imag=float(input("enter imaginary part "));
    def display(self):
        print(self.real,  self.imag);
    def __add__ (s1,s2):
        s=complex();
        s.real=s1.real+s2.real;
        s.imag=s1.imag+s2.imag;
        return(s);
    def __str__ (self):
        return('complex(%d,%d)'%(self.real,self.imag));
    
    def __del__(self):
        print("object destroyed");

    
c1=complex();
c2=complex();
c1.input();
c2.input();
c1.display();
c2.display();
c3=complex();
c3=c1+c2;
c3.display();
print(type(c3));
print(c3);
