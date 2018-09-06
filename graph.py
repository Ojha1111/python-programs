n=int(input("enter no. of vertices"));
graph=[[0]*n]*n;
type=int(input("enter 1 for eighted or 2 for unweighted graph"));
if type==1:
    infinity=999;
else:
    infinity=0;
for i in range(n):
    for j in range(n):
        value=int(input("is thus any path in %d and %d",(i,j)));
        if value==0:
             graph[i][j]=infinity;
        elif type==1 and value !=0:
            weight=int(input('enter the value of the path :'))
            graph[i][j]=weight
        else:
            graph[i][j]=1
print('enter the graph is :')
for i in range(n):
    for j in range(n):
        print(graph[i][j],end=' ');
print( );
            
