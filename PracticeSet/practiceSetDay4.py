# Reverse String
userInput= input("Enter String to reverse: ") or "shubham"

def reverseInput(input):
    revInp= input[::-1]
    return revInp

print(reverseInput(userInput))

#Check Palindrome

def checkPalindrome(input):
    
    if input.lower()== reverseInput(input):
        print(f"Provided {input} is Palindrome.")
    else:
        print(f"Provided {input} is Not Palindrome.")

checkPalindrome(userInput)

#largest Number in List

userList=[5,8,2,15,1]

def largestNum(inputList):
    # maxnum = max(inputList) #inbuild method
    maxnum =0
    for x in inputList:
        
      
        if x > maxnum:
            maxnum= x
          
    return maxnum

maximumnum = largestNum(userList)
print(f"larget num in {userList} is :{maximumnum}")


#Second Largest from list
myList = [10,20,30,5,25,14,85,12,62]
def secondMaxNum(inputList):
    
    maxinum = largestNum(inputList)
    inputList.remove(maxinum)
    secondMax = largestNum(inputList)
    
    return secondMax

print(secondMaxNum(myList))


#Count Vowels and consonants

def countVowelsandConsonants(input):
    vowels =0
    consonants=0

    for x in input:
        if x.lower() in ('a' , 'e' , 'i' , 'o' , 'u'):
            vowels+=1
        else:
            consonants+=1
    print(f"count of vowels: {vowels} and count of consonants: {consonants}")

countVowelsandConsonants(userInput)


#remove duplicate 

def removeDuplicate(input):
    
    removeDup = set(input)

    return list(removeDup)

print(removeDuplicate(userInput))