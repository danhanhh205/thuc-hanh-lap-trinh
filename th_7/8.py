print("Nguyễn Danh Ánh")
print("235752021610023")
def write_list_to_file(list_data, filename):
  with open(filename, 'w') as f:
    for item in list_data:
      f.write(str(item) + '\n')

# Ví dụ sử dụng:
my_list = [1, 2, 3, "hello", "world"]
output_file = (r"C:\zalo\ktddt\accc.txt")

write_list_to_file(my_list, output_file)
print("Danh sách đã được ghi vào tệp", output_file)
