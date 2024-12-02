print("Nguyễn Danh Ánh")
print("235752021610023")
def copy_file_loop(source_file, destination_file):

  with open(source_file, 'r') as f_in, open(destination_file, 'w') as f_out:
    for line in f_in:
      f_out.write(line)

source = (r"C:\zalo\ktddt\accc.txt")
destination = (r"C:\zalo\ktddt\acccc.txt")
copy_file_loop(source, destination)
