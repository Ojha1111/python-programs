graph={'a':['b','c','d'],'b':['c','e'],'c':['f'],'d':['c','g'],'e':['h'],'f':['e','g'],'g':['h'],'h':[]}
status={}
for i in graph:
    status[i]=0;
queue=[]
root=input("enter root element :");
queue.append(root);
status[root]=1;
while len(queue)!=0:
    element=queue[0];
    print(element)
    status[element]=2;
    for i in graph[element]:
        if status[i]==0:
            queue.append(i);
            status[i]=1;
    del queue[0];
