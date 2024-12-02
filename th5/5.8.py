print ("Nguyễn Danh Ánh")
print ("235752021610023")
print ("###########")
def Sequential_Search(dlist, item):
    for index, value in enumerate(dlist):
        if value == item:
            return True, index
    return False, -1 
def main():
    n = int(input("Nhập số phần tử của danh sách: "))
    dlist = []
    for i in range(n):
        element = int(input(f"Nhập phần tử thứ {i+1}: "))
        dlist.append(element)
    item = int(input("Nhập phần tử cần tìm: "))
    found, index = Sequential_Search(dlist, item)
    if found:
        print(f"Phần tử {item} được tìm thấy tại vị trí {index}.")
    else:
        print(f"Phần tử {item} không có trong danh sách.")
if __name__ == "__main__":
    main()
