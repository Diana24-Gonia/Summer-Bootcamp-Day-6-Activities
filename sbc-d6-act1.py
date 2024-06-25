#ACTIVITY PALINDROME
  
Empty = []
Words = input("Enter the word: ")
palindrome = "".join(reversed(Words.replace(" ","").lower()))

d = Words.replace(" ","").lower() 
Empty.append(d)

for i in Empty:
    if i == palindrome:
       print( Words, "Is a Palindrome" )
    else:
       print(f"'{Words}', {palindrome} Is not a palindrome",)