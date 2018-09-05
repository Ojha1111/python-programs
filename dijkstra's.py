graph=[[999,4,2,20],[4,999,999,3],[2,999,999,6],[20,3,6,999]]
n=len(graph[0]);
vertices=[]
destination=[]
src=[]
distance=[]
d=0
s=int(input("enter the source vertex: "));
dest=int(input("enter destination vertex: "));
curr=s;
while True:
    for i in range(n):
        if i not in vertices and graph[curr][i] != 999:
            distance.append(d+graph[curr][i]);
            src.append(curr);
            destination.append(i);
    d=min(distance);
    verttices.append(curr);
    if dest in vertices:
        break;
    pos=distance.index(d);
    curr=destination[pos];
    del distance[pos];
    del src[pos];
    del destination[pos];
print("minimum distance : ",d);
