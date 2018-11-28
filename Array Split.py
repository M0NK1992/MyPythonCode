print("Enter the array of numbers seperated by spaces: \n")
arr=[int(x) for x in input().split()]
#arr= [0,0,0,-1,-1, -2,5,6]
arr.sort(reverse= True)
#arr.reverse()
count= len(arr)
#print(count)
print(arr)

#summing array elements
def summ(ar):
    arlen=len(ar)
    sum=0
    for i in range(arlen):
        sum= sum+ ar[i]
    return sum

#Sorting
j=0
k=0
arr1= []
arr2= []
sumarr1=0
sumarr2=0
for i in range(count):
    sumarr1= summ(arr1)
    sumarr2= summ(arr2)
    if i==0:
        arr1.append(arr[i])
        
    #Making sure the two arrays have elements
    elif sumarr1==sumarr2:
        if len(arr1)>len(arr2):
            arr2.append(arr[i])
        else:
            arr1.append(arr[i])
    #Adding elements to array based on their sum
    elif sumarr1>sumarr2 :
        if arr[i]<0:
            arr1.append(arr[i])
            
        else:
            arr2.append(arr[i])
            
    else:
        if arr[i]<0:
            arr2.append(arr[i])
            
        else:
            arr1.append(arr[i])
            
sumarr1= summ(arr1)
sumarr2= summ(arr2)
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Sum of Array 1:", sumarr1)
print("Sum of Array 2:", sumarr2)
if sumarr1>sumarr2:
    print("The difference is", sumarr1-sumarr2)
else:
    print("The difference is", sumarr2-sumarr1)


