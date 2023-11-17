"""

print("Hey I am a good \nboy")
#\n is called escape sequence character it starts new line in our output
'''this is also a comment and 
this is a multiline comment in python'''
'''this is also a multiline comment we can include double quotes'''
print("hey i am a good \"boy\"")
#if we want to put some wprd or some sentences in double quotes then we have to use \""the main material will come inside these quotes either double or single quotes
print("hey", 6, 7, sep="-", end="009")#sep is used to seperate many words from specific points that we have given
'''as we have used end in above so when we write our code from next line then the output will come on the same line from the above output and the value whivh we will give inside end that value will be includedd in our output'''
'''and we can write \n in the end after giving value to it then our next output will come on the next line'''
print("Hey")


"""

#Now Variables and Data Types in python
a = 123456 #int data type
b = "Tony" #string data type always written in quotes
c = True
d = None
e = complex(4, 5)
x = ["apple", "banana", "cherry"]
y = ("apple", "banana", "cherry")
z = {"apple", "banana", "cherry"}
f = {"name" : "John", "age" : 36}
print(a)
a1 = 5
print(b)
print(e)
print(a + a1) #we can add same types of data types only
print("the type of a is ", type(a)) #this tells the type of data type
print("the type of b is ", type(b))
print("the type of c is ", type(c))
print("the type of d is ", type(d))
print("the type of e is ", type(e))
print("the type of x is ", type(x))
print("the type of y is ", type(y))
print("the type of z is ", type(z))
print("the type of f is ", type(f))