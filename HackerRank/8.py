if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
x,y=max(arr),min(arr)
for i in range(len(arr)):
    if(y<arr[i]):
        if(arr[i]<x):
            y=arr[i]
print(y)
