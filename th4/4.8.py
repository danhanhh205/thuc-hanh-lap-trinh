print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
chuoi = input("Nhập dãy các từ: ")
danh_sach_tu = chuoi.split()
do_dai_max = max(len(tu) for tu in danh_sach_tu)
tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == do_dai_max]
print("Từ dài nhất:", ", ".join(tu_dai_nhat))
