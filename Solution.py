def findContentChildren(g, s):
    s=sorted(s)
    g=sorted(g)
    n1=len(g)
    n2=len(s)
    gstart=0
    sstart=0
    count=0
    while gstart<n1 and  sstart<n2:
        if s[sstart]>=g[gstart]:
            count+=1
            gstart+=1
            sstart+=1
        else:
            sstart+=1
    return count
g=[10,9,8,7]
s=[5,6,7,8]
print(findContentChildren(g,s))



    