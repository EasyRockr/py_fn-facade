#region [1] Python HOME

class PythonHome():
    def __init__(self):
        print("Title: Python Home")
        print("Hello, World!")


#endregion

#region [2] Python Intro

class PythonIntro():
    def __init__(self):
        print("Title: Python Intro")
        print("Hello, World!")

#endregion

#region [3] Python Get Started
import sys

class PythonGetStarted():
    def __init__(self):
        print("Title: Python Get Started")
        print("Version: " + sys.version)

#endregion

#region [4] Python Syntax

class PythonSyntax():
    def __init__(self):
        if 5 > 2:
            print("5 is greater than 2")

#endregion

#region [5] Python Comments

class PythonComments():
    def __init__(self):
        #This is a Comment
        #print("Hello, World!")
        print("Cheers, Mate!")

#endregion

#region [6.1] Python Variables

class PythonVariables():
    def __init__(self):
        x = 5
        y = "John"
        print(x)
        print(y)

        x=4
        x= "Sally"
        print(x)

        x = str(3)
        y = int(3)
        z = float(3)

        x = 5
        y = "John"
        print(type(x))
        print(type(y))

        x = "John"
        # is the same as
        x = 'John'

        a = 4
        A = "Sally"
        # A will not overwrite a

#endregion

#region [6.2] Variable Names

class VariableNames():
    def __init__(self):
        myvar = "John"
        my_var = "John"
        _my_var = "John"
        myVar = "John"
        MYVAR = "John"
        myvar2 = "John"

        #Camel Case
        myVariableName = "Camel"
        #Pascal Case
        MyVariableName = "Pascal"
        #Snake Case
        my_variable_name = "Snake"

#endregion

#region [6.3] Assign Multiple Values

class AssignMultipleValues():
    def __init__(self):
        fruits = ["apple", "banana", "orange"]
        x, y, z = fruits
        print(x)
        print(y)
        print(z)

        x = y = z = "Orange"
        print(x)
        print(y)
        print(z)



#endregion

#region [6.4] Output Variables

class OutputVariables():
    def __init__(self):
        x = "Python is awesome."
        print(x)
        
        x = "Python"
        y = "is"
        z = "awesome."
        print(x,y,z)
        print(x+y+z)

        x = 5
        y = 10
        print(x+y)

        x = 5
        y = "John"
        #Error:
        #print(x+y)
        #Allowed:
        print(x, y)




#endregion

#region [6.5] Global Variables

x = "awesome"

class GlobalVariables():
    def __init__(self):
        global x
        print("Python is " + x)

        x = "fantastic"
        print("Python is " +x)

    

#endregion

#region [7] Python Data Types

class PythonDataTypes():
    def __init__(self):
        
        #Print data type
        x = "Hello World"
        print(type(x))
        x = 20
        print(type(x))
        x = 20.5
        print(type(x))
        x = 1j
        print(type(x))
        x = ["apple", "banana", "cherry"]
        print(type(x))
        x = ("apple", "banana", "cherry")
        print(type(x))
        x = range(6)
        print(type(x)) #012345
        x = {"name" : "John", "Age" : 36}
        print(type(x))
        x = {"apple", "banana", "cherry"}
        print(type(x))
        x = frozenset({"apple", "banana", "cherry"})
        print(type(x))
        x = True 
        print(type(x))
        x = b"Hello"
        print(type(x))
        x = bytearray(5)
        print(type(x))
        x = memoryview(bytes(5))
        print(type(x))
        x = None 
        print(type(x))
        print()

        #Specify Data Type
        x = str("Hello World")
        print(x)
        x = int(123)
        print(x)
        x = float(20.5)
        print(x)
        x = complex(1j)
        print(x)
        x = list(("apple", "banana", "cherry"))
        print(x)
        x = tuple(("apple", "banana", "cherry"))
        print(x)
        x = range(6)
        print(x)
        x = dict(name="John", age=36)
        print(x)
        x = set(("apple", "banana", "cherry"))
        print(x)
        x = frozenset(("apple", "banana", "cherry"))
        print(x)
        x = bool(5)
        print(x)
        x = bytes(5)
        print(x)
        x = bytearray(5)
        print(x)
        x = memoryview(bytes(5))
        print(x)

        
        
#endregion

#region [8] Python Numbers

class PythonNumbers():
    def __init__(self):
        x = 1
        y = 2.5
        z = 1j

        scifloat = -87.7e100 #Sample scientific number with float

        complexformat = 3+5j
        complexformat2 = 5j
        complexformat3 = -5j

        #Convertion of values
        x = 1
        y = 2.8
        z = 1j

        a = float(x)
        b = int(y)
        c = complex(x)
        print(a)
        print(b)
        print(c)

        import random 

        print(random.randrange(1,100))



#endregion

#region [9] Casting

class Casting():
    def __init__(self):
        x = int(1)
        y = int(2.8)
        z = int("3")

        w = float("4.2")
        x = float(1)
        y = float(2.8)
        z = float("3")

        

        

#endregion

#region [10.1] Python Strings

class PythonStrings():
    def __init__(self):
        print("Hello")
        print('Hello')

        print("It's alright")
        print("'He is called, Johnny'")
        print('"He is called, Johnny"')

        a = "Hello"
        print(a)

        a = """Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
        sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua."""

        print(a)

        a = '''Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
        sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua.'''

        print(a)

        a = "Hello, World!"
        print(a[0])
        
        print()
        for x in "Banana":
            print(x)

        a = "Hello, World!"
        print(len(a))

        txt = "The best things in life are free."
        print("free" in txt)

        if "free" in txt:
            print("Yes, 'free' is present.")

        txt = "The best things in life are free!"
        print("expensive" not in txt)

        txt = "The best things in life are free!"
        if "expensive" not in txt:
            print("No, 'expensive' is NOT present.")

#endregion

#region [10.2] Slicing Strings


#endregion

#region Main

def main():
    print()
    PythonStrings()

if __name__ == "__main__":
    main()

#endregion