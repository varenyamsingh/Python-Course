a = "Tony !!!!!!! Tony"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
# strings are immutable we cannot do changes in strings instead we can create new one

print(a.rstrip("!"))#this removes the extra strip characters like ! which comes at the end 

print(a.replace("Tony", "John"))
print(a.split(" "))#this split makes lists of that which we give input and the input which we have given must contain spaces in between

blogheading = "introduction to my blog"
print(blogheading.capitalize())#this helps us to make our first letter capital this feature is not available in javascript

str1 = "Welcome to the Console"
print(len(str1))
print(len(str1.center(50)))#this gives extra spaces to make our content in center of the page by using given spaces

print(a.count("Tony"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))#this is a boolean datatype it tells us wheather the given string ends with the given input or not

str2 = "He's name is michael fernandeze. and he is a good boy"
print(str2.find("is"))#it finds the given word in our document and tells us the exact index position of that specific word and agar vo word humare document me nhi hoga toh vo hume -1 return karega

#alphanumeric characters = A-Z, a-z, 0-9
str2 = "His name is michael fernandeze."
print(str2.isalnum())#tells whether the string is alphanumeric or not

str3 = "Welcome"
print(str3.isalpha())
str3 = "Welcome00"
print(str3.isalpha())

str3 = "Welcome"
print(str3.islower())
print(str3.isupper())#check whether string is lowercase or uppercase

str3 = "Welcome\n hey"
print(str3.isprintable())
str3 = "Welcome"
print(str3.isprintable())#tells us whether all the input given in our string is printable or not 

str3 = "    "#space done by using tab is a wide space
print(str3.isspace())
str3 = "Welcome        "
print(str3.isspace())#tells us whether we have used wide spaces or not

str3 = "Welcome"
print(str3.istitle())
str3 = "Welcome here we come"
print(str3.istitle())#tells us whethe all the words in our string is starting from capital or not

str3 = "Welcome here we come"
print(str3.startswith("Welcome"))
print(str3.startswith("Hello"))#tells whether the string starts with the given word or not

str3 = "Welcome here we come"
print(str3.swapcase())#converts lowercase to uppercase and vice-versa

str3 = "Welcome here we come"
print(str3.title())#makes all the starting words capital
