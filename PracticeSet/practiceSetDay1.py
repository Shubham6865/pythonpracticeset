print("1. Personal Introduction Program")

userinput = input("Enter your name: ") or "Shubham"
print(f"Hey {userinput}, how are you")

#-----------------------------------------------------

print("2. Sum of Two Numbers")
num1 = 10
num2= 20
print(f"sum of {num1} and {num2} is {num1+num2}")

#-----------------------------------------------------

print("3. Area of Rectangle")
length = 10
height = 20
areaOfRectangle= length* height
print(f"area of rectangle which has length of {length} and height of {height} is {areaOfRectangle}")

#-----------------------------------------------------

print("4. Temperature Converter degrees celsius to fahrenheit")

userdegreecelsius= int(input("Enter Temperature Converter degrees celsius "))
fahrenheit= (userdegreecelsius* (9/5))+32.0
# print(type(fahrenheit))
print(f"{userdegreecelsius} degrees celsius in fahrenheit is {fahrenheit}")
#-----------------------------------------------------

print("5. Swap Two Numbers")

num1 = 20
num2 = 10
print("before")
print(num1, num2)
temp = num1
num1=num2
num2=temp
print("after")
print(num1, num2)
#-----------------------------------------------------

print("6. Simple Interest Calculator")

principal = 10000
rateOfInterset= 10.2
timeInYears = 1

simpleInterset = (principal*rateOfInterset* timeInYears)/100

print(f"simple Interset is {simpleInterset}")
#-----------------------------------------------------

print("7. Marks Total Average Percentage")

english = 70
marathi =80
maths= 45
hindi = 60

avg = ((english+marathi+maths+hindi)/4)
print(f"Average percentage is {avg}")
#-----------------------------------------------------

print("8. Convert Minutes to Hours and Minutes")

min = 187

hours = min// 60
minutes = min%60

print (f"{min} minutes is {hours} hours and {minutes} minutes")

#-----------------------------------------------------

print("Age in Days Calculator")

age = 15
print(f"age in days {age*365.25}")

#-----------------------------------------------------

print("Stationery Bill Calculator")

pen = 10
pencil=5
book =20

noOfPens = int(input("Enter no of pen you want: "))
noOfPencil = int(input("Enter no of pencil you want: "))
noOfBooks = int(input("Enter no of book you want: "))


totalbill = ((noOfPens*pen)+(noOfPencil*pencil)+(noOfBooks*book))
print(f"your total stationery bill is {totalbill}")