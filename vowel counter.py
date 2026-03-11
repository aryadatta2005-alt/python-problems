text=input("Enter a string: ")
print("The string you entered is:", text)
vowels = "AEIOUaeiou"
count=0
for char in text:
    if char in vowels:
        count+=1
print("Number of vowels in the string:", count)
