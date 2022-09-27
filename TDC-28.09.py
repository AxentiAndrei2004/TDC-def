import math
from ssl import OP_NO_RENEGOTIATION
a=int(input('Introduceti numarul a='))
b=int(input('Introduceti numarul b='))
c=int(input('Introduceti numarul c='))

def div_max(x,y,z):
    while(True):
        for i in range(1,max(x,y,z)+1):
            if x%i==0 and y%i==0 and z%i==0:
                divmax=i
            return divmax

def mult_min(x,y,z):
    if a>b and a>c:
        m=a
    if b>a and b>c:
        m=b
    if c>a and c>b:
        m=c
    while(True):
        if((m%a==0) and (m%b==0) and (m%c==0)):
            mult=m
            break
        m+=1
    return mult

def max(x,y,z):
    if a>b:
        if c>a:
            max=c
        else:
            max=a
    else:
        if c>b:
            max=c
        else:
            max=b
    return max

def min(x,y,z):
    if a<b:
        if c<a:
            min=c
        else:
            min=a
    else:
        if c<b:
            min=c
        else:
            min=b
    return min

def div_com(x,y,z):
    com=[]
    for i in range(1,int(max(x,y,z)/2)+1):
        if x%i==0 and y%i==0 and z%i==0:
            com.append(i)

    return com

def multipli_trei(x,y,z):
    mult=[]
    for i in range(1,x**5):
        for q in range(1,y**5):
            for r in range(1,z**5):
                if x*i==y*q and y*q==z*r:
                    mult.append(x*i)
                if len(mult)==3:
                    return mult

def triun(x,y,z):
    if x+z>y and z+y>x and x+y>z:
        P=(x+y+z)/2
        A=math.sqrt(P*(P-x)*(P-z)*(P-y))
        return f'Poate fi triunghi, cu aria{A} si perimetrul{P}'
    else:
        return f'Nu poate fi triunghi'

def sol_reale(x,y,z):
    D=(b**2)-4*a*c
    if D>0:
        x1=((-b)-math.sqrt(D)/(2*a))
        x2=((-b)+math.sqrt(D)/(2*a))
        sol=str(a)+""+str(x2)
    if D==0:
        x=(-b)/(2*a)
        sol+=str(x1)
    else:
        return f'Solutiile ecuatiei{sol}'
print('Cel mai mare divizor comun',div_max(a,b,c))
print('Cel mai mic multiplu comun',mult_min(a,b,c))
print('Valoarea Maxima',max(a,b,c))
print('Valoarea minima',min(a,b,c))
print('Divizorii comuni',div_com(a,b,c))
print('Trei multipli comuni',multipli_trei(a,b,c))
print('Numerele citite pot fi lungimile laturilor unui triunghi',triun(a,b,c))
print('Solutiile reale pentru ecuatia patratica',sol_reale(a,b,c))
    




