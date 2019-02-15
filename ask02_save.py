def firstnum(a):
    tmp=True
    i=2
    while i<a :
        if a%i==0:
            tmp=False
            break
        else:
            i=i+1
    return tmp  
print "give me a number"
a=input()
j=0
listof_first=a*[0]
charl=a*[""]
k=-1
fores=a*[0]

for i in range(2,a+1):
    
    if (a%i==0) and firstnum(i)==True:
        k=k+1
        t=a
        pl=0
        listof_first[j]=i
        while t%i==0:
           t=t/i
           fores[k]=fores[k]+1
        j=j+1
for i in range(0,j):
    a1=str(listof_first[i])
    a2=str(fores[i])
    my_list = [a1, a2]
    charl[i]="**".join(my_list)
list_1=list(filter(lambda a: a != "", charl))
print ")(".join(list_1)

