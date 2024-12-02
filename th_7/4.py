print("Nguyễn Danh Ánh")
print("235752021610023")

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open (fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head(r'C:\zalo\ktddt\accc.txt',1)
