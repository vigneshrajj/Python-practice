#1
from functools import reduce
li=[x for x in range(1,1000) if x%3==0 or x%5==0]
val=reduce(lambda a,b : a+b,li)
print(val)



#2
P,fib,f1,f2= 0,0,1,0
fibl = []
while fib < 4000000:
    fib = f1 + f2
    f2,f1 = f1,fib
    if fib % 2 == 0:
        P += fib
        fibl.append(fib)
print(P)  

  

#3
flag,num=0,600851475143
for i in range(2,num):
    if(num%i==0):
        for j in range(2,i):
            if(i%j==0):
                flag=1
            else:
                continue
        if(flag==0):
            print(i)
            


#4
maxx=0
for i in range(100,1000):
    for j in range(100,1000):
        num=str(i*j)
        s=num[::-1]
        if((num==s)and (int(s)>maxx)):
            maxx=int(s)
            


#5
maxx,i=0,1
while maxx==0:
    for j in range(11,21):
        if(i%j!=0):
            break
    if((j==20)and(i>maxx)):
        maxx=i
    i+=1
print(maxx)
        


#6
from functools import reduce
li=reduce(lambda a,b:a+b,[x*x for x in range(101)])
li1=(reduce(lambda a,b:a+b,[x for x in range(101)]))**2
print(li1-li)



#7
maxx=0
for num in range(2,10002):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if (prime and (num>maxx)):
       maxx=num
print(maxx)



#8
numl='7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
maxx=0
for i in range(len(numl)-12):
    mult=1
    for j in range(0,13):
        mult*=int(numl[i+j])
    if(mult>maxx):
        maxx=mult
print(maxx)



#9
for i in range(1000):
    for j in range(i+1,1000):
        for k in range(j+1,1000):
            if((i+j+k==1000)and(i**2+j**2==k**2)):
                print(i*j*k)
                break
            
            
            
#10
summ=0
li=list()
for i in range(2,2000000):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
        else:
            continue
    if(flag==0):
        summ+=i
print(summ)
