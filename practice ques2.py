numbers = []
a=input("Enter numbers name")
b=input("Enter numbers name")
c=input("Enter numbers name")

numbers.append(a)
numbers.append(b)
numbers.append(c)

if (numbers.sort()==numbers.sort(reverse=True)):
    print("it's a palindrome")
else:
    print("fuck you nasty dirty bitch")                          