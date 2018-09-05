n=int(input("enter no of vertices: "));
graph={ };
for i in range(n):
    node=input("enter name of vertex");
    graph[node]=[];
for i in graph:
    m=int(input("enter no of edges of for node %s"%i));
    for j in range(m):
        adj=input("enter adjacent vertex name : ");
        if adj in graph:
            graph[i].append(adj);
        else:
            break;
    print(graph);
