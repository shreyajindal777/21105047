#Question 1

def moveTower(n, source, dest, temp):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", dest+".")
        return
    moveTower(n-1, source, temp, dest) 
    print('Move disk',n,'from source',source,'to destination',dest+'.')
    moveTower(n-1,temp,dest,source)
    
n=3
moveTower(n,'A','B','C')



#Question 2

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("USING FOR LOOP")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("USING WHILE LOOP")

i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")



#Question 3

val1 = int(input("Enter first integer value(dividend): "))
while True:                                                                                             #Loop to make sure val2 != 0(i.e. denominator must not be 0)
    val2 = int(input("Enter second integer value(divisor): "))
    if val2 != 0:
        break
    else:
        print("\nDivisor must not be 0\nPlease enter the divisor again")
result = divmod(val1,val2)
print("\nQuotient:",result[0],"\nRemainder:",result[1])

print("\na. Check whether the function (divmod()) is callable or not:")                                 #Q3(a)
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(", which means it is callable")
else:
    print(", which means it is not callable")

print("\nb. Check whether all the values are zero or not:")                                             #Q3(b)
if all(x != 0 for x in result):
    print("All values in result(i.e. quotient and remainder) are non-zero.")
else:
    print("All values in result(i.e. quotient and remainder) are not non-zero(i.e. one of them is 0).")

print("\nc. Add (4,5,6) to the result and filter out values greater than 4:")                           #Q3(c)
c_part = result + (4,5,6)
c_part_output = sorted(list((x for x in c_part if x>4)))
print("Values greater than 4(in list format) are:", c_part_output)

print("\nd. Convert the above result into a set datatype:")                                             #Q3(d)
d_part = set(c_part_output)
print("The output of previous part in set datatype would be:", d_part)

print("\ne. Make the set immutable:")                                                                   #Q3(e)
e_part = frozenset(d_part)
print("The immutable set would be:", e_part)

print("\nf. Evaluate the maximum value from the set and find out its hash value:")                      #Q3(f)
f_part = max(e_part)
print("The maximum value from the set is:", f_part)
print("The hash value of %d(considering it to be integer) is %d and its hash value is %d(if we consider %s as a string)." % (f_part,hash(f_part),hash(str(f_part)),str(f_part)))


#Question 4

class Student:                                                                                          
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print("Object Created\n")
    def __del__(self):
        print("\nObject destroyed")
name = input("Enter name of student: ").strip()                                                         
roll_no = int(input("Enter SID of %s: " % (name)))
student1 = Student(name,roll_no)                                                                        
print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))     
del student1          

#Question 5

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part <a> updating salary
employee1.salary = 70000
print(f"a. The updated salary of {employee1.name} is {employee1.salary} ")
#part <b> deleting a record
print("b. Record of Viren deleted", end='')
del employee3
print("\n")



#Question 6

word =input("Enter the word: ")
word=word.lower()


test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word=test_word.lower()

def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N ) ")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input, try again with y/Y or n/N ")
        userinput()
userinput()
