#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#Extras:
#
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
name=input('Enter your name: ')
age=int(input('Enter your age: '))
left=100-age
message="Hey "+ name +" ,Years left for you to become 100 years old: "+ str(left) +"\n"
mult=int(input('Enter a number: '))
print(message*mult)



num=int(input('Enter a number: '))
if(num%2==0 and num%4!=0):
    print('Your number is even')
elif(num%4==0):
    print('Your number is multiple of 4')
else:
    print('Your number is odd')
    
    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[i for i in a if i<5]
print(b)




a=int(input('Enter a number: '))
b=[i for i in range(1,a) if a%i==0]
print(b)




import random
a = [random.randint(1,10) for i in range(10)]
b = [random.randint(1,10) for i in range(15)]
c= set(a) and set(b)
print(c)



a = [random.randint(1,10) for i in range(10)]
print(a,a[0],a[-1])