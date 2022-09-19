a=int(input('iNTRODUCETI PRIMUL NUMAR='))
b=int(input('INTRODUCETI AL DOILEA NUMAR='))

import math

def suma(x,y):
    return x+y

def produsul(x,y):
    return x*y

def m_aritmetica(x,y):
    return (x+y)/2   

def M_divizor(x,y):
    while b!=0:
        a,b=abs(b),abs(a%b)
        return a
    
def m_multiplu(x,y):
    return math.lcm(a,b)

def minim(x,y):
    return min(a,b)

def maxim(x,y):
    return(a,b)

def suma_nr_citite():
    n=int(input('Introduceti 1 numarul='))
    m=int(input('Introduceti al 2 numar='))
    return 'c=',m+n

def produsul_nr_citite():
    n=int(input('n='))
    m=int(input('m='))
    return 'c=',m*n

def toti_div_com(x,y):
    div_com=[]
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            div_com.append(i)

    return div_com


def cinci_multipli(x,y):
    multp=[]
    for i in range(1,6):
        multp.append(a*b*i)
    return multp

print('Suma=',suma(a,b))
print()
print()
print()
print()
print()
print()
print()
print()
print()
print ('Cel mai mic multiplu comun=',m_multiplu(10,20))