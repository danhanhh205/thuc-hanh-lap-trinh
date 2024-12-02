print("Nguyễn Danh Ánh")
print("235752021610023")

def doc_toan_bo_file(ten_file):

  with open(ten_file, 'r') as file:
    noi_dung = file.read()
  return noi_dung


ten_file = (r"C:\zalo\ktddt\accc.txt")
noi_dung = doc_toan_bo_file(ten_file)

print(noi_dung)
