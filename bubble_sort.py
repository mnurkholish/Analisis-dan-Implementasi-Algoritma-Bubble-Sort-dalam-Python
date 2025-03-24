"""Bubble Sort"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

data = [-2, 45, 0, 11, -9]

sortedData = bubbleSort(data)

print(f'Data yang sudah diurutkan:\n{sortedData}')
