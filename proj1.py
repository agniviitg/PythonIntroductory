#Bubble Sort
def sort(arr):
    n = 0
    for x in arr:
        if x != 'End':
            n = n+1
        else:
            break
    while True:
        checker = 0
        x = arr[0]
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                checker = 1
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t
                i = i + 1
        if checker == 0:
            break

    print('Sorted array is')
    for i in range(n):
        print(arr[i])
i = 0
arr = [0]
while True:
    x = input("Enter any number or 'End' to stop the loop:")
    if x == 'End':
        break
    try:
        arr[i] = int(x)
    except:
        print("Enter a valid number")
sort(arr, i)
