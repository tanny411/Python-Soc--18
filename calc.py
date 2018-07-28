#to start the program
"""
print(1+2)
print('aysha')
print('aysha' + 'kamal')
print('lekh '*4) """
#print('aysha'*'kamal') nope :v
"""
print('aysha is '+str(22)+' years old')
print('you\'re cool')
print("you're cool")
"""
# 'python' in command line to directly code in there, exit() to exit
# e.g name='aysha', then if I print(name) in command line or simply write name, wala!
name='some-name tadatada'
n=len(name)
# print(n)
# # print(name[n-1])
# for i in range(0,9):
#     print(name[i]) #from 0, go till 8
# for i in range(0,len(name)):
#     if i%2==0: print(name[i])
# print(name[-3]) #3 no. letter from the end; notice backward indexing is from 1, i.e -1 is the last one.

##string int mixin
# var1='10'
# var2=98
# print(var1+str(var2))
# print(int(var1)+var2)
# print(float(var1)+var2)
### results: 1098, 108, 108.0

"""
##need to retype the following , as they were sopid from site and still have formatting with them
float('15')​
float('99.999'​)
int('99.999'​)

int('5 is my favorite number!'​) #error
int('Who asked you about 5 or whatever?'​) #error
float('Your momma did.'​) #error

str('stringy'​)
int(3)
"""
# # they are same cuz python turns everything into string inorder to print
# print(30)
# print('30'+'aysha')
# var='50'
# print(var)

# pet=input("pet name?")
# print("so your pets name is "+pet) #input is always in string

# str="aysha kamal"
# print(str.center(40,'.'))
# print(str.ljust(40,'.'))
# print(str.rjust(40,'.'))

# import random
# print (random.randint(1,101)) #(1 to 100)

# https://docs.python.org/3/library/math.html
# function fmod() is generally preferred when working with floats, while Python’s x % y is preferred when working with integers.

"""
text=""
while text!="bye":
    text=input("say something please ")
    if text=="fuck": 
        print("THATS ENOUGH")
        break
print("Good Bye!")
"""

"""
for x in range (5):
    print(x)

print("another loop")
for x in range (3,8):
    print(x)

print("now with steps")
for x in range (5,9,2):
    print(x)
"""
print("for loop in lists")
ara=["aysha","tanny","kamalamala","blekhop"]
for s in ara:
    #print(s+" is one of the elements of the array")
    if len(s)>7:
        print("LONG NAME")
    elif len(s)==7:
        print("7 characters")
    else:
        print("MINIMAL")

