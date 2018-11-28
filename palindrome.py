print("Enter the string:")
string= str(input())
print("You entered:",string)
l= len(string)
palin=True
for i in range(0,l):
    if i==l:
        pal= True
    elif string[i]==string[l-1-i]:
        pal= True
    else:
        palin= False
        print("mismatch at",i,l-i)
if palin== False:
    print("it is not apalindrome")
else:
    print("Palindrome")