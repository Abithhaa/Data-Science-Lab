arr=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    arr.append(int(input(f"Enter elements {i+1}: ")))
print(f"The array is : {arr}")
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("sorted array is:",arr)

OUTPUT:
Enter the number of elements:5
Enter elements 1: 25
Enter elements 2: 6
Enter elements 3: 15
Enter elements 4: 3
Enter elements 5: 8
The array is : [25, 6, 15, 3, 8]
sorted array is: [3, 6, 8, 15, 25]
