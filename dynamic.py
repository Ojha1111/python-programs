def lcw():
    u="secretary"
    v="secret"
    lcw=([0]*(len(v)+1 for x in range(len(u)+1))
    max = 0
    for c in range(len(v)-1,-1,-1):
         for r in range(len(u)-1,-1,-1):
            if u[r]==v[c]:
                 lcw[r][c]=lcw[r+1][c+1]+1
            else:
                 lcw[r][c]=0
            if lcw[r][c]>max:
                 max=lcw[r][c]
         return(max)
print lcw()
         
