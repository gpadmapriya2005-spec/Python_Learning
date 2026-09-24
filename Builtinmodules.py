# Import required modules
import math
import random
import sys
import platform
import collections
import itertools
from datetime import datetime, date, timedelta

#Math module
print('------------Math Module----------------')
print('Square root of 25:', math.sqrt(25))   #5
print('Power (2^3):', math.pow(2, 3))        #8
print('Value of PI:', math.pi)               #3.14
print('Ceiling of 4.3:', math.ceil(4.3))     #5
print('Ceiling of -4.3:', math.ceil(-4.3))   #-4
print('Floor of 4.8:', math.floor(4.8))      #4
print('Floor of -4.8:', math.floor(-4.8))    #-5
print('Factorial of 5:', math.factorial(5))  #120
print('GCD of 12 and 18:', math.gcd(12, 18)) #6
print('LCM of 12 and 18:', math.lcm(12,18))  #36
print('Sine of 45 radians:', math.sin(45))   #address
print('Cosine of 45 radians:', math.cos(45))  #address
print('Tangent of 45 radians:', math.tan(45))  #address
print('Degrees of 45 radians:', math.degrees(45))  #address
print('Radians of 45 degrees:', math.radians(45))  #address
print()
print()

# Random Module
print('-------------Random Module--------------')
# random float between 0.0 to 1.0 including
print('Random float:', random.random())
# random float between x to y including
print('Random float from x to y:', random.uniform(1,10))
# random does not take any arguments
print(random.random(1,10))   #(2,4,5,6,7,8,9)
# random int between x to y including
print('Random integer:', random.randint(1, 100))
# random int between x to y-1 in steps of z 
print('Random integer from 1 to 20 insteps of 2:', random.randrange(1,21,2))
#random with list
numbers = [10, 20, 30, 40, 50]
print('Random choice:', random.choice(numbers))  #50
random.shuffle(numbers)
print('Shuffled list:', numbers)  #[20,40,30,50,10]
print('Random sample:', random.sample(numbers, 3))  #[30,20,10]
print()
print()


# Sys module
print('----------------Sys Module----------------')
print('Python version:', sys.version)                 #AMD64
print('Python executable:', sys.executable)           #executable address
print('Number of command-line arguments:', len(sys.argv))  #1
print()
print()

# Platform Module
print('--------------Platform Module--------------')
print('Operating system:', platform.system())  #Windows
print('Machine:', platform.machine())          #AMD64
print('Processor:', platform.processor())      #Intel64 Family 6 Model 142 Stepping 12, GenuineIntel
print('Python implementation:', platform.python_implementation())   #CPython
print()
print()

# Collections Module
print('---------------Collections Module----------------')
# Counter
words = ['rakesh', 'adhithya', 'rakesh', 'charan', 'adhithya', 'rakesh']
counter = collections.Counter(words)
print('Word count:', counter)
# Most common item
print('Most common:', counter.most_common(1))  #[('rakesh' 3)]
print('Most common:', counter.most_common(2))  #[('rakesh',3),('aditya',2)]
print()
# DefaultDict
student_marks = collections.defaultdict(list)
student_marks['Alice'].append(90)   
student_marks['Alice'].append(85)
student_marks['Bob'].append(78)
print('Student marks:', dict(student_marks))  #{'Alice':[90,85],'Bob':[78]}
print()
# NamedTuple
Student = collections.namedtuple('Student', ['name', 'age', 'course'])
student = Student('John', 20, 'Python')
print('Student tuple:', student)     #Student', (name='John', age='20', course='Python')
print('Student name:', student.name) #John
print('Student age:', student.age)   #20
print('Student course:', student.course)  #Python
print()
print()

# Itertools module
print('--------------Itertools Module--------------')
items = ['A', 'B', 'C']
# Permutations
print('Permutations:')   
permutations = itertools.permutations(items)
print(list(permutations))  #[('A','B','C'),('A','C','B'),('B','A','C'),('B','C','A'),('C','A','B'),('C','B','A')]
# Combinations
print('Combinations:')   #[('A','B'),('B','C'),('C','A')]
combinations = itertools.combinations(items, 2)
print(list(combinations))
# Product
print('Cartesian product:')  #[(1,'A'),(1,'B'),(2,'A'),(2,'B')]
cproduct = itertools.product([1, 2], ['A', 'B'])
print(list(cproduct))
print()
print()

# Datetime Module
print('------------------Datetime Module-------------------')
# Current date and time
now = datetime.now()
print('Current date and time:', now)  #24 11.45
# Current date
today = date.today()  
print('Today\'s date:', today)  #24
# Format date and time
print('Formatted date:', now.strftime('%d-%m-%Y'))  #24-9-2026
print('Formatted time:', now.strftime('%H:%M:%S'))  #11:45:04
# Create a specific date time
birthday = datetime(2000, 5, 15, 19, 50, 50)
print('Example birthday:', birthday)   #2000-5-15 19:50:50
# Add days
future_date = today + timedelta(days=7)
print('Date after 7 days:', future_date)  #2026-10-01
# Subtract days
past_date = today - timedelta(days=7)
print('Date 7 days ago:', past_date)   #2026-09-17

