s=str(input("enter the string \n"))
pos1=s.find("not")
pos2=s.find("poor")
if(pos1<pos2):
    x=s[pos1:pos2+4]
    s=s.replace(x,"good")
