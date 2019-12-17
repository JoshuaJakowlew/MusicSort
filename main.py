def main():
    arr = [99, 21, 19, 22, 28, 11, 14, 18, 1]
    print(arr)
    mergesort(arr, lambda x, y: x < y)
    print(arr)

 
def merge(left, right, arr, cmp):
    l = 0
    r = 0
    n = 0
 
    while l < len(left) and r < len(right):
        if cmp(left[l], right[r]):
            arr[n] = left[l]
            l += 1
        else:
            arr[n] = right[r]
            r += 1
 
        n += 1
  
    while l < len(left):
        arr[n] = left[l]
        l += 1
        n += 1
  
    while r < len(right):
        arr[n] = right[r]
        r += 1
        n += 1
 
def mergesort(arr, cmp):
    n = len(arr)
    if n < 2:
        return
 
    mid = n // 2
    left = arr[0:mid]
    right = arr[mid:n] 
 
    mergesort(left, cmp)
    mergesort(right, cmp)
 
    merge(left, right, arr, cmp)


if __name__ == "__main__":
    main()