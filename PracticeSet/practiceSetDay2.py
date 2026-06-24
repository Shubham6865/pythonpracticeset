print("1. Even or Odd Checker")
userNum = int(input("Enter num to check"))
if userNum % 2 ==0:
  print(f"{userNum} is Even")
else: print(f"{userNum} is Odd")

#-------------------------------------------------------------------
print("2. Positive Negative Zero Checker")
if userNum>=0:
  print("num is positive")
else: print("num is negative")

#-------------------------------------------------------------------
print("3. Largest of Two Numbers")
num1 =10
num2 =20
if num1>num2:
  print("largest num is num1")
elif num2>num1:
  print("largest num is num1")
else: print("both are same")

#-------------------------------------------------------------------
print("4. Largest of Three Numbers")

num3=50

if num1>= num2 and num1>num3:
  print(f"{num1} is largest.")
elif num2>=num1 and num2>=num3:
  print(f"{num2} is largest")
else: print(f"{num3} is largest")

#-------------------------------------------------------------------
print("5. Voting Eligibility Checker")

if userNum>18:
  print("you are eligiable for voting")
else: print("you are not eligiable for voting")

#-------------------------------------------------------------------
print("6. Leap Year Checker")
year=2001
if (( year %4==0 and year%100!=0)or year%400==0):
  print(f"{year} is leap year")
else: 
  print(f"{year} is not leap year")

#-------------------------------------------------------------------
print("7. Vowel or Consonant Checker")
check = 'f'
vowels = ['a','e','i','o','u']

if check in vowels:
  print(f"{check} is vowels")
else:
  print(f"{check} is consonant")

#-------------------------------------------------------------------
print("8. Grade Calculator")
marks =20
if marks>=90:
  print("A Grade")
elif marks>=70:
  print("B Grade")
elif marks>=40:
  print("C Grade")
else:
  print("D Grade")
#-------------------------------------------------------------------
print("9. Divisible by 5 and 11 Checker")
if marks%5==0 and marks%11==0:
  print("marks are Divisible by 5 and 11")
else:
  print("marks are not Divisible by 5 and 11")

#-------------------------------------------------------------------
print("10. Electricity Bill Calculator")
perunit=13
previousUnit=2344
currentUnit=2405

print(f"your current bill is {(currentUnit-previousUnit)*perunit}")