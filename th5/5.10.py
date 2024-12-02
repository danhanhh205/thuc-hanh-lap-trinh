print ("Nguyễn Danh Ánh")
print ("235752021610023")
print ("###########")
def binary_search(lst, value):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return True 
        elif lst[mid] < value:
            low = mid + 1  
        else:
            high = mid - 1 
    return False 
def main():
    n = int(input("Nhập số phần tử của danh sách: "))
    lst = []
    for i in range(n):
        element = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(element)
    lst.sort()
    value = int(input("Nhập phần tử cần tìm: "))
    found = binary_search(lst, value)
    if found:
        print(f"Phần tử {value} có trong danh sách.")
    else:
        print(f"Phần tử {value} không có trong danh sách.")
if __name__ == "__main__":
    main()
