# -*- coding: cp1253 -*-
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
print "Δωσε την αρχικη τιμη του διαστηματος "
a=input()
tmp=False
while (tmp==False ): 
    print "Δωσε την τελικη τιμη του διαστηματος "
    b=input()
    if b>a :
        tmp=True
print "Δωσε ενα ακεραιο αριθμο δ"
d=input()
d=int(d)
j=0
for i in range(a,b+1):
    tmp1=firstnum(i)
    if tmp1==True:
        j=j+1
a1_list=j*[1]
k=0
for i in range(a,b+1):
    tmp1=firstnum(i)
    if tmp1==True:
        a1_list[k]=i
        k=k+1
array=(j-1)*[1]
for i in range(1,k-1):
    array[i]=a1_list[i]-a1_list[i-1]
    if array[i]==d:
        print (a1_list[i-1],',',a1_list[i])
        break
