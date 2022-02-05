def reverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return reverse(str1[1: ])+str1[0]

string = input("Enter a word:::")
str1 = reverse(string)
print("word in reverse Order : ",str1)

if(string == str1):
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")

