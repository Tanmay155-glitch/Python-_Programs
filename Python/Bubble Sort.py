arr = [int(x) for x in input("Enter a list of numbers: ").split()]

n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)  # Shows the array after each swap

print("Sorted list: ", arr)
