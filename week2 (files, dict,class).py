def moo(n):
    print("moo"*n)
    return 'moo'*n

# for i in range (10):
#     moo(i)

filename="book.txt"
file = open(filename,'r')

# for line in file:
#      print(line)

#raw doesnt work with the prev. for lop cuz otherwise it goes to the end of
#the file, then then theres nothing to read/rint with raw
raw=file.read()
#print(raw[:3]) #first three chracters
#print(len(raw)) #number of characters inthe file
print(raw[2:5]) #from 2 to 5 indices

#day-2
print(chr(65))

#day3
ara={
    "a":500,
    "b":90,
    "z":98,
    "c":"okay"
}
print(ara)
##access
print(ara["a"])
# print(ara["d"]) #keyError

##add and modify
ara["aysha"]=34.98
print(ara["aysha"])

##delete
del(ara["aysha"])
print(ara)

##length
print(len(ara))

#delete dict
del(ara)
# print(ara) #error ara doesnt exist anymore

##contructor dict
map=dict(first_name="Aysha", last_name="Kamal",reg="2015331042",Inst="SUST")
print(map)

###CLASSES

class Student():
    def __init__(self,reg,name,inst):
        self.reg=reg
        self.name=name
        self.inst=inst

'''
##for no construtor in class
s1=Student()
s1.reg=2015331042
s1.name="tanny"
s1.inst="akhali boro school"
s1.po="po" #THIS IS WEIRD
print(s1.po)
'''

s2=Student(42,"aysha","sust")
print(s2.reg)

##delete class properties *_*
del s2.reg
# print(s2.reg) #Errored
del s2
# print(s2) #Shows error

